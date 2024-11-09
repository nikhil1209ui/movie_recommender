import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=da7191990c9338ad01eaa3515e90b81c&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original"+data["poster_path"]

movie_dict = pickle.load(open('df_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

st.title("Movies Recommender System")

selected_movie_name = st.selectbox(
    'Select a Movie', movies['title'].values
)

# for getting similarity.pkl as one
chunk_files = [
    "similarity_part_0.pkl", "similarity_part_1.pkl", "similarity_part_2.pkl", "similarity_part_3.pkl",
    "similarity_part_4.pkl", "similarity_part_5.pkl",
    "similarity_part_6.pkl", "similarity_part_7.pkl", "similarity_part_8.pkl",
    "similarity_part_9.pkl", "similarity_part_10.pkl"
]

# List to store all loaded chunks
all_chunks = []

# Load each chunk and append its data to `all_chunks`
for chunk_file in chunk_files:
    with open(chunk_file, 'rb') as file:
        chunk_data = pickle.load(file)
        all_chunks.extend(chunk_data)  # Extend by chunk data

similarity = all_chunks

if st.button('recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f"<h3 style='text-align: center; font-size: 16px;'>{names[0]}</h3>", unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        st.markdown(f"<h3 style='text-align: center; font-size: 16px;'>{names[1]}</h3>", unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        st.markdown(f"<h3 style='text-align: center; font-size: 16px;'>{names[2]}</h3>", unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(f"<h3 style='text-align: center; font-size: 16px;'>{names[3]}</h3>", unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(f"<h3 style='text-align: center; font-size: 16px;'>{names[4]}</h3>", unsafe_allow_html=True)
        st.image(posters[4])