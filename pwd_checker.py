def pwd_strength(pwd):
    score = 0
    feedback = ""

    if len(pwd) >= 12:
        score += 1
    else:
        feedback += f"\n-> Password is short. ({len(pwd)} characters)."
    
    for char in pwd:
        if any(char.isupper()):
            score += 1
        else:
            feedback += f"\n-> Missing uppercase letters."
        
        if any(char.islower()):
            score += 1
        else:
            feedback += f"\n-> Missing lowercase letters."
        
        if any(char.isdigit()):
            score += 1
        else:
            feedback += f"\n-> Missing numbers."
        
        symbols = "!@#$%^&*()-_+=|{[}]:;'<,>.?/"
        if any(char in symbols):
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
    
    return score, f"Password Strength: {strength}\n{feedback}."