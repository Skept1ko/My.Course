immutable_var = 1, 2.0, "str", True, [10, 2.12, "int"]

print(immutable_var)
print(type(immutable_var))
print(immutable_var[1])
print(immutable_var[4][1])

# immutable_var[0] = 2 --> не изменяемая переменная
# print(immutable_var)

mutable_list = [1, "str", 2.5]

print(mutable_list)
mutable_list[1] = "int"
print(mutable_list)
