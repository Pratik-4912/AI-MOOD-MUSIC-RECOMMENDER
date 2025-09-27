import streamlit as st
import cv2
from deepface import DeepFace
from transformers import pipeline
from googleapiclient.discovery import build
import tempfile
import os

# ========== CONFIG ==========
YOUTUBE_API_KEY = ""  # Replace with your API key

# Initialize NLP model
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Function: Detect emotion from text
def detect_text_emotion(text):
    result = emotion_classifier(text)[0]
    return result['label']

# Function: Detect emotion from face
def detect_face_emotion(img_path):
    result = DeepFace.analyze(img_path, actions=['emotion'], enforce_detection=False)
    return result[0]['dominant_emotion']

# Function: Get YouTube songs
def get_youtube_recommendations(emotion):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    query = f"{emotion} mood songs"
    request = youtube.search().list(
        part="snippet", q=query, maxResults=5, type="video"
    )
    response = request.execute()
    videos = []
    for item in response['items']:
        title = item['snippet']['title']
        url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        videos.append((title, url))
    return videos

# Streamlit UI
st.set_page_config(page_title="AI Mood Music Recommender", page_icon="🎧", layout="wide")

st.title("🎧 AI Emotion-Based Music & Mood Recommender")
st.write("Detect your mood via **face** or **text**, and get music or quotes that match your emotion!")

# Input type selection
option = st.radio("Choose Input Type:", ["Text", "Webcam"])

if option == "Text":
    user_text = st.text_area("How do you feel today?")
    if st.button("Analyze Emotion"):
        if user_text.strip():
            emotion = detect_text_emotion(user_text)
            st.success(f"Your detected emotion: **{emotion}** 😄")
            
            # Show songs
            st.subheader("🎵 Recommended Songs:")
            videos = get_youtube_recommendations(emotion)
            for title, url in videos:
                st.markdown(f"- [{title}]({url})")
        else:
            st.warning("Please enter some text.")

elif option == "Webcam":
    st.write("Capture your emotion via webcam 📸")
    img_file = st.camera_input("Take a picture")
    if img_file is not None:
        # Save temp image
        temp = tempfile.NamedTemporaryFile(delete=False)
        temp.write(img_file.read())
        temp.close()
        
        # Detect emotion
        emotion = detect_face_emotion(temp.name)
        st.success(f"Detected Emotion: **{emotion}** 🧠")

        # Songs
        st.subheader("🎶 Recommended Songs:")
        videos = get_youtube_recommendations(emotion)
        for title, url in videos:
            st.markdown(f"- [{title}]({url})")

        os.remove(temp.name)
