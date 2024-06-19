from pwd_checker import pwd_strength

def main():
    while True:
        print("""PASSWORD GUIDELINES:
              -> Length = Minimum 12 characters
              -> Should include upper and lower case letters, numbers and special characters
              -> Do not set a password already in use
              -> Do not include personal information such as name, date of birth, etc.
              
              """)

        password = input("Enter your password: ")
        score, feedback = pwd_strength(password)

        if score >= 5:
            print(f"Your are good to go!\n{feedback}")
            break
        else:
            print(f"Kindly try a stronger password.\n{feedback}")