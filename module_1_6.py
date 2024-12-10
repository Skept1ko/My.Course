my_dict = {"login": "Artem", "password": 12345678}

print(my_dict["login"])
print(my_dict.get("birth"))

my_dict.update({"birth": 2004, "height": 175})
print(my_dict)
x = my_dict.pop("login")
print(my_dict)
print(x)

my_set = {1, 2, 5.5, 1, 5.5}
print(my_set)
my_set.add(10)
print(my_set)
my_set.discard(1)
print(my_set)