


class User:
    def __init__(self, name="No Name Provided", email="", password="1234abcd", account=0):
    #Define the attributes of the class
        self.name = name
        self.email = email
        self.password = password
        self.account = account

    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")

    # Adding r before ''' tells Python not to interpret backslashes as escape sequences
    notes = r'''
    !s — Calls str(value) to produce a human-readable string representation.
    !r — Calls repr(value) to produce an unambiguous/developer-friendly representation 
            (quoting strings and escaping special characters).
    !a — Calls ascii(value) to return a pure-ASCII string 
            using repr() escapes (\x, \u, \U) for non-ASCII characters.
    '''

    def __str__(self):
        return f"User(name={self.name!r}, email={self.email!r}, account={self.account})"
      
    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r}, account={self.account!r})"



#Outside of the class you would create an instance of the User class
new_user = User("John Doe", "johndoe@example.com",  "1234abcd", 1000)
print(f"Name: {new_user.name} | Account: {new_user.account}")
#Call the login method using the new object
#new_user.login()

