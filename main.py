import streamlit as st
from script.multipage import MultiPage
from script import homepage, Model1, Model2, Model3, Model4

@st.cache(allow_output_mutation=True)
def init():
    app = MultiPage()
    
    app.add_page("Homepage", homepage.app,"")
    app.add_page("Model1", Model1.app,"")
    app.add_page("Model2", Model2.app,"")
    app.add_page("Model3", Model3.app,"")
    app.add_page("Model4", Model4.app,"")

    return app

st.title("Webiste for metabolic syndrome prediction[test ver.]")

#mainPage = Page("Main", main)
#secondPage = Page("Second", main)

app = init()
app.run()

#main()

