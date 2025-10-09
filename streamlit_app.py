import streamlit as st

st.title("📁 Load Local Files")

# Example local paths (change these to match your own)
image_path = images.jpg
video_path = download.jpg
audio_path =audio file

# Display image")
st.subheader("images.jpg")
st.image(image_path, caption="Local Image", use_column_width=True)

# Display video
st.subheader("download.jpg")
with open(video_path, "rb") as v:
    st.video(v.read())

# Display audio
st.subheader("audio file")
with open(audio_path, "rb") as a:
    st.audio(a.read())
