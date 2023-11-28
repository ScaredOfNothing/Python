import hashlib
import getpass

# A dictionary to store usernames and their corresponding hashed passwords
UserDatabase = {}

def create_user_account():
    # Get a new username from the user
    new_username = input("Enter your desired username: ")
    
    # Get a new password securely from the user
    new_password = getpass.getpass("Enter your secure password: ")
    
    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
    
    # Store the username and hashed password in the user database
    UserDatabase[new_username] = hashed_password
    
    # Display a success message
    print("User account created successfully!")

def user_login():
    # Get the username from the user
    entered_username = input("Enter your username: ")
    
    # Get the password securely from the user
    entered_password = getpass.getpass("Enter your password: ")
    
    # Hash the entered password using SHA-256 algorithm
    hashed_entered_password = hashlib.sha256(entered_password.encode()).hexdigest()
    
    # Check if the entered username exists in the database and if the hashed password matches
    if entered_username in UserDatabase and UserDatabase[entered_username] == hashed_entered_password:
        print("Login successful! Welcome back,", entered_username + "!")
    else:
        print("Invalid username or password. Please try again.")

def main_program():
    # Main program loop
    while True:
        # Ask the user for their choice
        user_choice = input("Enter 1 to create a new user account, 2 to login, or 0 to exit: ")
        
        # Check the user's choice and call the appropriate function
        if user_choice == "1":
            create_user_account()
        elif user_choice == "2":
            user_login()
        elif user_choice == "0":
            # Exit the program
            break
        else:
            # Display an error message for an invalid choice
            print("Invalid choice! Please enter a valid option.")

# Ensure that the main_program function is called only if this script is run directly
if __name__ == "__main__":
    main_program()