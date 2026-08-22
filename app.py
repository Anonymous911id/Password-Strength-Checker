import re
import streamlit as st

def check_length(password: str) -> bool:
    return len(password) >= 8

def check_regex_patterns(password: str) -> dict:
    return {
        "has_upper": bool(re.search(r"[A-Z]", password)),
        "has_lower": bool(re.search(r"[a-z]", password)),
        "has_digits": bool(re.search(r"\d", password)),
        "has_special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

def check_repeated_chars(password: str) -> bool:
    return bool(re.search(r"(.)\1{2,}", password))

def check_weak_password(password: str, filename: str = 'weak_passwords.txt') -> bool:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if password == line.strip():
                    return True

        return False
    except FileNotFoundError:
        return False

def evaluate_password(password: str) -> dict:
    score = 0
    feedback = []

    if check_weak_password(password, 'weak_passwords.txt'):
        return {"status": "Weak",
                "score": 0,
                "feedback": ["This password is too common and easily guessable!"]}

    if check_length(password):
        score += 1
    else:
        feedback.append("Password should contain at least 8 characters")

    if len(password) >= 12:
        score += 1

    patterns = check_regex_patterns(password)
    for key, value in patterns.items():
        if value:
            score += 1
        else:
            if key == "has_upper": feedback.append("Add uppercase")
            if key == "has_lower": feedback.append("Add lowercase")
            if key == "has_digits": feedback.append("Add digits")
            if key == "has_special": feedback.append("Add special characters")

    if check_repeated_chars(password):
        score -= 1
        feedback.append("Do not use too many of same characters in a row")
    
    if score <= 2:
        status = "Weak"
    elif score <= 4:
        status = "Medium"
    else:
        status = "Strong"

    return {"status": status, "score": score, "feedback": feedback}


user_input = input("Enter the password: ")
result = evaluate_password(user_input)

print(f"Result: {result['status']} (Score: {result['score']}/6)")
if result['feedback']:
    print("Advices:" , ", ".join(result['feedback']))