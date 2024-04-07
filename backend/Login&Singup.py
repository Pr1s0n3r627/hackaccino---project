#Importing
import csv

class UserAuthenticator:
    def __init__(self, file_path):
        self.file_path = file_path

    def register_user(self, username, password):
        """
        Register a new user by adding their credentials to the CSV file.
        
        Parameters:
        username (str): The username of the new user.
        password (str): The password of the new user.
        """
        with open(self.file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

    def authenticate_user(self, username, password):
        """
        Authenticate a user by checking their credentials against the stored data in the CSV file.
        
        Parameters:
        username (str): The username of the user.
        password (str): The password of the user.
        
        Returns:
        bool: True if authentication is successful, False otherwise.
        """
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
        return False

def main():
    """
    Main function to demonstrate the usage of UserAuthenticator for user registration and authentication.
    """
    file_path = 'user_credentials.csv'  # Replace with the path to your CSV file
    authenticator = UserAuthenticator(file_path)

    while True:
        choice = input("Enter '1' to register, '2' to login, or 'q' to quit: ")
        
        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            authenticator.register_user(username, password)
            print("User registered successfully!")
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authenticator.authenticate_user(username, password):
                print("Login successful!")
            else:
                print("Invalid username or password. Please try again.")
        elif choice.lower() == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
