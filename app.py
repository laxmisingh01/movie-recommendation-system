import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os 
# Page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Netflix style background
st.markdown("""
<style>
body {
    background-color: #141414;
}
.stApp {
    background-color: #141414;
    color: white;
}
h1 {
    color: #E50914;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# Fetch poster + details
def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=5a21a78346900dd5f1e5a03c7cd0b914&language=en-US"
        response = requests.get(url)

        data = response.json()

        poster = "https://via.placeholder.com/500x750?text=No+Image"

        if data.get("poster_path"):
            poster = "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

        overview = data.get("overview", "No overview available")
        rating = data.get("vote_average", "N/A")
        release = data.get("release_date", "N/A")

        return poster, overview, rating, release

    except:
        return (
            "https://via.placeholder.com/500x750?text=No+Image",
            "Overview unavailable",
            "N/A",
            "N/A"
        )


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []
    overviews = []
    ratings = []
    releases = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        poster, overview, rating, release = fetch_movie_details(movie_id)

        names.append(movies.iloc[i[0]].title)
        posters.append(poster)
        overviews.append(overview)
        ratings.append(rating)
        releases.append(release)

    return names, posters, overviews, ratings, releases

if os.path.exists("similarity.pkl") and os.path.getsize("similarity.pkl") < 1000000:
    os.remove("similarity.pkl")

if not os.path.exists("similarity.pkl"):   
    url = "https://drive.google.com/file/d/1J2c9Zk-yVro6rWpbg6Hqg1ezrG2EVoq1"
    gdown.download(url, "similarity.pkl", fuzzy=True)


# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# Title
st.markdown("<h1>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)


# Movie selector
selected_movie_name = st.selectbox(
    "Which movie do you like?",
    movies['title'].values
)


# Recommend button
if st.button("Recommend"):

    names, posters, overviews, ratings, releases = recommend(selected_movie_name)

    st.session_state.names = names
    st.session_state.posters = posters
    st.session_state.overviews = overviews
    st.session_state.ratings = ratings
    st.session_state.releases = releases


# Display recommendations
if "names" in st.session_state:

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i in range(5):

        with cols[i]:

            st.image(st.session_state.posters[i])
            st.markdown(f"**{st.session_state.names[i]}**")

            if st.button("Details", key=f"details_{i}"):

                st.write("⭐ Rating:", st.session_state.ratings[i])
                st.write("📅 Release Date:", st.session_state.releases[i])
                st.write("📖 Overview:", st.session_state.overviews[i])


# Footer
st.markdown("""
<style>
.footer {
position: fixed;
bottom: 0;
width: 100%;
background-color: #141414;
color: gray;
text-align: center;
padding: 10px;
font-size: 14px;
}
.footer a {
color: #E50914;
text-decoration: none;
margin: 0 10px;
}
</style>

<div class="footer">
Made by <b>Laxmi Singh</b> |
<a href="https://www.linkedin.com/in/laxmi-singh-369492297/">LinkedIn</a>
<a href="https://github.com/laxmisingh01">GitHub</a>
<a href="https://www.instagram.com/kindaa.lucky/">Instagram</a>
<a href="mailto:laxmisingh.works@gmail.com">Email</a>
<br><br>
© 2026 Laxmi Singh. All Rights Reserved.
</div>
""", unsafe_allow_html=True)