"""
SDOH (Social Determinants of Health) Data Processing Script
Combines multiple healthcare datasets for California counties and ZIP codes.
"""

import pandas as pd
import numpy as np
import unittest

# -----------------
# Data Processing Functions
# -----------------

def load_sdoh_data(file_path: str) -> pd.DataFrame:
    """Load SDOH dataset for California ZIPs with demographic indicators."""
    print("Processing SDOH Dataset...")
    data = pd.read_excel(file_path, sheet_name='Data')
    
    # Keep demographic and social indicator columns
    columns_to_keep = [
        'ZIPCODE', 'ZCTA', 'STATE',  # Geographic identifiers
        'ACS_TOT_POP_WT_ZC',         # Total population
        'ACS_PCT_CHILD_DISAB_ZC',    # Child disability %
        'ACS_PCT_DISABLE_ZC',        # Overall disability %
        'ACS_PCT_HISPANIC_ZC',       # Hispanic population %
        'ACS_MEDIAN_AGE_ZC',         # Median age
        'ACS_PCT_FEMALE_ZC',         # Female %
        'ACS_PCT_MALE_ZC',           # Male %
        'ACS_PCT_ENGL_NOT_WELL_ZC'   # Poor English proficiency %
    ]
    
    filtered_data = data[columns_to_keep]
    filtered_data = filtered_data[filtered_data['STATE'] == 'California']
    filtered_data['ZIPCODE'] = filtered_data['ZIPCODE'].astype(str).str.zfill(5)
    
    return filtered_data

def load_zip_code_crosswalk(file_path: str) -> pd.DataFrame:
    """Load and clean ZIP code to county mapping data."""
    print("Processing ZIP Code to County Crosswalk...")
    zip_data = pd.read_csv(file_path)
    
    # Keep only mapping columns and clean county names
    zip_data = zip_data[['zip', 'county']]
    zip_data['zip'] = zip_data['zip'].astype(str).str.zfill(5)
    zip_data['county'] = zip_data['county'].str.replace(' County', '', regex=False).str.strip()
    
    return zip_data

def process_hpsa_data(file_path: str) -> pd.DataFrame:
    """Process Healthcare Professional Shortage Area scores by county."""
    print("Processing HPSA Dataset...")
    data = pd.read_excel(file_path)
    
    # Calculate median HPSA scores by county
    data['County Equivalent Name'] = data['County Equivalent Name'].str.replace(' County', '', regex=False).str.strip()
    hpsa_scores = data.groupby('County Equivalent Name')['HPSA Score'].median().reset_index()
    hpsa_scores.columns = ['county', 'Median HPSA Score']
    
    return hpsa_scores

def process_aqi_data(file_path: str) -> pd.DataFrame:
    """Process Air Quality Index data for California counties."""
    print("Processing AQI Dataset...")
    data = pd.read_csv(file_path)
    
    # Filter for California and clean county names
    data = data[data['State'].str.lower() == 'california']
    data['County'] = data['County'].str.replace(' County', '', regex=False).str.strip()
    
    return data[['County', 'Median AQI']]

def process_chr_data(file_path: str) -> pd.DataFrame:
    """Process County Health Rankings data for health metrics."""
    print("Processing County Health Rankings Dataset...")
    data = pd.read_excel(file_path, sheet_name='Ranked Measure Data', skiprows=1)
    
    # Select relevant health metrics
    columns_to_keep = [
        'State', 'County',
        '% Fair or Poor Health',
        'Average Number of Physically Unhealthy Days',
        'Average Number of Mentally Unhealthy Days',
        '% Adults with Obesity',
        'Food Environment Index',
        '% Physically Inactive',
        '% Vaccinated'
    ]
    
    chr_filtered = data[columns_to_keep]
    chr_filtered = chr_filtered[chr_filtered['State'].str.lower() == 'california']
    chr_filtered['County'] = chr_filtered['County'].str.replace(' County', '', regex=False).str.strip()
    
    return chr_filtered

def merge_datasets(sdoh: pd.DataFrame, zip_crosswalk: pd.DataFrame,
                  hpsa: pd.DataFrame, aqi: pd.DataFrame,
                  chr_data: pd.DataFrame) -> pd.DataFrame:
    """Merge all datasets into final comprehensive dataset."""
    print("Merging datasets...")
    
    # Merge steps - using left joins to keep all ZIP codes
    merged = pd.merge(sdoh, zip_crosswalk, left_on='ZIPCODE', right_on='zip', how='left')
    merged = pd.merge(merged, hpsa, on='county', how='left')
    merged = pd.merge(merged, aqi, left_on='county', right_on='County', how='left')
    final = pd.merge(merged, chr_data, left_on='county', right_on='County', how='left')
    
    # Clean up duplicate columns
    columns_to_drop = ['zip', 'County_x', 'County_y', 'State']
    final.drop(columns=[col for col in columns_to_drop if col in final.columns], inplace=True)
    
    return final

