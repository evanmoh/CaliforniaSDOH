
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
Demographic Analysis:
--------------------------------------------------

Demographic Summary Statistics:
       ACS_MEDIAN_AGE_ZC  ACS_PCT_FEMALE_ZC  ACS_PCT_HISPANIC_ZC  ACS_PCT_DISABLE_ZC
count        2536.000000        2552.000000          2552.000000         2543.000000
mean           40.193849          49.279949            31.859193           12.506465
std             9.156933           6.654993            23.989631            6.922351
min            15.900000           0.000000             0.000000            0.000000
25%            34.200000          48.457500            13.362500            8.865000
50%            38.250000          50.300000            24.460000           10.910000
75%            44.600000          51.740000            46.810000           14.480000
max            79.500000         100.000000           100.000000          100.000000

Health Metrics Analysis:
--------------------------------------------------

Health Metrics Summary Statistics:
       % Fair or Poor Health  Average Number of Physically Unhealthy Days  Average Number of Mentally Unhealthy Days  % Adults with Obesity  Median HPSA Score   Median AQI
count            2585.000000                                  2585.000000                                2585.000000            2585.000000        2584.000000  2431.000000
mean               15.104990                                     3.227852                                   4.678314              29.404023           8.430534    46.447141
std                 3.046054                                     0.419772                                   0.318268               4.562157           5.473718    11.135140
min                 9.500000                                     2.450219                                   3.972747              19.000000           0.000000    15.000000
25%                13.000000                                     3.007288                                   4.451347              28.100000           3.000000    37.000000
50%                15.600000                                     3.114880                                   4.643930              28.800000          12.000000    46.000000
75%                16.500000                                     3.516812                                   4.872720              31.700000          12.000000    59.000000
max                24.000000                                     4.161616                                   5.510197              39.100000          16.000000    67.000000

High Risk Areas:
Number of ZIP codes with poor health indicators: 323
Percentage of total: 12.5%

Geographic Disparities Analysis:
--------------------------------------------------

Top 10 Counties with Highest Poor Health Percentage:
          % Fair or Poor Health  Median HPSA Score  Median AQI  ACS_TOT_POP_WT_ZC
county                                                                           
Imperial                   24.0               10.0        54.0           267840.0
Tulare                     22.8               15.0        52.0           930782.0
Merced                     21.7               11.0         NaN           362132.0
Kern                       21.2               14.0        52.0          1635374.0
Madera                     21.2               15.0         NaN           206705.0
Fresno                     20.2               12.0        49.0          2380221.0
Kings                      20.1               10.0         NaN           218803.0
Colusa                     19.2               12.0        53.0            21662.0
Glenn                      18.7                5.0        27.0            44498.0
Monterey                   18.3               15.0        37.0           620939.0
