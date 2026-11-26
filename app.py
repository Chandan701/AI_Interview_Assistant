import streamlit as st
from groq import Groq 

st.set_page_config(page_title='AI INTERVIEW ASSISTANT',page_icon='🎯',layout='centered')
st.title('🎯 AI INTERVIEW ASSISTANT')
st.caption('Pratice interviews with AI-generated questions and constructive feedback.')
st.caption('Founder and Launched by CHANDAN R')
st.write("DEPARTMENT OF ARTIFICAL AND DATA SCIENCE")

try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API Connection Successful")
except(keyError,FileNOTFOUNDError):
  st.error("GROQ_API_KEY is missing.Add it to Streamlit Cloud -> App setting secrets")
  st.stop()
