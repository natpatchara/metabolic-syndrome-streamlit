#Model 1 pure physical examination
import streamlit as st

def app(model):
    st.title('ML sydrome prediction(model1)')

    with st.form(key='Model_form'):
        c11, c12 = st.columns(2)
        age = c11.number_input('Enter a age:')
        wc = c12.number_input("Enter a weaist circumference")
        c21, c22 = st.columns((1, 2))
        weight = c21.number_input('Enter a weight(kg):', value=0)
        height = c22.number_input('Enter a height(cm):',value=120)
        c31, c32 = st.columns((1, 1))
        is_BMI = c31.checkbox("Do you have calculated BMI")
        bmi = c32.number_input("Enter your bmi:")
        if (is_BMI):
            pass
        else:
            bmi = weight / (height / 100) / (height / 100)
        c41, c42 = st.columns((1, 2))
        sbp = c41.number_input('Enter a systolic blood pressure:')
        dbp = c42.number_input('Enter a diastolic blood pressure:')
        submitted = st.form_submit_button('Submit')

    def model(**arg):
        return 0


    if (submitted):
        #res = model()
        st.write("Your input")
        st.write("Age: {}".format(age))
        st.write("Waist circumference: {}".format(wc))
        st.write("BMI: {}".format(bmi))
        st.write("DBP: {}".format(dbp))
        st.write("SBP: {}".format(sbp))
