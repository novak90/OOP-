import hashlib


class IdCounter():
    id = 1

    def __init__(self):
        self.id = IdCounter.id
        IdCounter.id += 1

    def __int__(self):
        return IdCounter.id


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

        if alpha and numeric:
            pass
        else:
            print("Must container at least 1 number, and at least 1 letter")

    def get(self):
        return hashlib.sha256(self.password.encode()).hexdigest()

    def check(self, password, hash):
        return hashlib.sha256(password.encode()).hexdigest() == hash


class Product():

    def __init__(self, name, price, rating=0):

        if name:
            self.__name = name
        else:
            raise ValueError

        if price:
            if isinstance(price, int):
                self.price = price
            else:
                raise TypeError

        else:
            raise ValueError

        if isinstance(rating, int):
            self.rating = rating
        else:
            raise TypeError

        self.__id = IdCounter().id

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return (f"{self.id}_{self.name}")

    def __repr__(self):
        return (f"{self.id}_{self.name}")


class Cart():
    print("not implemented")


class User():
    print("not implemented")


class Store():
    print("not implemented")


if __name__ == '__main__':
    p = Product(name='Toaster', price=200)
    z = Product(name='Toasterz', price=200)
    print(z)