passwords = []
unlocked = False


class NewUser:
    def __init__(self,user_password):
        self.user_password = user_password

    def check_password_length(self):
        return len(self.user_password) < 8

    def check_password_spaces(self):
        for characters in self.user_password:
            if characters == " ":
                return True

    def check_password_isdigit(self):
        return self.user_password[0:1].isdigit()

    def verify_password(self):
        password_verify = input("To confirm the password please re-enter it: ")
        return password_verify == self.user_password

    def create_account(self):
        passwords.append(self.user_password)
        print("New user account created.")


def display_menu():
    while True:
        print("Please choose from:\n"
              "1. New User\n"
              "2. Existing User")
        user_choice = input("Please choose from the above options, 1 or 2: ")
        if user_choice not in ["1", "2"]:
            print("Input must be 1 or 2.")
        else:
            break
    return user_choice


def new_user():
    password = (input("Please enter the new password, it must be at least 8 characters long,\n"
                      "cannot contain any spaces and cannot begin with a number:"))
    new_password = NewUser(password)
    if new_password.check_password_length():
        print("Password length must be 8 or more characters.")
        new_user()
    elif new_password.check_password_isdigit():
        print("Password cannot begin with a number.")
        new_user()
    elif new_password.check_password_spaces():
        print("Password cannot contain spaces.")
        new_user()
    else:
        if new_password.verify_password():
            new_password.create_account()
        else:
            print("Passwords do not match.")
            new_user()


def existing_user():
    log_in_attempts = 3
    while log_in_attempts != 0:
        log_in_attempts -= 1
        existing_password = input("Please input your password to continue: ")
        if existing_password in passwords:
            return True
        else:
            if log_in_attempts > 0:
                print(f"Incorrect password, you have {log_in_attempts} attempts remaining.")
            else:
                break
    quit("Program ended. Incorrect password entered too many times.")


while not unlocked:
    if display_menu() == "1":
        new_user()
    else:
        if len(passwords) == 0:
            print("No accounts exist at the moment, you'll need to create one.")
            new_user()
        else:
            if existing_user():
                print("Access granted. Welcome!")
                break