def analyze_coverage(final_dataset: pd.DataFrame) -> None:
    """Analyze and report dataset coverage using SDOH as baseline."""
    total_zips = len(final_dataset)
    
    print("\nDataset Coverage Analysis:")
    print("-" * 50)
    print(f"Total SDOH records (baseline): {total_zips:,}")
    
    # County coverage
    has_county = final_dataset['county'].notna().sum()
    county_pct = (has_county / total_zips) * 100
    print(f"\nCounty Matching:")
    print(f"Records with county data: {has_county:,} ({county_pct:.1f}%)")
    
    # HPSA coverage
    has_hpsa = final_dataset['Median HPSA Score'].notna().sum()
    hpsa_pct = (has_hpsa / total_zips) * 100
    print(f"\nHPSA Coverage:")
    print(f"Records with HPSA scores: {has_hpsa:,} ({hpsa_pct:.1f}%)")
    
    # AQI coverage
    has_aqi = final_dataset['Median AQI'].notna().sum()
    aqi_pct = (has_aqi / total_zips) * 100
    print(f"\nAQI Coverage:")
    print(f"Records with AQI data: {has_aqi:,} ({aqi_pct:.1f}%)")
    
    # CHR coverage
    chr_col = '% Fair or Poor Health'
    has_chr = final_dataset[chr_col].notna().sum()
    chr_pct = (has_chr / total_zips) * 100
    print(f"\nCounty Health Rankings Coverage:")
    print(f"Records with CHR data: {has_chr:,} ({chr_pct:.1f}%)")
    
    # Complete records
    complete_records = final_dataset.dropna(subset=[
        'county',
        'Median HPSA Score',
        'Median AQI',
        chr_col
    ]).shape[0]
    complete_pct = (complete_records / total_zips) * 100
    print(f"\nComplete Coverage:")
    print(f"Records with all data sources: {complete_records:,} ({complete_pct:.1f}%)")
    
    # Geographic summary
    unique_zips = final_dataset['ZIPCODE'].nunique()
    unique_counties = final_dataset['county'].dropna().nunique()
    print(f"\nGeographic Summary:")
    print(f"Unique ZIP codes: {unique_zips:,}")
    print(f"Unique counties: {unique_counties:,} (out of 58 CA counties)")
    print(f"Average ZIP codes per county: {unique_zips/unique_counties:.1f}")

# -----------------
# Simple Tests
# -----------------

class TestDataProcessing(unittest.TestCase):
    """Simple tests for data processing functions."""
    
    def test_zip_code_formatting(self):
        """Test ZIP code standardization to 5 digits."""
        test_data = pd.DataFrame({
            'zip': ['1234', '94025', '944'],
            'county': ['Test County 1', 'Test County 2', 'Test County 3']
        })
        result = load_zip_code_crosswalk(test_data)
        self.assertTrue(all(result['zip'].str.len() == 5))
        self.assertTrue('01234' in result['zip'].values)
    
    def test_county_name_cleaning(self):
        """Test removal of 'County' suffix from names."""
        test_data = pd.DataFrame({
            'County Equivalent Name': ['Orange County', 'Los Angeles County'],
            'HPSA Score': [10, 15]
        })
        result = process_hpsa_data(test_data)
        self.assertTrue('Orange' in result['county'].values)
        self.assertFalse(any(result['county'].str.contains('County')))

# -----------------
# Main Execution
# -----------------

def main():
    """Main function to process and merge all datasets."""
    # Define file paths
    source_dir = 'Source/'
    sdoh_file = source_dir + 'SDOH_2020_ZIPCODE_1_0.xlsx'
    zip_crosswalk_file = source_dir + 'zip_code_database.csv'
    hpsa_file = source_dir + 'all-primary-care-hpsas.xlsx'
    aqi_file = source_dir + 'annual_aqi_by_county_2024.csv'
    chr_file = source_dir + '2023 County Health Rankings Data - v2.xlsx'
    
    try:
        # Load and process each dataset
        sdoh_data = load_sdoh_data(sdoh_file)
        zip_crosswalk = load_zip_code_crosswalk(zip_crosswalk_file)
        hpsa_data = process_hpsa_data(hpsa_file)
        aqi_data = process_aqi_data(aqi_file)
        chr_data = process_chr_data(chr_file)
        
        # Merge datasets
        final_dataset = merge_datasets(sdoh_data, zip_crosswalk, hpsa_data, aqi_data, chr_data)
        
        # Save dataset
        output_file = "SDOH_Final_Dataset.xlsx"
        final_dataset.to_excel(output_file, index=False)
        print(f"\nFinal dataset saved as {output_file}")
        
        # Analyze and report coverage
        analyze_coverage(final_dataset)
        
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {str(e)}")
    except Exception as e:
        print(f"Error processing data: {str(e)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        unittest.main(argv=['first-arg-is-ignored'])
    else:
        main()