import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('dt model.pkl','rb'))


def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Graduate Admission Predictor</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: Black;'>Drop in The required Inputs and we will do  the rest.</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: center; color: Black;'>Submission for The Python Week</h4>", unsafe_allow_html=True)
  st.sidebar.header("What is this Project about?")
  st.sidebar.text("It a Web app that would help the user in determining whether they will get admission in a Graduate Program or not.")
  st.sidebar.header("What tools where used to make this?")
  st.sidebar.text("The Model was made using a dataset from Kaggle along with using Kaggle notebooks to train the model. We made use of Sci-Kit learn in order to make our Linear Regression Model.")



  age = st.slider("Input Your AGE ",0.0,100.0)
  FQ1 = st.slider("Input your fq1",0.0,340.0)
  FQ2 = st.slider("Input your FQ2",0.0,120.0)
  FQ4 = st.slider("FQ4", 0.0,100.0)
  FQ33 = st.slider("FQ33", 0.0,100.0)
  FQ34 = st.slider("FQ34", 0.0,100.0)
  FQ37 = st.slider("FQ37", 0.0,100.0)

 

  inputs = [[age,FQ1,FQ2,FQ4,FQ33,FQ34,FQ37]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(float)
    st.success('Your average yearly amount spent {}'.format(updated_res))


if __name__ =='__main__':
  main()