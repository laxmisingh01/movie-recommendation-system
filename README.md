# movie-recommendation-system

A **Netflix-style Movie Recommendation Web App** built using **Python, Streamlit, and Machine Learning**.
The system recommends movies similar to the one selected by the user using **content-based filtering**.

---

## 🚀 Features

* 🎥 Recommend **5 similar movies**
* 🖼 Display **movie posters**
* ⭐ Show **ratings**
* 📅 Show **release date**
* 📖 Show **movie overview**
* 🎨 **Netflix-style UI** built with Streamlit
* ⚡ Fast recommendations using **cosine similarity**

---

## 🧠 How It Works

This project uses a **Content-Based Recommendation System**.

Steps used:

1. Movie dataset is cleaned and processed.
2. Important features like **genres, keywords, cast, and crew** are combined into a single column.
3. Text data is converted into vectors using **CountVectorizer**.
4. **Cosine similarity** is used to measure similarity between movies.
5. The system recommends the **top 5 most similar movies**.

---

## 🛠 Tech Stack

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**
* **Pickle**
* **TMDB API**
* **Requests**

---

## 📂 Project Structure

```
movie-recommender-system
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/laxmisingh01/movie-recommender-system.git
```

Go to the project folder:

```bash
cd movie-recommender-system
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

Run the Streamlit application:

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## 📸 Demo

Example interface:

* Select a movie
* Click **Recommend**
* Get **5 similar movies with posters and details**

You can add screenshots here later.

---

## 🔑 API Used

This project uses the **TMDB API** to fetch movie posters and details.

Website:
https://www.themoviedb.org/

---

## 📌 Future Improvements

* 🔍 Search suggestions while typing
* 🎬 Trending movies section
* ❤️ Add to favorites
* 👤 User login system
* 📊 Better recommendation algorithm

---

## 👩‍💻 Author

**Laxmi Singh**

LinkedIn:
https://www.linkedin.com/in/laxmi-singh-369492297/

GitHub:
https://github.com/laxmisingh01

Instagram:
https://www.instagram.com/kindaa.lucky/

---

## 📜 License

This project is open source and available under the **MIT License**.

---

⭐ If you like this project, consider giving it a **star on GitHub**!
