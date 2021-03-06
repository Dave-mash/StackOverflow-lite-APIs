import re

# data = {
#     'username': 'Dave',
#     'email': 'dave@email.com',
#     'password': 'asdk',
#     'confirm_password': 'asdk'
# }

class RegistrationForm:
    
    def __init__(self, Fname, Lname, username, email, password, confirm_password):
        self.Fname = Fname
        self.Lname = Lname
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
    
    def data_exists(self):
        if not self.username or not self.Fname or not self.Lname or not self.email or not self.password or not self.confirm_password:
            return False
        else:
            return True

    def valid_name(self):
        if len(self.username) < 3 or len(self.username) > 20:
            return False
        else:
            return True

    @classmethod
    def valid_email(cls, email):
        cls.email = email
        regex = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        
        if not re.match(regex, cls.email):
            return False
        else:
            return True

    @classmethod
    def valid_password(cls, password):
        cls.password = password
        regex = re.compile(r'[a-zA-Z0-9@_+-.]{3,}$')
        # regex = re.compile(r'^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z](?=.*?[^A-Za-z\s0-9]))')

        if not re.match(regex, cls.password):
            return False
        else:
            return True

    def valid_confirm_password(self):
        if self.password != self.confirm_password:
            return False
        else:
            return True
   

class LoginForm(RegistrationForm):

    def __init__(self, email, password, questions=[]):
        self.email = email
        self.password = password
        self.questions = questions

    def get_questions(self, question):
        que = Questions(self.email, self.questions)
        self.questions.append(que)

class Questions(LoginForm):

    def __init(self, email, title, question):
        self.title = title
        self.email = email
        self.question = question

# user = LoginForm(
#     data['email'],
#     data['password']
# )

# user = RegistrationForm(
#     data['username'],
#     data['email'],
#     data['password'],
#     data['confirm_password']
# )

# user.valid_password(data['password'])
# user.valid_email(data['email'])
# user.valid_confirm_password()
# user.valid_username()