from pwd_checker import pwd_strength # Import the password strength checker function

def main():
    """
    This function prompts the user for a password, validates input,
    checks its strength, and provides feedback.
    """

    print("""\nPASSWORD GUIDELINES:
    -> Length = Minimum 12 characters
    -> Should include upper and lower case letters, numbers and special characters
    -> Do not set a password already in use
    -> Do not include personal information such as name, date of birth, etc.

              """)
    
    while True:
        try:
            password = input("Enter your password: ") # Get user input for password

            if not isinstance(password, str): # Validate input: check if it's string
                raise ValueError("Invalid input. Please enter a string password.")
            
            score, feedback = pwd_strength(password) # Check password strength and get feedback

            if score >= 5:
                print(f"\n{feedback}\n\nYour are good to go!")
                break
            else:
                print(f"\n{feedback}")
            
            opt = input("Would you like to try a stronger password? (y/n): ") # Ask user if they want to try again

            if opt.lower() == "y":
                continue
            else:
                print("Exiting program...")
                break
        
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()