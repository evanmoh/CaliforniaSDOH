"""
SDOH Data Analysis Script
Performs power analysis and exploratory data analysis on the merged SDOH dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.power import TTestPower
import os

def load_dataset():
    """Load the processed SDOH dataset."""
    return pd.read_excel("SDOH_Final_Dataset.xlsx")

def perform_power_analysis(data):
    """
    Perform power analysis to determine if we have sufficient data
    for detecting relationships between health outcomes and demographics.
    """
    print("\nPower Analysis:")
    print("-" * 50)
    
    # Calculate effect sizes for key relationships
    health_outcomes = '% Fair or Poor Health'
    demographics = ['ACS_PCT_DISABLE_ZC', 'ACS_MEDIAN_AGE_ZC', 'ACS_PCT_HISPANIC_ZC']
    
    for demo in demographics:
        # Calculate correlation and effect size
        correlation = data[health_outcomes].corr(data[demo])
        effect_size = abs(correlation)
        
        # Calculate achieved power
        analysis = TTestPower()
        power = analysis.power(effect_size=effect_size, 
                             nobs=len(data), 
                             alpha=0.05)
        
        print(f"\nRelationship: {health_outcomes} vs {demo}")
        print(f"Effect size (correlation): {effect_size:.3f}")
        print(f"Sample size: {len(data)}")
        print(f"Achieved power: {power:.3f}")
        
        # Calculate required sample size for 0.80 power
        required_n = analysis.solve_power(effect_size=effect_size, 
                                        power=0.8, 
                                        alpha=0.05)
        print(f"Required sample size for 80% power: {int(required_n)}")

def create_demographic_analysis(data):
    """Analyze demographic distributions and create visualizations."""
    print("\nDemographic Analysis:")
    print("-" * 50)
    
    # Create output directory
    os.makedirs('analysis_outputs', exist_ok=True)
    
    # Population distribution by county
    plt.figure(figsize=(12, 6))
    data.groupby('county')['ACS_TOT_POP_WT_ZC'].sum().sort_values(ascending=False).head(15).plot(kind='bar')
    plt.title('Population Distribution by County (Top 15)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('analysis_outputs/population_distribution.png')
    plt.close()
    
    # Age vs Health Outcomes
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='ACS_MEDIAN_AGE_ZC', y='% Fair or Poor Health')
    plt.title('Median Age vs Poor Health Outcomes')
    plt.tight_layout()
    plt.savefig('analysis_outputs/age_vs_health.png')
    plt.close()
    
    # Demographics summary
    demo_summary = data[[
        'ACS_MEDIAN_AGE_ZC',
        'ACS_PCT_FEMALE_ZC',
        'ACS_PCT_HISPANIC_ZC',
        'ACS_PCT_DISABLE_ZC'
    ]].describe()
    
    print("\nDemographic Summary Statistics:")
    print(demo_summary)

def analyze_health_metrics(data):
    """Analyze health-related metrics and their relationships."""
    print("\nHealth Metrics Analysis:")
    print("-" * 50)
    
    # Correlation matrix of health metrics
    health_cols = [
        '% Fair or Poor Health',
        'Average Number of Physically Unhealthy Days',
        'Average Number of Mentally Unhealthy Days',
        '% Adults with Obesity',
        'Median HPSA Score',
        'Median AQI'
    ]
    
    # Create correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(data[health_cols].corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Between Health Metrics')
    plt.tight_layout()
    plt.savefig('analysis_outputs/health_correlations.png')
    plt.close()
    
    # Summary statistics for health metrics
    health_summary = data[health_cols].describe()
    print("\nHealth Metrics Summary Statistics:")
    print(health_summary)
    
    # Calculate ZIP codes with poor health indicators
    high_risk = data[
        (data['% Fair or Poor Health'] > data['% Fair or Poor Health'].median()) &
        (data['Median HPSA Score'] > data['Median HPSA Score'].median()) &
        (data['Median AQI'] > data['Median AQI'].median())
    ]
    
    print(f"\nHigh Risk Areas:")
    print(f"Number of ZIP codes with poor health indicators: {len(high_risk)}")
    print(f"Percentage of total: {(len(high_risk) / len(data)) * 100:.1f}%")

def analyze_geographic_disparities(data):
    """Analyze geographic disparities in health outcomes."""
    print("\nGeographic Disparities Analysis:")
    print("-" * 50)
    
    # Calculate county-level health metrics
    county_metrics = data.groupby('county').agg({
        '% Fair or Poor Health': 'mean',
        'Median HPSA Score': 'mean',
        'Median AQI': 'mean',
        'ACS_TOT_POP_WT_ZC': 'sum'
    }).round(2)
    
    # Sort by poor health percentage
    county_metrics = county_metrics.sort_values('% Fair or Poor Health', ascending=False)
    
    print("\nTop 10 Counties with Highest Poor Health Percentage:")
    print(county_metrics.head(10))
    
    # Visualize geographic disparities
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data, x='Median HPSA Score', y='% Fair or Poor Health')
    plt.title('Health Outcomes by HPSA Score Ranges')
    plt.tight_layout()
    plt.savefig('analysis_outputs/geographic_disparities.png')
    plt.close()

def main():
    """Main function to run all analyses."""
    try:
        # Load the processed dataset
        print("Loading SDOH dataset...")
        data = load_dataset()
        
        # Perform analyses
        perform_power_analysis(data)
        create_demographic_analysis(data)
        analyze_health_metrics(data)
        analyze_geographic_disparities(data)
        
        print("\nAnalysis completed! Check 'analysis_outputs' folder for visualizations.")
        
    except FileNotFoundError:
        print("Error: Could not find SDOH_Final_Dataset.xlsx. Please run the data processing script first.")
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()