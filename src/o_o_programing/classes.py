# chapter 9
def sample():
    pass


class Dog:
    # state
    breed = ''
    age = ''
    name = ''
    color = ''

    # behavior
    # self keyword is used to show that functions and variables are belong to class
    def bark(self):
        print('Dog is barking')

    def run(self):
        name = self.name
        print(f'{self.name} is running fast .....')


# creating the object from the class(model)
# creating the instances from the class - INSTANTIATION

dog1 = Dog()
dog1.name = 'Roxi'

dog2 = Dog()
dog2.name = 'Flower'

dog3 = Dog()
dog3.name = 'Meli'

print("******Behaviour of the dog: dogs are running *******")
dog1.run()
dog2.run()
dog3.run()
