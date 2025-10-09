import streamlit as st

# Set the app title
st.title("📸🎥🎵 File Uploader: Image, Video, and Audio")

st.write("Upload and preview your image, video, or audio files below 👇")

# --- Image Upload ---
st.subheader("flower")
image_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "gif"])

if image_file is not None:
    st.image(image_file, caption="Uploaded Image", use_column_width=True)

# --- Video Upload ---
st.subheader("🎥 Video Upload")
video_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi", "mkv"])

if video_file is not None:
    st.video(video_file)

# --- Audio Upload ---
st.subheader("🎵 Audio Upload")
audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "ogg"])

if audio_file is not None:
    st.audio(audio_file)

# --- Extra Info ---
st.write("---")
st.info("Tip: You can upload one file at a time in each section. Refresh the page to upload again.")
