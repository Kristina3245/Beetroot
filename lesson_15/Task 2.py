class Dog:
    age_factor = 7

    def __init__(self):
        self.dog_age = int(input("Enter your dog's age: "))

    def human_age(self):
        human_age = self.dog_age * Dog.age_factor
        print(f"Human's age of your dog is: {human_age}")

dog = Dog()
dog.human_age()