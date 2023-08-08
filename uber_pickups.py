from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
#from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    #with open
local_css("style/style.css")


#  ---- LOAD ASSETS ------ #

lottie_coding = load_lottieurl("https://lottie.host/310cd599-02ae-495e-a006-1ec8ca970d6d/C81gFsNplj.json")
img_contact_from = Image.open("images/1.png")
img_lottie_animation = Image.open("images/2.png")



# -----   HEADER SECTİON  ----- #
with st.container():
    st.subheader("Hi, I am Mehmet :wave: ")
    st.title("A Junior Software Developer From Turkey")
    st.write("I am passionate about finding ways to use python and VBA to be more efficient and effective in business settings.")
    st.write("[Learn More>](https://github.com/memetolmaz)")


#  ----  WHAT I DO IN REAL TIME ------- #
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            
            On my Website I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses
            - are working with Excel and found themselves thinking - " there has to be a better way"
            
            If this sounds interesting to you , consider following and turning on the notifications , so you don't miss any content.
            
            """
        )
        st.write("[My Linkedin Profile >](https://www.linkedin.com/in/memet-olmaz/)")
    with right_column:
        st_lottie(lottie_coding,height=500, key="coding")

# ----- PROJECTS ---- ### 

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column , text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    
    with text_column:
        st.subheader("Car Rental Automation With C# and MsSqL Server")
        st.write(
            """

            Learn how to use otomation systems in C#
            Working with database at the same time is more effective way to develop your programming skills
            You can review whole codes in my github. I'll put the link below. Enjoy !!!


            """
        )
        st.markdown("[Take a look the whole codes](https://github.com/memetolmaz/Car-Otomation-)")
with st.container():
    image_column , text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_from)
    with text_column:
        st.subheader("How to do a good Admin Panel  in C#")
        st.write(
            """
            Want to add Admin Panel in your project with database connection ? 
            In this project , you can find everything you need. Just take a look...
            """
        )

# ----- CONTACT ------- ## 
with st.container():
    st.write("---")
    st.header("Get In Touch With Me !")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/olmazmehmet7@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false"> 
        <input type="text" name="name" placeholder="Your Name" requried>
        <input type="email" name="email" placeholder="Your email " required>
        <textarea name="message" placeholder="Your message here" requried></textarea>
        <button type="submit">Send</button>
    </form>

"""
    left_column , right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()


#with st.sidebar:
#    selected = option_menu(
#        menu_title = None,
#        options =["Home","Projects","Contact"],
#    
#if selected == "Home":
#    st.title(f"You have selected {selected}")
#if selected == "Projects":
#    st.title(f"You have selected {selected}")
#if selected == "Contact":
#    st.title(f"You have selected {selected}")

