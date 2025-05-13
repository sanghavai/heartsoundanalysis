import streamlit as st
import librosa
import numpy as np
import joblib

rf_model = joblib.load("smart_stethoscope_rf_model.pkl")

def extract_features(audio_file):
    audio, sr = librosa.load(audio_file, sr=None)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    return np.mean(mfcc, axis=1).reshape(1, -1)

st.title("Smart Stethoscope – AI for Heart Sound Analysis")
st.write("Upload a heartbeat audio file to check if it's Normal or Abnormal.")

uploaded_file = st.file_uploader("Upload WAV file", type=["wav"])

if uploaded_file is not None:
    features = extract_features(uploaded_file)
    prediction = rf_model.predict(features)[0]

    st.write("### Prediction:", "Normal" if prediction == 0 else "Abnormal")
