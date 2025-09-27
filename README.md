# 🎧 AI Emotion-Based Music & Mood Recommender

**Detect your mood and get personalized music recommendations!**

This AI-powered web app detects your current emotion through **text input** or **webcam facial expression** and recommends **YouTube songs** that match your mood. It combines **Computer Vision**, **NLP**, and **API integration** to create a fun, interactive, and engaging experience.

---

## 🌟 Features

* Detect emotions from **text** using a pre-trained NLP model.
* Detect facial emotions from a **webcam image** using **DeepFace**.
* Recommend **YouTube songs** matching your mood.
* Real-time feedback with **spinner indicators** to improve user experience.
* Works entirely with **free tools and APIs**.

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **Face Emotion Detection:** DeepFace + OpenCV
* **Text Emotion Detection:** HuggingFace Transformers (`distilbert-base-uncased-emotion`)
* **Music Recommendations:** YouTube Data API v3
* **Backend:** Python
* **Database:** Optional (can be added with Supabase for mood logs)

---

## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/AI-Emotion-Music-Recommender.git
cd AI-Emotion-Music-Recommender
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your **YouTube API Key** in `app.py`:

```python
YOUTUBE_API_KEY = "YOUR_API_KEY_HERE"
```

4. Run the Streamlit app:

```bash
python -m streamlit run app.py
```

5. Open your browser and start detecting moods & enjoying music! 🎶

---

## 💡 Future Enhancements

* Motivational quotes for each detected emotion.
* Real-time mood tracking and emoji dashboard.
* User mood logs stored in a cloud database (Supabase).
* Multi-language support (Hindi/Marathi).

---

