class Test():
    def public_func(self):
        print('Публичная функция')

    def _protected_func(self):
        print('Защищенная функция')

    def __private_func(self):
        print('Приватная функция')

    def test_private(self):
        self.__private_func()

test = Test()
test.public_func()
test._protected_func()
test.test_private()