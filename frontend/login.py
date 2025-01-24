# Import requires libraries
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
 
passwords = ["XXX", "XXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pass.pkl"
with open(file_path, "wb") as file:
    pickle.dump(hashed_passwords, file)
