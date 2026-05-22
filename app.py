import streamlit as st
import re
import random
import string
import hashlib

st.title("🔐 Password Strength Analyzer")

password = st.text_input("Enter Your Password", type="password")

def check_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add special characters.")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, remarks

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

if password:

    strength, feedback = check_password_strength(password)

    st.subheader(f"Password Strength: {strength}")

    if strength == "Strong":
        st.success("Excellent Password ✅")
        st.progress(100)

    elif strength == "Medium":
        st.warning("Moderate Password ⚠")
        st.progress(60)

    else:
        st.error("Weak Password ❌")
        st.progress(30)

    if feedback:
        st.write("### Suggestions")
        for item in feedback:
            st.write("- ", item)

st.write("### Suggested Strong Password")

generated_password = generate_strong_password()

st.code(generated_password)

st.text_input("Copy Your Password", generated_password)