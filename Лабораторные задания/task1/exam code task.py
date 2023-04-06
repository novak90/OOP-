import hashlib
from random import uniform, choice, randint
from faker import Faker
fake = Faker()


class IdCounter:
        def __init__(self):
            self._id = 0

        def get_id(self):
            self._id += 1
            return self.id

        @property
        def id(self):
            return self._id


class Password:


    def __init__(self, password):
        self.password = password

        if len(self.password) < 8:
            pass_len = len(self.password)
            print(
                f"Password needs to be at least 8 characters, current length: {pass_len}"
            )
            return
        alpha = False
        numeric = False
        for i in password:
            if i.isalpha():
                alpha = True

            if i.isdigit():
                numeric = True

        if not alpha or not numeric:
            print("Must container at least 1 number, and at least 1 letter")


    def get_hash(self):
        return hashlib.sha256(self.password.encode()).hexdigest()


    def check(self, password, hash):
        return hashlib.sha256(password.encode()).hexdigest() == hash


class Product:
    _id_counter = IdCounter()

    def __init__(self, name, price, rating):
        self._name = name
        self._id = self._id_counter.get_id()
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"Product({self._id}, {self._name}, {self.price}, {self.rating})"

    def __str__(self):
        return f'{self._id}_{self._name}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

class Cart:
    def __init__(self, cart=None):
        if not cart:
            cart = []
        if not isinstance(cart, list):
            raise TypeError("В корзине не список")
        self.cart = cart

    def get_cart(self):
        return self.cart

    def additem(self, product):
        self.cart.append(product)
        print("Товар был добавлен ".format(self))

    def removeitem(self, product):
        try:
            self.cart.remove(product)
            print("Товар был убран ".format(self))
        except:
            print("Извините, корзина уже пуста")


class User:
    def __init__(self, username, input_password):
        self._id_counter = IdCounter()
        self._user_cart = Cart()
        self._user_id = self._id_counter.get_id()
        self._username = self.valid_username(username)
        self.password = Password(input_password).get_hash()
        self._user_cart = Cart().get_cart()

    def __str__(self):
        return f"id: {self._user_id}, Логин: {self._username}"

    def __repr__(self):
        return f"User(id: {self._user_id}, Логин: {self._username}, Пароль: ********, Корзина: {self._user_cart})"

    @staticmethod
    def valid_username(username):
        for letter in username:
            if not letter.isalpha():
                TypeError("Имя должно состоять из букв")


class Goods_generator:
    _id_counter = IdCounter()
    def __iter__(self):
        return self

    def __next__(self):
        product = Product(''.join(fake.color_name()).title(),
                          str(round(uniform(1, 100), 2)) + '$',
                          round(uniform(0, 5), 2))
        return product



class paint_Store:
    _id_counter = IdCounter()

    def __init__ (self,input_username= None, input_password = None): \

        if input_username is not None:
            self._username = User(input_username, input_password).valid_username(input("Введите имя пользователя: "))
            self.password = Password(input_password).password.get_hash(input_password)
            del input_password
        self.cart = Cart().get_cart()

    def add_random(self, val=1):
        for n in range(val):
            prod = Product(''.join(fake.color_name()).title(), str(round(uniform(1, 100), 2)) + '$', round(uniform(0, 5), 2))
            self.cart.append(prod)



if __name__ == '__main__':
    product1 = Product(''.join(fake.color_name()).title(), str(randint(1, 100)) + '$', randint(1, 100))
    print(product1.__repr__())
    product2 = Product(''.join(fake.color_name()).title(), str(randint(1, 100)) + '$', randint(1, 100))
    print(product2.__repr__())
    product3 = Product(''.join(fake.color_name()).title(), str(randint(1, 100)) + '$', randint(1, 100))
    print(product3.__repr__())

    cart1 = Cart(['зеленый', 'черный', 'белый'])
    print(cart1.cart)
    cart1.additem("фиолетовый")
    print(cart1.cart)
    cart1.removeitem("белый")
    print(cart1.cart)

    user = User(str(fake.name()), '1234abcd')
    print(user.__repr__())

    store = paint_Store()
    store.add_random()
    print(store.cart)