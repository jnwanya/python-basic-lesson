my_list = [0, 1, 2, 3, 4, 5]
an_equal_list = [x for x in range(6)]
multiply_list = [x * 3 for x in range(6)]
print(multiply_list)
even_list = [n for n in range(20) if n % 2 == 0]
print(even_list)
names = ['John', ' James', 'TONY']
normalized_list = [name.strip().lower() for name in names];
print(normalized_list)
