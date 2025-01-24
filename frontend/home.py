# Importing required libraries
import streamlit as st
# import streamlit_authenticator as stauth
from pathlib import Path
import pickle

import sys

sys.path.insert(1, "backend/example.py")



# User authentication
# names = ["Shravan Devraj", "Jason Xie"]
# usernames = ["sd", "tsuki"]

# file_path = Path(__file__).parent / "hashed_pass.pkl"
# with open(file_path, "rb") as file:
#     hashed_passwords = pickle.load(file)

# authenticator = stauth.Authenticate(
#     credentials={"names": names, "usernames": {"sd": "abc123", "tsuki": "abc123"}, "hashed_passwords": hashed_passwords},
#     cookie_name="LensCook",
#     key="abcdef"
# )

# name, authentication_status, username = authenticator.login("Login", "main")

# print(authentication_status)

# if authentication_status == False:
#     st.error("Username or Password is incorrect")
# if authentication_status == None:
#     st.error("Please enter Username and Password")
# if authentication_status:
#     pass

st.title("LensCook")

