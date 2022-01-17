class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        print (f"Hello, my name is {self.name}.")

    def say_age(self):
        print (f"I am {self.age} years old.")


class Superhero (Person):
    def __init__(self, name, age, occupation, secret_identity, nemesis):
        super ().__init__ (name, age, occupation)
        self.secret_identity = secret_identity

    def reveal_secret_identity(self):
        print (f"My real name is {self.secret_identity}.")

    def say_nemesis(self):
        print (f"My nemesis is {self.nemesis}.")

    def say_age(self):
        print (f'Young or old I will trimph over evil')

    #we have overridden say_age function of the parent.
    #we can restore it as shown below

    def old_say_hello(self):
        super ().say_hello ()





hero = Superhero ('Storm', 30, 'Queen of Wakanda', 'Oro Monroe', 'Shadow King')
hero.say_hello ()
hero.say_age ()
hero.old_say_hello ()