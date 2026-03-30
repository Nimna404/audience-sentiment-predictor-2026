🎬 Box Office vs. Audience Sentiment: An End-to-End Data Pipeline

📌 Executive Summary

Can internet hype and review scores predict a movie's financial success? This full-stack data project extracts live movie data via APIs, engineers a clean dataset, visualizes audience vs. critic sentiment in Power BI, and deploys a Machine Learning model to test the predictive power of review scores on final Box Office revenue.

Spoiler: The math proves that making a "good" movie does not guarantee making a "profitable" movie.

📊 The Final Dashboard

(Note: Replace the link below with the actual path to your dashboard screenshot)

🏗️ Project Architecture & Methodology

This project was built from scratch following the complete Data Science Lifecycle:
1. Data Extraction (The API Pipeline)

   Script: src/fetch_dataset.py

   Process: Built a custom Python script to query the TMDb API (for the top-grossing movies from 2023-2026) and cross-reference them with the OMDb API to extract
   IMDb ratings, Rotten Tomatoes critic scores, and total Vote volume.

   Challenge Overcome: Handled API rate limiting using time.sleep() and dynamic JSON parsing.
2. Data Engineering & Cleaning

   Script: src/clean_data.py

   Process: Utilized pandas to transform messy, real-world JSON data into a clean, analysis-ready CSV.

   Transformations: Stripped currency symbols ($, ,), standardized text-to-integers, handled NaN (null) values for unreleased films, and mathematically scaled
   IMDb scores to a 100-point system to match Rotten Tomatoes.

3. Descriptive Analytics (Power BI)

   File: audience-sentiment-predictor-2026.pbix

   Process: Designed an executive-level dashboard prioritizing high data-to-ink ratios and intuitive UI.

   Key Features:

     Custom DAX Measures: Formatted raw integers into clean, readable KPIs (74%, 6.8/10, $28.4B).

     The "Square Zoom" Scatter Plot: Forced equal, fixed axes (20 to 100) on the scatter plot to visually expose the baseline leniency of general audiences
     compared to professional critics.

     Custom Tooltips: Built hidden report pages to provide specific movie details (Revenue, Year) when hovering over individual data points.

4. Predictive Analytics (Machine Learning)

   Script: src/predict_box_office.py

   Process: Developed a RandomForestRegressor via scikit-learn to test a financial hypothesis: Can we predict total revenue using only three variables (RT Score,
   IMDb Rating, IMDb Votes)?

   Methodology: Implemented an 80/20 train_test_split with a locked random_state to prevent data leakage and ensure reproducibility.

🧠 Core Business Insights

1. The "Audience Forgiveness" Gap: The Power BI scatter plot reveals a massive visual void in the bottom-right quadrant. Insight: Critics will happily score a
   movie a 20/100, but general audiences rarely rate a blockbuster below a 50/100. Audiences are inherently more forgiving.

2. Sentiment Does Not Equal Dollars: The Random Forest AI achieved an $R^2$ score of 0.34. While a junior analyst might view this as a low accuracy score, it
   mathematically proves a massive industry truth: Review scores only account for roughly 34% of a movie's Box Office variance. The other 66% is driven by outside
   factors.

🚧 Model Limitations & Future Iterations (V2)

To elevate the predictive model from a V1 Proof-of-Concept to production-grade accuracy ($R^2$ > 0.75), the following steps are required in future iterations:

Feature Expansion: The model is currently "feature starved." Future versions must integrate API data for Production Budget, Marketing (P&A) Spend, and an Existing                    IP Flag (e.g., Marvel/Sequel vs. Original).

Target Skewness Correction: Box office revenue is exponentially skewed (a few billion-dollar movies ruin the curve). Applying a Logarithmic Transformation
                            (np.log1p()) to the target variable will stabilize the Random Forest's variance.
                            
Cross-Validation: Replacing the single train/test split with K-Fold Cross-Validation to ensure model stability across smaller datasets.








## 📂 Repository Structure
```text
audience-sentiment-predictor/
│
├── Dashboard/
│   └── audience-sentiment-predictor-2026.pbix    # Power BI dashboard file
│
├── Data/
│   ├── Processed/
│   │   └── the_audience_cleaned.csv              # Cleaned, ML-ready data
│   └── Raw/
│       └── the_audience_master.csv               # Raw API output
│
├── Images/
│   └── audience-sentiment-predictor.png          # Dashboard screenshot for README
│
├── Src/
│   ├── clean_data.py                             # Pandas cleaning script
│   ├── fetch_dataset.py                          # API extraction script
│   └── predict_box_office.py                     # Scikit-learn Random Forest model
│
├── .gitignore                                    # Ignores .venv and system files
├── README.md                                     # Project documentation
└── requirements.txt                              # Python package dependencies
