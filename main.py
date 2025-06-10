import streamlit as st
from streamlit_option_menu import option_menu
st.title("Vinsup Infotech")
# with st.sidebar:
#     st.header("Internship")
# st.write("- Vinsup Infotech📈")
# st.text_input("Enter your Name:")
# st.button("Confirm")
with st.sidebar:
    data=option_menu(
        menu_title='Ranjani',
        options=["Education","City","Contact"],
        icons=["book","geo-alt","telephone"],
    )
if data=="Education":
    st.header("Registration page")
    
   
    col1,col2 = st.columns(2)
    with col1:
        name=st.text_input("Enter your name:")
        email=st.text_input("Enter your mail id:")
        city = st.selectbox("Select your city:", 
                        options=["Coimbatore", "Chennai", "Bangalore", "Hyderabad", "Mumbai", "Other"])
    with col2:
        contact_number=st.text_input("Enter your contact number:")
        gender=st.text_input("Enter your gender:")
        gender = st.radio("Select your gender:", options=["Male", "Female", "Other"])
    if st.button("Submit"):
        st.write(name,email,contact_number,city,gender)
    
elif data=="City":
    st.header("City page")
elif data=="Contact":
    st.header("Contact page")
    