import re

def evaluate_password(password: str) -> dict:

    if len(password) < 8:
        return {
            "status": "Invalid",
            "score": 0,
            "feedback": ["Password should contain at least 8 characters"]
        }

    score = 0
    feedback = []

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add number")

    if re.search(r"[!@#$%^&*()|<>,.?\":]", password):
        score += 1
    else:
        feedback.append("Add a special character")

    if len(password) >= 12:
        score += 1

    if re.search(r"(.)\1{2,}", password):
        score = max(0, score - 1)
        feedback.append("Do not use the same characters in a row")

    if score <= 2:
        status = "Weak"
    elif score <= 4:
        status = "Medium"
    else:
        status = "Strong"

    return {"status": status, "score": score, "feedback": feedback}


user_input = input("Enter the password: ")
result = evaluate_password(user_input)

print(f"Result: {result['status']} (Score: {result['score']}/5)")
if result['feedback']:
    print("Advices:" , ", ".join(result['feedback']))