def pwd_strength(pwd):
    score = 0
    feedback = ""

    if len(pwd) >= 12:
        score += 1
    else:
        feedback += f"\n-> Password is short. ({len(pwd)} characters)."

    if any(char.isupper() for char in pwd):
        score += 1
    else:
        feedback += f"\n-> Missing uppercase letters."
    
    if any(char.islower() for char in pwd):
        score += 1
    else:
        feedback += f"\n-> Missing lowercase letters."
    
    if any(char.isdigit() for char in pwd):
        score += 1
    else:
        feedback += f"\n-> Missing numbers."
    
    symbols = "!@#$%^&*()-_+=|{[}]:;'<,>.?/"
    if any(char in symbols for char in pwd):
        score += 1
    else:
        feedback += f"\n-> Missing special characters or symbols."
    
    if score >= 5:
        strength = "Strong"
    elif score == 4:
        strength = "Medium"
    elif score == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return score, f"\nPassword Strength: {strength}{feedback}"