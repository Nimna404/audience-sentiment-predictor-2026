import requests                                                 # Load network library
import pandas as pd                                             # Load dataframe library
import time                                                     # Load timing library

TMDB_API_KEY = "6da5591887843bb1f8ac7648489d4556"                              # Set TMDb credential
OMDB_API_KEY = "?i=tt3896198&apikey=e1476484"                                      # Set OMDb credential

def fetch_movies(year):                                         # Define fetch function
    movies_data = []                                            # Initialize empty list
    tmdb_url = "https://api.themoviedb.org/3/discover/movie"    # Set TMDb endpoint
    params = {                                                  # Open parameters dict
        "api_key": TMDB_API_KEY,                                # Pass auth key
        "primary_release_year": year,                           # Pass target year
        "sort_by": "revenue.desc"                               # Sort by box office
    }                                                           # Close parameters dict
    
    response = requests.get(tmdb_url, params=params)            # Execute HTTP GET
    results = response.json().get("results", [])                # Extract results array
    
    for movie in results[:50]:                                  # Loop top 50 movies
        title = movie.get("title")                              # Extract title
        
        omdb_url = "http://www.omdbapi.com/"                    # Set OMDb endpoint
        omdb_params = {                                         # Open parameters dict
            "apikey": OMDB_API_KEY,                             # Pass auth key
            "t": title,                                         # Pass movie title
            "y": year                                           # Pass release year
        }                                                       # Close parameters dict
        
        omdb_res = requests.get(omdb_url, params=omdb_params)   # Execute HTTP GET
        omdb_data = omdb_res.json()                             # Parse JSON response
        
        rt_score = None                                         # Initialize default score
        if "Ratings" in omdb_data:                              # Check ratings existence
            for rating in omdb_data["Ratings"]:                 # Loop through ratings
                if rating["Source"] == "Rotten Tomatoes":       # Check for RT source
                    rt_score = rating["Value"]                  # Extract RT score
        
        movies_data.append({                                    # Append dict to list
            "Title": title,                                     # Store title
            "Year": year,                                       # Store year
            "IMDb_Rating": omdb_data.get("imdbRating"),         # Store IMDb score
            "IMDb_Votes": omdb_data.get("imdbVotes"),           # Store vote count
            "Box_Office": omdb_data.get("BoxOffice"),           # Store revenue
            "RT_Score": rt_score                                # Store critic score
        })                                                      # Close dictionary
        
        print(f"Fetched data for: {title}")                     # Print progress update
        time.sleep(0.2)                                         # Pause for rate limits
        
    return movies_data                                          # Return final list

all_movies = []                                                 # Initialize master list
for target_year in range(2023, 2027):                           # Loop recent years
    yearly_data = fetch_movies(target_year)                     # Call fetch function
    all_movies.extend(yearly_data)                              # Add to master list
    
df = pd.DataFrame(all_movies)                                   # Convert list to DataFrame
df.to_csv("the_audience_master.csv", index=False)               # Export data to CSV
print("Dataset generation complete. Saved as CSV.")             # Print success message