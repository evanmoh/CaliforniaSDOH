
# California SDOH Dataset: README
## 1. Executive Summary
The California SDOH dataset was developed to address key challenges with existing Social Determinants of Health data, including data silos, lack of interoperability, and limited California-specific insights. This comprehensive dataset harmonizes ZIP code, county, and state-level data while integrating multiple robust sources, such as SDOH, HPSA, AQI, and County Health Rankings, to provide granular, actionable insights for policymakers, healthcare professionals, and researchers.

### Potential Applications:
Policy analysis to address health disparities in California regions.
Identifying underserved areas for healthcare interventions.
Environmental impact assessments on public health.
Resource allocation and targeted policy-making at ZIP code and county levels.

## 2. Description of Data
### Data Sources:
SDOH Dataset: Provides national demographic and social indicators (e.g., % uninsured, median household income).
ZIP Code Crosswalk: Links ZIP codes to counties for geographic harmonization.
HPSA Data: Healthcare Professional Shortage Area scores for measuring healthcare access.
AQI Data: County-level median air quality metrics for environmental insights.
County Health Rankings (CHR): Key health metrics, including physical inactivity, food environment index, and % adults with obesity.
### Key Variables:
Demographic Indicators: Population, % Hispanic, % English not proficient, % uninsured.
Healthcare Metrics: Median HPSA score, access to primary care.
Environmental Metrics: Median AQI values (e.g., PM2.5 levels).
Health Outcomes: % fair/poor health, physically inactive adults, food environment index.



## 3. Power Analysis
![image](https://github.com/user-attachments/assets/2fd7b4c0-b2ad-48ea-9a84-13af8e5c251a)


## 4. Exploratory Analysis
![image](https://github.com/user-attachments/assets/e1555875-b505-483e-a0d4-6fc07ebb1f1e)
![image](https://github.com/user-attachments/assets/79be11d9-b95d-4ed3-a9db-cacfbb66d818)
![image](https://github.com/user-attachments/assets/3f0f6674-2011-464b-8f2c-3cba8a24b5d2)

## 5. Source Files
Raw Excel Files: https://github.com/evanmoh/CaliforniaSDOH/tree/main/Source </b>
SDOH Data from AHRQ (Zip-code level, 2023): https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html</b>
AQI Data from EPA: https://aqs.epa.gov/aqsweb/airdata/download_files.html</b>
County Health Ranking (CHR) Data: https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation</b>
USDA Food Access Data: https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data/

## 6. Data Transformation File
https://github.com/evanmoh/CaliforniaSDOH/blob/main/SDOH_Transform.py

## 7. Power Analysis and Exploratory Analysis
https://github.com/evanmoh/CaliforniaSDOH/blob/main/EDA_PowerAnalysis.py

## 8. Data Coverage
### Dataset Coverage and Completeness:
Our dataset comprehensively covers California's healthcare landscape, with excellent coverage across multiple data sources. The baseline SDOH dataset includes 2,585 unique ZIP codes across California. Here's a detailed breakdown of our coverage:

### Geographic Coverage:
Complete coverage of all 58 California counties
2,585 unique ZIP codes represented
Average of 44.6 ZIP codes per county, indicating good distribution across counties

### Data Source Integration:
County and HPSA Data: Nearly perfect integration with 2,584 records (100.0%) having both county assignments and HPSA scores
Air Quality Data: Strong coverage with 2,431 records (94.0%) containing AQI measurements
County Health Rankings: Complete coverage with all 2,585 records (100.0%) including CHR metrics

### Completeness:
94.0% of records (2,431) have complete data across all sources
The primary gap appears in AQI coverage, which affects 6% of records
The matching and integration process maintained data integrity, with minimal loss of information
This high level of coverage suggests that our dataset provides a robust foundation for analyzing health determinants across California. The complete county coverage and high ZIP code representation make it particularly valuable for both broad county-level analysis and more granular ZIP code-level investigations. The small gap in AQI coverage should be considered when conducting environmental health analyses, but it doesn't significantly impact the dataset's overall utility.

## 8. California SDOH Data Limitations
The SDOH dataset, while comprehensive, has several important limitations to consider:
### Temporal Limitations:
The dataset primarily uses 2020 data, which may not accurately reflect current conditions. Additionally, the data collection period coincided with the COVID-19 pandemic, potentially creating atypical patterns in health outcomes and healthcare access. The cross-sectional nature of the data also means we cannot observe trends or changes over time.
### Geographic Coverage:
While we aimed to cover all California counties and ZIP codes, some geographic areas have incomplete data. Rural areas are particularly susceptible to underrepresentation. Furthermore, ZIP code boundaries don't always align with healthcare service areas or community boundaries, which may affect the accuracy of service accessibility measurements.
### Data Quality and Integration:
The merging of multiple data sources (SDOH, HPSA, AQI, and County Health Rankings) introduces challenges due to different collection methodologies and reporting periods. Some ZIP codes have missing data for certain metrics, particularly in health outcomes and air quality measurements. The aggregated nature of the data at both ZIP code and county levels masks individual-level variations and local disparities.
### Demographic Representation:
The demographic categories in the dataset are broadly defined, potentially oversimplifying the diversity within communities. Income and wealth distribution data may not fully capture economic disparities. Language barriers during data collection might have affected the accuracy of reported health outcomes in non-English-speaking communities.
### Healthcare Access Metrics:
The HPSA scores, being county-level measurements, don't capture local variations in healthcare access within counties. The dataset lacks detailed information about specialty care availability and doesn't fully account for transportation barriers that might affect healthcare access. Quality metrics for healthcare services are limited.
### Environmental Factors:
Air Quality Index (AQI) data is only available at the county level, missing important local variations in air quality. The dataset lacks comprehensive environmental health indicators and doesn't capture seasonal environmental variations that might affect health outcomes. Other environmental risk factors such as water quality and noise pollution are not included.
### Methodological Constraints:
The aggregated nature of the data makes it susceptible to ecological fallacy, where group-level correlations might not reflect individual-level relationships. Self-reporting bias in health outcomes may affect data accuracy. The different spatial scales used across datasets (ZIP code vs. county level) create challenges in precise geographic analysis.
These limitations should be considered when using this dataset for analysis or decision-making purposes. Users should exercise appropriate caution when making inferences, particularly for small geographic areas or specific demographic groups.



