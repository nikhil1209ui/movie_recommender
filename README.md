Data used : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Framework used : Streamlit

<img width="575" alt="image" src="https://github.com/user-attachments/assets/767b1453-d766-4535-8dca-5d7117bc2f47">


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Movie Recommender System
-
This project is a movie recommendation system that provides recommendations based on movie similarity using content-based filtering. It involves data preprocessing, feature engineering, vectorization, model building, and deployment using Streamlit for a user-friendly interface.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Workflow:-
   -

Data Ingestion -> Feature Engineering -> Vectorization -> Similarity Calculation-> Model Saving -> Streamlit Interface -> User Interaction -> Recommendation Display

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Feature Engineering Flow:-
   -

Raw Data -> Convert JSON Columns -> Concatenate Tags -> Clean Text -> Generate Vectors

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Project Structure
-
1. Data Preparation: Merging datasets and extracting relevant features.
2. Feature Engineering: Transforming raw data into meaningful tags.
3. Vectorization: Converting text data into vectors using CountVectorizer.
4. Model Building: Computing cosine similarity to measure movie similarity.
5. Deployment: Building a web interface using Streamlit.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Data Preparation
   -
   Two datasets, tmdb_5000_movies.csv and tmdb_5000_credits.csv, are merged on the movie title to consolidate information.

2. Feature Engineering
   -
2.1 Extracting Key Information:
  
   
   Several columns contain complex, nested information. To prepare them for analysis, these fields are transformed using helper functions.

   Genres and Keywords: Extract genre and keyword names.

   Cast: Retrieve up to three main cast members.

   Crew: Extract the director's name.


2.2. Text Preprocessing

  Text data is tokenized and cleaned by removing spaces and converting to lowercase to ensure uniformity. All tags are combined into a single feature (tags).
  
3. Vectorization
   -
   The CountVectorizer is used to convert text data into numerical vectors. Stemming with the Porter Stemmer reduces words to their root forms, enhancing the model's ability 
   to recognize similarities.

4. Model Building
   -
4.1. Calculating Similarity
  
   Cosine similarity is used to find similarities between movies. For a given movie, the function recommend() retrieves the top 5 similar movies based on cosine distances.
   
4.2. Saving Model Artifacts
  
  The similarity matrix and processed data are saved as pickle files to be loaded in the deployment environment.


5. Deployment with Streamlit
   -
5.1. Setting Up Streamlit

   The web interface, created using Streamlit, provides an interactive selection menu for users to choose a movie and receive recommendations. The movie poster is fetched    
   using the TMDB API.

5.2. Fetching Movie Posters

   The fetch_poster() function uses the TMDB API to retrieve posters of recommended movies.

   
