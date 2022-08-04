users_list = [
    {'first': 'Tre', 'last': 'Mays', 'email': 'tdog@hotmail.com'},
    {'first': 'Lucie', 'last': 'Chevreuil', 'email': 'lc@hotmail.com'},
    {'first': 'Nisrine', 'last': 'Kane', 'email': 'nk@gmail.com'},
    {'first': 'D', 'last': 34, 'email': 'hi mom'}
]

class User:

    users = []

    def __init__(self, user_dict) -> None:
        self.first = user_dict['first']
        self.last = user_dict['last']
        self.email = user_dict['email']
        User.users.append(self) 


    def login(self):
        print(f"welcome {self.first}")

    @classmethod
    def register(cls, the_list):
        for user_in_list in the_list:
            if not User.validate_user(user_in_list):
                print('sorry, invalid')
            else:
                cls.users.append(User(user_in_list))
    
    @staticmethod
    def validate_user(user:dict)-> bool:
        is_valid = True
        if len(user['first']) < 2:
            
            is_valid = False
        if len(user['last']) < 2:
            is_valid = False
        return is_valid


if not User.validate_user(users_list[-1]):
    print("Sorry, D! you need a longer name")    

user1 = User(users_list[-1])
user2 = User(users_list[1])

user_instances = User.register(users_list)