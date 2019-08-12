my_variable = "hello"

grades = [32, 45, 56, 78, 90, 93] # list

tuples_grades = (32, )  # tuples

set_grades = {45, 45, 89, 23, 59}  # unique and unordered

grades.append(34)


# print(sum(grades) / len(grades))

# print(set_grades)

# print(grades)

set_one = {1, 2, 3, 4, 5}
set_two = {3, 4, 5, 5.0, 6}

print(set_one.intersection(set_two))
print(set_one.union(set_two))
print(set_one.difference(set_two))
