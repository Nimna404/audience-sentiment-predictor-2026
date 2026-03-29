import pandas as pd                                                 # Load dataframe library
import numpy as np                                                  # Load numerical library for NaN handling

def process_audience_data():                                        # Define cleaning function
    # Match the exact Windows paths from your fetch script
    raw_file = r"E:\s23002167\Data Analytics\Projects\audience-sentiment-predictor-2026\Data\Raw\the_audience_master.csv"
    clean_file = r"E:\s23002167\Data Analytics\Projects\audience-sentiment-predictor-2026\Data\Processed\the_audience_cleaned.csv"
    
    print("Loading raw dataset...")
    df = pd.read_csv(raw_file)                                      # Load raw dataset
    
    # 1. HANDLE MISSING & UNRELEASED DATA
    df.replace("N/A", np.nan, inplace=True)                         # Convert literal "N/A" strings to true nulls
    df.dropna(subset=['Box_Office', 'RT_Score', 'IMDb_Rating', 'IMDb_Votes'], inplace=True) # Drop incomplete movies
    
    # 2. CLEAN BOX OFFICE (Remove $ and commas)
    df['Box_Office'] = df['Box_Office'].astype(str)                 # Force string type
    df['Box_Office'] = df['Box_Office'].str.replace('$', '', regex=False) # Remove dollar signs
    df['Box_Office'] = df['Box_Office'].str.replace(',', '', regex=False) # Remove commas
    df['Box_Office'] = pd.to_numeric(df['Box_Office'])              # Convert to pure integer/float
    
    # 3. CLEAN IMDB VOTES (Remove commas)
    df['IMDb_Votes'] = df['IMDb_Votes'].astype(str)                 # Force string type
    df['IMDb_Votes'] = df['IMDb_Votes'].str.replace(',', '', regex=False) # Remove commas
    df['IMDb_Votes'] = pd.to_numeric(df['IMDb_Votes'])              # Convert to pure integer
    
    # 4. CLEAN ROTTEN TOMATOES SCORE (Remove %)
    df['RT_Score'] = df['RT_Score'].astype(str)                     # Force string type
    df['RT_Score'] = df['RT_Score'].str.replace('%', '', regex=False)     # Remove percent signs
    df['RT_Score'] = pd.to_numeric(df['RT_Score'])                  # Convert to pure integer
    
    # 5. STANDARDIZE METRICS
    df['IMDb_Rating'] = pd.to_numeric(df['IMDb_Rating'])            # Ensure numeric rating
    df['IMDb_Rating'] = df['IMDb_Rating'] * 10                      # Scale IMDb to 100 to match RT
    
    # 6. EXPORT
    df.to_csv(clean_file, index=False)                              # Export clean dataset
    
    # Print a summary to prove it worked
    print(f"\nSuccess! Cleaned {len(df)} movies.")
    print(f"Clean data saved to:\n{clean_file}")                    # Print confirmation

if __name__ == "__main__":                                          # Check main execution
    process_audience_data()                                         # Run the function