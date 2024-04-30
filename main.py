class User():
    def __init__(self, user_id, name):
        self.__id = user_id
        self.__name = name
        self.__access = 'user'

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_access(self):
        return self.__access

    def set_name(self, name):
        self.__name = name

    def set_access(self, access):
        self.__access = access

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._User__access = 'admin'
        self.user_list = []

    def add_user(self, user):
        self.user_list.append(user)

    def remove_user(self, user_id):
        for user in self.user_list:
            if user.get_id() == user_id:
                self.user_list.remove(user)
                break

admin = Admin('000001', "Admin User")
user1 = User('002234', "Иванов Алексей")
user2 = User('002523', "Звягинцева Ксения")
user3 = User('005773', "Кривоногов Василий")
user4 = User('002230', "Жилина Анна")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)

for user in admin.user_list:
    print(user.get_id(), user.get_name())

admin.remove_user('002523')

for user in admin.user_list:
    print(user.get_id(), user.get_name())


