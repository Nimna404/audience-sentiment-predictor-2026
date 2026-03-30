import pandas as pd                                                 # Import pandas for data manipulation
from sklearn.model_selection import train_test_split                # Import function to split data into train/test
from sklearn.ensemble import RandomForestRegressor                  # Import the Random Forest AI algorithm
from sklearn.metrics import mean_absolute_error, r2_score           # Import tools to measure AI accuracy

def train_box_office_model():                                       # Define the main machine learning function
# 1. Match the exact Windows path cleaned data
    data_path = r"E:\s23002167\Data Analytics\Projects\audience-sentiment-predictor-2026\Data\Processed\the_audience_cleaned.csv" # Set the path to the cleaned dataset
    
    print("Loading cleaned dataset for AI training...")             # Print status message to terminal
    df = pd.read_csv(data_path)                                     # Load the CSV data into a pandas DataFrame
    
# 21. DEFINE FEATURES (X) AND TARGET (Y)
    features = ['RT_Score', 'IMDb_Rating', 'IMDb_Votes']            # Select the sentiment/hype columns as inputs
    target = 'Box_Office'                                           # Select revenue as the target to predict
    
    X = df[features]                                                # Create the Feature Matrix (X)
    y = df[target]                                                  # Create the Target Vector (Y)
    
# 3. SPLIT THE DATASET
    # Hold back 20% of the data to test the AI on movies it hasn't seen yet
    X_train, X_test, y_train, y_test = train_test_split(            # Split data into training and testing sets
        X, y, test_size=0.2, random_state=42                        # 20% test size, seed 42 for reproducibility
    )                                                               # Close train_test_split function
    
# 4. INITIALIZE AND TRAIN THE AI MODEL
    print("Training the Random Forest algorithm...")                # Print status message to terminal
    model = RandomForestRegressor(n_estimators=100, random_state=42)# Create AI with 100 decision trees
    model.fit(X_train, y_train)                                     # Train the AI using the 80% training data
    
# 5. TEST THE AI ON THE HELD-BACK DATA
    print("Testing AI on unseen movies...")                         # Print status message to terminal
    predictions = model.predict(X_test)                             # Ask AI to predict box office for the 20% test set
    
# 6. EVALUATE ACCURACY
    r2 = r2_score(y_test, predictions)                              # Calculate R-Squared (0.0 to 1.0 accuracy score)
    mae = mean_absolute_error(y_test, predictions)                  # Calculate average dollar amount the AI was wrong by
    
    print("\n--- AI MODEL PERFORMANCE ---")                         # Print header for results
    print(f"R-Squared Score: {r2:.2f} (1.0 is perfect)")            # Print the R-Squared score
    print(f"Mean Absolute Error: ${mae:,.0f} off per movie")        # Print the average error in formatted dollars
    
    # 6. SIMULATE A NEW MOVIE PITCH
    print("\n--- EXECUTIVE PREDICTION TEST ---")                    # Print header for simulation
    print("Pitching: Blockbuster with 88% RT, 75 IMDb, 500k Votes") # Describe the fake movie inputs
    
    fake_movie = pd.DataFrame([[88, 75, 500000]], columns=features) # Construct fake movie data point
    predicted_rev = model.predict(fake_movie)[0]                    # Ask AI to predict its box office
    
    print(f"AI PREDICTS FINAL REVENUE: ${predicted_rev:,.0f}\n")    # Print the final predicted dollar amount

if __name__ == "__main__":                                          # Check if script is run directly (not imported)
    train_box_office_model()                                        # Execute the main machine learning function