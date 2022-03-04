import streamlit as st

st.title('ML sydrome prediction')

with st.form(key='Model_form'):
    c11, c12 = st.columns(2)
    name = c11.text_input("Enter a name:")
    surname = c12.text_input("Enter a surname")
    c21, c22 = st.columns((1, 1))
    is_middlename = c21.checkbox("Do you have middlename")
    if (is_middlename):
        middlename = c22.text_input("Enter your middlename")
    else:
        middlename = ''
    c31, c32 = st.columns((1, 2))
    age = c31.number_input('Enter a age:')
    DOB = c32.date_input('Date of birth:')
    c41, c42 = st.columns(2)
    weight = st.number_input('Enter a weight(kg):', value=0)
    height = st.number_input('Enter a height(cm):', value=120)
    submitted = st.form_submit_button('Submit')

def model(**arg):
    return 0

if (submitted):
    res = model()
    st.write("Prediction is {}".format(res))
