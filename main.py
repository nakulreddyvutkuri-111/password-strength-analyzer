import re

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


password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)
import random
import string

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("\nSuggested Strong Password:")
print(generate_strong_password())
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

hashed_password = hash_password(password)

print("\nEncrypted Password Hash:")
print(hashed_password)
# Check password reuse

try:
    with open("passwords.txt", "r") as file:
        old_passwords = file.read().splitlines()

    if hashed_password in old_passwords:
        print("\n⚠ Password already used before!")
    else:
        print("\n✅ New password detected.")

        with open("passwords.txt", "a") as file:
            file.write(hashed_password + "\n")

except FileNotFoundError:
    print("passwords.txt file not found.")