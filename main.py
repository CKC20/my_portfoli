import streamlit as st 
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
# lottie_coder="https://lottiefiles.com/animations/coder-jAUpeq1je0"
st.set_page_config(layout="wide")
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
# lottie_coder=load_lottieurl("https://lottie.host/ae444b9e-f5ab-4f2c-9cf1-5cd1b90b9957/egkv5J0Ydr.json")
lottie_coder1=load_lottieurl("https://lottie.host/413799f0-1288-4407-b135-94aa680b719a/rJ53xdG4bf.json")  
lottie_coder2=load_lottieurl("https://lottie.host/d14edd5a-2b67-42e3-92fa-bbb2b25f12e9/pAlCDKyaWb.json")
lottie_coder3=load_lottieurl("https://lottie.host/e4298faf-9908-4b45-b2d6-396355d0db49/gmpb26VNQw.json")
lottie_coder4=load_lottieurl("https://lottie.host/b7037cab-7c81-400c-8ab7-c8ed46fb70ab/GsIIYr5h3R.json")
lottie_coder5=load_lottieurl("https://lottie.host/380b66de-cb14-4a3a-b36c-ed6ba96def87/xbWsjkK838.json")
lottie_coder6=load_lottieurl("https://lottie.host/bb5c2ae5-6b65-4ff0-b587-4d5838685ee9/JN0KgTb6CV.json")
lottie_coder7=load_lottieurl("https://lottie.host/118f49eb-e32d-4221-abbc-457241b016ea/IJoiYvENBm.json")
lottie_coder=load_lottieurl("https://lottie.host/501b5575-c70c-41e1-82b4-cbc2371d15c9/pgtiHhNvgv.json")# FOR NAMASTE 
lottie_coder8=load_lottieurl("https://lottie.host/7e4d86b5-6353-4b2e-87e3-e12b6df6b226/SrSC6RGViM.json")
lottie_coder_phn=load_lottieurl("https://lottie.host/2efaf6d7-bb32-4110-9a25-2ee75ab75eb9/2Gasar5Z8K.json")
lottie_coder9=load_lottieurl("https://lottie.host/4b56c921-2654-40ef-a04d-cd53a6847fe5/dkbvLdQlWi.json")
lottie_coder_link=load_lottieurl("https://lottie.host/83b64c84-9cb7-49ea-badc-9e7f968e72f7/IjANr1ULrs.json")
st.write("##")
# with st.container():
#     col_x,col_y=st.columns(2)
#     with col_x:
#          st.subheader("hey guys:wave:")#,divider='rainbow')
#     with col_y:
#         st_lottie(lottie_coder,height=300,width=300)
st.subheader("hey guys :red[NAMASTE]:wave:",divider='rainbow')
st.title("welcome to My Porfolio website")
st.subheader("          ",divider='rainbow')
st.balloons()

with st.container():
    selected = option_menu(
        menu_title = None,
        options=['About','Education','Projects','Contact'],
        icons=['person','book','code-slash','chat-left-text-fill'],
        orientation='horizontal'
    )
if selected =='About':

    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.write("##")
            st.title("I am :orange[Charchit Kumar Chauhan]")
            st.subheader(" Completed Btech  in  :red[ Computer Science   ]:blue[  from Kiet Group Of Institution Ghaziabad] ")
            
        with col2:
            st_lottie(lottie_coder1)
if selected=='Education':
    with st.container():
        col3,col4,col5=st.columns(3)
        with col3:
            st_lottie(lottie_coder3,height=140,width=160)

            st.subheader("Kiet Group Of Institution Ghazibad",divider='rainbow')
            st.write("   ")
            st.subheader("Priyanka Modern Sr Sec School Dhampur",divider='rainbow')
            st.write("   ")
            st.subheader("Priyanka Modern Sr Sec School Dhampur",divider='rainbow')
            st.write("   ")
        with col4:
            st_lottie(lottie_coder4,height=140,width=150)

            st.write("   ")
            st.write("    ")
            st.subheader("                 :red[Computer Science Engineering]",divider='rainbow')
            st.write("    ")
            st.write("    ")
            st.write("    ")
            st.subheader(":red[Senior Secondary]",divider='rainbow')
            st.write("    ")
            st.write("    ")
            st.write("    ")
            st.subheader(":red[High School]",divider='rainbow')

        with col5:
            st_lottie(lottie_coder5,height=140,width=150)
            st.write("    ")
            st.write("    ") 
            st.subheader(":blue[8.6  C.G.P.A]",divider='rainbow') 
            st.write("    ")
            st.write("    ")
            st.write("    ")
            st.subheader(":blue[77% Percentage]",divider='rainbow')
            st.write("    ")
            st.write("    ")
            st.write("    ")
            st.subheader(":blue[77.7% Percentage]",divider='rainbow')
if selected=='Projects':
    st.subheader(":orange[Here are my Projects]:books:",divider='rainbow')
    col7,col8=st.columns(2)
    with col7:
        st.subheader(':red[Predicting Box Office Revenue]')
        st.write("_____")
        st.write('• Implement a model to predict how much revenue a movie makes at box office.')
        st.write('• Technology used: Machine Learning, EDA Analysis, Feature Engineering.')
        st.subheader(':red[Movie Sentiment Analysis]')
        st.write('•Developed a model to make sentiment analysis regarding a movie. Model is trained on the basis Of the review of the movie. Review is between 0-5 which is based on the rating from the audience')
        st.write('•Technology used: NLP, Plotly (graph) ,Word Cloud(For reviews),Confusion Matrix')
        
    with col8:
        st_lottie(lottie_coder6,height=250,width=300)
        st_lottie(lottie_coder7,height=250,width=300)

if selected=="Contact":
    st_lottie(lottie_coder8,height=100,width=500)
    col_x,col_y=st.columns(2)
    with col_x:
        st.subheader(":red[CONTACT NO ---]:blue[7037904818]")
        st.subheader("    ",divider='rainbow')
        
        st.subheader(":red[LINKDLN PROFILE]")
        link_text = "Click to open my linkdin profile"
        link_url = "https://www.linkedin.com/in/charchit-kumar-chauhan-280a02207/"
        markdown_string = f"[{link_text}]({link_url})"
        st.markdown(markdown_string, unsafe_allow_html=True)
        st.subheader("    ",divider='rainbow')
        st.subheader(":red[EMAIL-ID]")
        link_text = "Click to open my Email-Id"
        link_url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"
        markdown_string = f"[{link_text}]({link_url})"
        st.markdown(markdown_string, unsafe_allow_html=True)
        st.subheader("    ",divider='rainbow')
    with col_y:
        st_lottie(lottie_coder_phn,height=100,width=300)
        st_lottie(lottie_coder_link,height=100,width=300)
        st_lottie(lottie_coder9,height=100,width=300)
        


    
     
        

        
        


            




    

