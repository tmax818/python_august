

users_list = [
    {'first': 'Tre', 'last': 'Mays', 'email': 'tdog@hotmail.com'},
    {'first': 'Lucie', 'last': 'Chevreuil', 'email': 'lc@hotmail.com'},
    {'first': 'Nisrine', 'last': 'Kane', 'email': 'nk@gmail.com'},


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
            cls.users.append(User(user_in_list))

user1 = User(users_list)
user2 = User(users_list[1])

user_instances = User.register(users_list)