import streamlit as st
import pickle

st.subheader('Iris Classification App')
sl=st.number_input('Enter sepal-length')
sw=st.number_input('Enter sepal-width')
pl=st.number_input(' Enter petal-length')
pw=st.number_input('Enter petal-width')
button=st.button('Predict')
if button:
   kn=pickle.load(open('iris.pkl','rb'))
   res=kn.predict([[sl,sw,pl,pw]])[0]
   st.markdown(f' The Species of the Flower is : {res}')