import streamlit as st

st.title('Streamlit Usage')

st.header('In Mathematics')
st.subheader('Formula:')
formula='(a+b)2=a2+b2=2ab'
st.latex(formula)

st.header('In Programming')
st.subheader('Code Representation:')
code='''input=input('words:')
words=input.split(" ")
emoji_mapping={
:) : 😃,
:( : 😞}
for word in words:
  output+=emoji_mapping.get(word,word)
print(output)'''
st.code(code,language='python')
st.header('In Media')
st.subheader('Image:')
st.image('11020521.jpg',caption = "itachi",width=500)

st.subheader('Video:')
video=open('straw-hat-luffy.1920x1080.mp4','rb')
video_bytes=video.read()
st.video(video_bytes)

st.subheader('Audio:')
audio=open('Squid Game Season 2 Mingle Mp3','rb')
audio_bytes=audio.read()
