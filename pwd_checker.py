def pwd_strength(pwd):
    """
    This function analyzes the strength of a password based on various criteria.
    
    Args:
        pwd (str): The password string to be evaluated.
    
    Returns:
        tuple: A tuple containing the password score (int) and a strength message (str).
  """
    
    score = 0
    feedback = ""

    if len(pwd) >= 12: # Check password length
        score += 1
    else:
        feedback += f"\n-> Password is short. ({len(pwd)} characters)."

    if any(char.isupper() for char in pwd): # Check password for uppercase letters
        score += 1
    else:
        feedback += f"\n-> Missing uppercase letters."
    
    if any(char.islower() for char in pwd): # Check password for lowercase letters
        score += 1
    else:
        feedback += f"\n-> Missing lowercase letters."
    
    if any(char.isdigit() for char in pwd): # Check for numbers
        score += 1
    else:
        feedback += f"\n-> Missing numbers."
    
    symbols = "!@#$%^&*()-_+=|{[}]:;'<,>.?/"
    if any(char in symbols for char in pwd): # Check for special characters
        score += 1
    else:
        feedback += f"\n-> Missing special characters."
    
    # Determine password strength based on score
    if score >= 5:
        strength = "Strong"
    elif score == 4:
        strength = "Medium"
    elif score == 3:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return score, f"\nPassword Strength: {strength}{feedback}"