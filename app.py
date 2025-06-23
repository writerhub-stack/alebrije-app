import streamlit as st
from alebrije_audio import analyze_audio
from generate_prompt import create_prompt

st.title("Alebrije Audio Visualizer 🎨")

audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if audio_file:
    with open("assets/uploaded_audio.wav", "wb") as f:
        f.write(audio_file.read())

    st.audio("assets/uploaded_audio.wav")

    st.write("Analyzing audio...")
    features = analyze_audio("assets/uploaded_audio.wav")
    st.json(features)

    st.write("Generating alebrije prompt...")
    prompt = create_prompt(features)
    st.success(prompt)