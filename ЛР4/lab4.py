# Вихляев Егор, ММТ-2

# Exercise 1


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, name, age):
        self.children.append(Child(name, age))

    def print_info(self):
        print(f"Parent: {self.name}, {self.age} years old")
        if self.children:
            print("Children:")
            for child in self.children:
                print(f"- {child.name}, {child.age} years old")
        else:
            print("No children")

    def calm_child(self, child_num):
        self.children[child_num].calm()

    def feed_child(self, child_num):
        self.children[child_num].feed()


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_calm = True
        self.is_fed = True

    def calm(self):
        self.is_calm = True
        print(f"{self.name} calmed down")

    def feed(self):
        self.is_fed = True
        print(f"{self.name} was fed")


parents = []
for i in range(int(input("Enter number of parents: "))):
    name = input(f"Enter name for parent {i+1}: ")
    age = int(input(f"Enter age for parent {i+1}: "))
    parent = Parent(name, age)

    num_children = int(input(f"Enter number of children for {name}: "))
    for j in range(num_children):
        child_name = input(f"Enter name for child {j+1}: ")
        child_age = int(input(f"Enter age for child {j+1}: "))
        parent.add_child(child_name, child_age)

    parents.append(parent)

while True:
    print("\nMenu:")
    print("1. Print parent info")
    print("2. Print children info")
    print("3. Take action on child")
    print("4. Quit")

    option = input("\nChoose option: ")

    if option == "1":
        parent_num = int(input("Enter parent number: "))
        parents[parent_num - 1].print_info()

    elif option == "2":
        parent_num = int(input("Enter parent number: "))
        print("\nChildren:")
        for i, child in enumerate(parents[parent_num - 1].children):
            print(f"{i+1}. {child.name}, {child.age}")

    elif option == "3":
        parent_num = int(input("Enter parent number: "))
        child_num = int(input("Enter child number: "))
        child = parents[parent_num - 1].children[child_num - 1]

        print("\nChoose action:")
        print("1. Calm child")
        print("2. Feed child")
        action = input("Action: ")

        if action == "1":
            parents[parent_num - 1].calm_child(child_num - 1)
        elif action == "2":
            parents[parent_num - 1].feed_child(child_num - 1)

    elif option == "4":
        break
