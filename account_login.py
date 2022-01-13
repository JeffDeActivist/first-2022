
"""A code for a small online shop application we begin by asking the user to create an account with us"""
print("Welcome to the official site of Jeff Enterprises Limited")


def account_creation_login():
    your_name, phone_number, password = input('Enter your name, phone number and the password of a length not less '
                                              'than 8 characters\n').split(sep=',')
    conditions_account_creation = [your_name == password,
                                   len(password) < 8,
                                   password == '12345678',
                                   'abcd' or '0000' or '12' or '11' in password]
    if any(conditions_account_creation):
        raise Exception('password should not be same as your name amd should have a length of more than 8'
                        '\n abcd or 0000 or 12 should not be included in your password')
    print(your_name, 'you have successfully created your account with Jeff Enterprises Limited ')

    def login():
        name, password_ = input('Enter your name and password to login').split(sep=',')
        conditions_account_login = [name == your_name,
                                    password_ == password]
        if all(conditions_account_login):
            print(name, 'you have successfully logged in.\nYou can now check the available items')
        else:
            raise Exception('wrong details entered')

    login()


account_creation_login()
