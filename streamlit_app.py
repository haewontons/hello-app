import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(page_title= "Happy Bday Eve", page_icon=":tada:", layout='wide')


def load_lottieurl (url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
        return r.json()

lottie_coding = load_lottieurl ("https://lottie.host/cb6909b4-c58a-40b2-97c0-d1dc4fd85ebd/pXrGjcJKZD.json")




# HEADER section
with st.container():
    first_column, second_column = st.columns((3, 1))
    with first_column:
        st.title("HAPPY BIRTHDAY EVE!")
        st.subheader("An extension to your card...")
        st.write("Using my awesome computer science skills, I've built a small webpage to extend your birthday card coz u "
             "can't write shit on the small ass panels of the physical card haha. So yk how I was learning how to "
             "code on Python, I figured out how to like make it into a webpage.")
    with second_column:
        st_lottie(lottie_coding, height = 300)




# This is eve
with st.container():
    st.write("---")
    st.header("This is Eve Tse")

    first_column, second_column = st.columns((2, 1))
    with first_column:
        st.write("Eve Tse was born on the 17th of February 2008. Born on the year of the rat, and evidently"
                     "so, she's the sweetest little rodent of all the land <3. As an Aquarious, she certainly"
                     "upholds the clever, analytical, and problem solving traits of the (hot) Water Bearer"
                )
        st.write("Eve Tse is the most patient and tolerating individual one may ever cross paths with"
                 "in their life. There is none other who will bear to listen to all the same shit every"
                 "day about the same shitty situation Haewon's found herself in over some shitty person."
                 "")
        st.write("There is nobody else in the world who can spread good vibes quite like Eve does."
                 "The whole world turns to look when she laughs (coz she's usually laughing with Haewon and "
                 "Haewon always laughs so godamn loud). The whole world turns to look when she sneezes (coz"
                 "she sneezes so many fuckn times at once). But most importantly, the whole world turns to look"
                 "when they hear the 'THUCK THUCK THUCK' of the four legged creature hopping around the corner."
                 )


    with second_column:
        st.write('image')

#with st.container():
#    st.write("---")
 #   st.header("Question")
 #   st.subheader("[Question]")
 #   input = st.text_input("Ansewr below")
 #   if input == ('answer'):
  #      st.write(':green[Correct]')
#    elif input == (''):
 #       st.write('')
 #   else:
 #       st.write(':red[Incorrect]')
