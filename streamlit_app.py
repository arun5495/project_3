import streamlit as st

st.title("📁 Load Local Files")

# Example local paths (change these to match your own)
image_path = images.jpg
video_path = download.jpg
audio_path = "C:/Users/YourName/Music/my_song.mp3"

# Display image
st.subheader("🖼️ Image from Local Path")
st.image(image_path, caption="Local Image", use_column_width=True)

# Display video
st.subheader("🎥 Video from Local Path")
with open(video_path, "rb") as v:
    st.video(v.read())

# Display audio
st.subheader("🎵 Audio from Local Path")
with open(audio_path, "rb") as a:
    st.audio(a.read())
