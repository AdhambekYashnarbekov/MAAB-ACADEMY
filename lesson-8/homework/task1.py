class Animal:
    def __init__(self, eating="Food", sleeping="Sleeping", moving="Moving", running="Running"):
        self.eating = eating
        self.sleeping = sleeping
        self.moving = moving
        self.running = running
    
    def eat(self):
        return "I am eating the food. Thank you!"
    
    def sleep(self):
        return "I am sleeping now. Get out!"
    
    def move(self):
        return "I am moving."
    
    def run(self):
        return "I am running."


class Dog(Animal):
    def __init__(self, sound="Wow-wow!"):
        super().__init__()  
        self.sound = sound  
    
    def make_sound(self):
        return self.sound


class Cat(Animal):
    def __init__(self, sound="Meow-meow!"):
        super().__init__()
        self.sound = sound
    
    def make_sound(self):
        return self.sound

class Chicken(Animal):
    def __init__(self, sound="Chip-chip!"):
        super().__init__()
        self.sound = sound
    
    def make_sound(self):
        return self.sound

class Bear(Animal):
    def __init__(self, sound="Rawr-rawr!"):
        super().__init__()
        self.sound = sound
    
    def make_sound(self):
        return self.sound


while True:
    choice = int(input("""Choose one of these animals:
    1. Dog
    2. Cat
    3. Chicken
    4. Bear
    5. Exit
    Enter your choice: """))

    if choice == 1:
        animal = Dog()
    elif choice == 2:
        animal = Cat()
    elif choice == 3:
        animal = Chicken()
    elif choice == 4:
        animal = Bear()
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
        continue

    print("\n--- Animal Actions ---")
    print(animal.eat())
    print(animal.sleep())
    print(animal.move())
    print(animal.run())
    print("Sound:", animal.make_sound())  
    print("\n")
