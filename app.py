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
    'How do you like to be contacted ?', movies['title'].values
)
similarity = pickle.load(open('similarity.pkl', 'rb'))

if st.button('recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.title(names[0])
        st.image(posters[0])
    with col2:
        st.title(names[1])
        st.image(posters[1])
    with col3:
        st.title(names[2])
        st.image(posters[2])
    with col4:
        st.title(names[3])
        st.image(posters[3])
    with col5:
        st.title(names[4])
        st.image(posters[4])


