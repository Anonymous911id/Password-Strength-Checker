# Password strength checker

A Python tool built with Streamlit to evaluate password strength using Regex and common cidtionary check with a clean web interface

## Features
- **Interactive Web UI:** Clean, user-friendly interface powered by Streamlit
- **Length & Character Validation:** Checks for uppercase, lowercase, digits, and symbols
- **Repetition Detection:** Identifies and warns against repeated characters
- **Common Password Lookup:** Compares inputs against a `weak_passwords.txt` dictionary
- **Real-time Feedback:** Provides a security score (Weak, Medium, Strong) and actionable improvement suggestions

## Prerequisites
- Python 3.x
- Streamlit library

## Installation & Setup
1. Clone or download this repository.
2. Ensure `weak_passwords.txt` is in the same folder.
3. Install the required dependency:
   ```bash
   pip install streamlit

## Usage
Run the Streamlit application using the command below:

```bash
streamlit run app.py
```
(Or use python -m streamlit run app.py if the command is not recognized in your environment)