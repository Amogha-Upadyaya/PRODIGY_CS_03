from pwd_checker import pwd_strength

def main():
    print("""\nPASSWORD GUIDELINES:
    -> Length = Minimum 12 characters
    -> Should include upper and lower case letters, numbers and special characters
    -> Do not set a password already in use
    -> Do not include personal information such as name, date of birth, etc.

              """)
    
    while True:
        password = input("Enter your password: ")
        score, feedback = pwd_strength(password)

        if score >= 5:
            print(f"{feedback}\n\nYour are good to go!")
            break
        else:
            print(f"{feedback}\n\nKindly try a stronger password.")

if __name__ == "__main__":
    main()