import streamlit as st
import random
import string

def genrate_password(length,use_digits,use_special_chars):  
    characters = string.ascii_letters

    if use_digits:        
        characters += string.digits     #adds no:1 ,2,3,4,5,6,7,8,9,0
    
    if use_special_chars:                       #add special characters !@#$%^&*()_+{}|:"<>?
        characters += string.punctuation

    return ''.join(random.choice(characters)for _ in range(length) )        #_ ki jaga i ya loop bi likh sakty hn# _ python ko batay ga k user/loop ki koi lenth malom ni

st.title("🔑Password Generator 📋")

length = st.slider("Select password Length",min_value=6,max_value=35,value=12)
use_digits = st.checkbox("Include digits 0-9")
use_special_chars= st.checkbox("Include special characters")


if st.button("Generate Password"):
    password = genrate_password(length,use_digits,use_special_chars)
    st.success(f"Generated Password: **'{password}'**")

st.write("--------------------------------------------------------------------")

st.write("👨‍💻 Build with 💖 by [Rabia Rehman](https://github.com/studentRabia?tab=repositories)")