# Pre-Screen-Submission: Overview
- Complete step by step execution is available on my Jupyter notebook with visualization highlights in my documentation file.
## Q1: Petrol additive clustering
- Performed descriptive analysis on the additives and identify distinct number of formulations present in data.
- There are 3 parts in this project:
> **Step 1. Identify Outliers:** Use DBSCAN to detect outliers in the data.
>
> **Step 2. Clustering:** Use K-Means Clustering to segregate the clean data observations into distinct number of formulations.
>
> **Step 3. Hypothesis Testing:** Apply Kruskal-Wallis test to verify if the formulations are significantly different. 

## Q2: Prediction on fresh fruit bunch (FFB) yield
- Identify important features and analyzed how they influence fresh fruit bunch (FFB) yield.
- Created a Tableau dashboard on [fresh fruit bunch yield analysis](https://public.tableau.com/views/OilPalmTreeYieldAnalysis/Dashboard1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
- There are 3 parts in this project:
> **Step 1. EDA + Feature Engineering:** I looked at the distributions of the numerical data and the value counts for the categorical variables. Then I created several new features using min-max ratio calculation and K-Means Clustering, which greatly reduced MAE baseline score to 0.515.
>
> **Step 2. Model Building:** I tried five different models on test set and evaluated them using MAE score:
- Random Forest Regressor
- Linear Regressor
- Lasso Regressor
- Gradient-boosting Regressor
The Random Forest Regressor model give the least MAE scores on the training and test sets.<br>After performing feature importance on the chosen model, most significant features for accuracy are **month, precipitation, harvested area and average temperature**, which are relevant to crop yield. 
>
## Q3: Analyze text given and answer questions provided
- Solutions in documentation file

## Codes and Resources Used
**Python Version:** Python 3.9<br>
**Packages:** numpy, matplotlib, seaborn, sklearn, nltk<br>
**DBSCAN Article:** https://medium.com/@dilip.voleti/dbscan-algorithm-for-fraud-detection-outlier-detection-in-a-data-set-60a10ad06ea8<br>
**Kruskal-Wallis Article:** https://www.geeksforgeeks.org/how-to-perform-a-kruskal-wallis-test-in-python/<br>









