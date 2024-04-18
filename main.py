
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import cohere
import streamlit as st

co = cohere.Client('k9fU42nP0rU1AYF2JDfoK2uWwIoGBrf70pJuZ3c9')
st.header('Emotion buddy')
st.text("Here to help solve your emotion problems!")

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    st.text("Clearing Ambient Sound")
    recognizer.adjust_for_ambient_noise(source, duration=10)
    st.text("Interview Started")
    recordedaudio=recognizer.listen(source)
    st.text('Finished!')
try:
    st.text("Determining Composite Interview Score")
    text1 = recognizer.recognize_google(recordedaudio, language='en-US')
    st.text('Your message:{}'.format(text1))
except Exception as ex:
    st.text(ex)
text1 = recognizer.recognize_google(recordedaudio, language='en-US')
Sentence = [text1]
analyser=SentimentIntensityAnalyzer()
for i in Sentence:
    v=analyser.polarity_scores(i)

st.text("Interview Composite Score:{}".format(v))
if v['compound'] == 0:
    user_question = "I am feeling neutral. give me quick advice."
elif v['compound'] > 0:
    user_question = "I am feeling happy. give me quick advice."
elif v['compound'] < 0:
    user_question = "I am feeling sad. give me quick advice."

if user_question:
    response = co.chat(
        model='command',
        message=user_question,
        max_tokens=300,
        temperature=0.7,
        k=0,
        conversation_id="user",
        prompt_truncation="AUTO"
    )

    st.write(response.text.strip("\n"))


