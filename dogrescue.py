# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:05:47 2026

@author: wamul
# CIS106 Final Project
# Dog Rescue Application

# Global list to store dogs
dogs = []
"""

# CIS106 Final Project
# Dog Rescue Application

# Global list to store dogs
dogs = []

# Main Function
 

def main():
    print("Welcome to the Dog Rescue Application!")
    menu()



# Menu Function
def menu():
    while True:
        print("\n------ Dog Rescue Menu ------")
        print("1. Add a Dog")
        print("2. View Dogs")
        print("3. Find Dog")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            addDog()
        elif choice == "2":
            viewDogs()
        elif choice == "3":
            findDog()
        elif choice == "4":
            print("Thank you for using the Dog Rescue Application!")
            break
        else:
            print("Invalid choice. Please try again.")



# Add Dog Function
def addDog():
    print("\n--- Add a Dog ---")

    name = input("Enter Dog Name: ")
    breed = input("Enter Dog Breed: ")
    age = input("Enter Dog Age: ")
    weight = input("Enter Dog Weight: ")

    # Store dog as a dictionary
    dog = {
        "Name": name,
        "Breed": breed,
        "Age": age,
        "Weight": weight
    }

    dogs.append(dog)
    print("Dog added successfully!")



# View Dogs Function

def viewDogs():
    print("\n--- View Dogs ---")

    if len(dogs) == 0:
        print("No dogs in the system.")
        return

    print("\n{:<15} {:<15} {:<10} {:<10}".format("Name", "Breed", "Age", "Weight"))
    print("-" * 50)

    for dog in dogs:
        print("{:<15} {:<15} {:<10} {:<10}".format(
            dog["Name"],
            dog["Breed"],
            dog["Age"],
            dog["Weight"]
        ))



# Find Dog Function

def findDog():
    print("\n--- Find Dog ---")

    search_name = input("Enter Dog Name to Search: ")

    found = False

    for dog in dogs:
        if dog["Name"].lower() == search_name.lower():
            print("\nDog Found!")
            print("Name:", dog["Name"])
            print("Breed:", dog["Breed"])
            print("Age:", dog["Age"])
            print("Weight:", dog["Weight"])
            found = True
            break

    if not found:
        print("Dog not found.")


# Run the program
main()
