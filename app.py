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
  st.error('GROQ_API_KEY is missing.Add it to Streamlit Cloud -> App setting secrets')
  st.stop()
import streamlit as st 
from groq import Groq

client = Groq (api_key = st.secrets["GROQ_API_KEY"])

st.title("AI Interview Assistant")

role=st.selectbox("Select Job Role",[
  "Python Developer",
  "Java Developer",
  "Machine Learning Engineer",
  "Software Engineer",
  "HR Executive"
])
if st.button("Generate Interview Questions"):
  prompt = "Generate 5 interview questions for the role of " +role

  response = client.chat.completions.create(
    model = "openai/gpt-oss-120b",
    messages=[
      {"role":"system","content":"You are an expert technical Interview"},
      {"role":"user","content":prompt}
    ]
  )
  output = response.choices[0].message.content
  st.write(output)
