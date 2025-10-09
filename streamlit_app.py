!pip install streamlit
%%writefile app.py
import streamlit as st

st.title("welcome streamlit")
st.header("this is header")
st.subheader("this is subheader")
formula1 = ''' a+b '''
st.latex(formula1)
formula = ''' (a+b)2 =  a2+b2+2ab '''
st.latex(formula)
python_code = '''
     a = 9
     b=4
     c=78
     v = a+b+c
     print(v)

    '''
st.code(python_code, language='python')
st.header("Python")
st.caption("python is good lang ")
%%writefile app1.py
import streamlit as st
st.image('//content/[TCR] Attack On Titan S04 E14 (Tamil).mkv/While loop.PNG' ,caption = " loop function",width=500)
st.header("display flower video")
# loc =open("/content/flower_vid.mp4",'rb')
# vid_bytes = loc.read()
# st.video(vid_bytes)
# st.header("display flower auideo")
# loc =open("/content/flower_vid.mp4",'rb')
# vid_bytes = loc.read()
# st.audio(vid_bytes,format=audio/ogg)
