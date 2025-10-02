# Week 5 Assignment
# Author: Awwal fawas
# Description: Custom Class with Inheritance + Polymorphism Example


# -------------------------------
# Assignment 1: Superhero Class
# -------------------------------

# Parent Class
class Character:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        return f"I am {self.name}, my power is {self.power}!"


# Child Class (Superhero)
class Superhero(Character):
    def __init__(self, name, power, weapon):
        super().__init__(name, power)  # Call parent constructor
        self.weapon = weapon

    def attack(self):
        return f"{self.name} attacks with {self.weapon} using {self.power}!"


# Child Class (Villain)
class Villain(Character):
    def __init__(self, name, power, weakness):
        super().__init__(name, power)
        self.weakness = weakness

    def evil_plan(self):
        return f"{self.name} is plotting evil with {self.power}, but fears {self.weakness}!"


# Test Assignment 1
print("=== Assignment 1: Superhero Class ===")
hero = Superhero("Iron Man", "Tech Genius", "Suit")
villain = Villain("Thanos", "Infinity Gauntlet", "Teamwork")

print(hero.introduce())
print(hero.attack())
print(villain.introduce())
print(villain.evil_plan())


# -------------------------------
# Activity 2: Polymorphism Example
# -------------------------------

class Animal:
    def move(self):
        print("This animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("🐕 The dog runs on 4 legs!")

class Bird(Animal):
    def move(self):
        print("🐦 The bird flies in the sky!")

class Fish(Animal):
    def move(self):
        print("🐟 The fish swims in the water!")

print("\n=== Activity 2: Polymorphism ===")
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
