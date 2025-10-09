import streamlit as st

st.title('Streamlit Usage✨')
st.code(code,language='python')
st.header('In Media💿')
st.subheader('📸Image:')
st.image('11020521.jpg',caption = " itachi",width=700)

st.subheader('🎞Video:')
video=open('naruto.1920x1080.mp4','rb')
video_bytes=video.read()
st.video(video_bytes)

st.subheader('🎧Audio:')
audio=open('Squid Game Season 2 Mingle Mp3','rb')
audio_bytes=audio.read()
st.audio(audio_bytes)
