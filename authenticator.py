import csv
import time
import os
from cryptography.fernet import Fernet

if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open("secret.key", "rb") as key_file:
    key = key_file.read()
    cipher_suite = Fernet(key)

os.system('cls' if os.name == 'nt' else 'clear')

user = input("Enter your username: ")
password =input("Enter your password: ") 
data = "user_password.csv" 
with open(data, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) < 2: continue 
        stored_user = row[0] 
        encrypted_password = row[1].encode()
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        if stored_user == user and decrypted_password == password:
            print("Authentication successful!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    else: 
        answer = input("This username and password is not correct do you want to create a new user or try again? (N=new user T=try again)")
        if answer.lower() == "n":
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            user = input("Enter your new username: ")
            password = input("Enter your new password: ")
            encrypted_pass = cipher_suite.encrypt(password.encode()).decode()
            with open(data, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([user, encrypted_pass])
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
            print("User created successfully!")
        elif answer.lower() == "t":
            print("Please try again.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            user = input("Enter your username: ")
            password = input("Enter your password: ")
            with open(data, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                     if row[0] == user and row[1] == password:
                        print("Authentication successful!")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                     else:
                        print("Authentication failed. Please try again. LAST CHANCE!")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        user = input("Enter your username: ")
                        password = input("Enter your password: ")
                        with open(data, "r") as file:
                            reader = csv.reader(file)
                            for row in reader:
                                if row[0] == user and row[1] == password:
                                     print("Authentication successful!")
                                     time.sleep(2)
                                     os.system('cls' if os.name == 'nt' else 'clear')
                                     break
                                else: 
                                    print("Account locked. Please try again later.")
                                    time.sleep(9999)
                                    
                        