name = 'Bob'
greeting = f'Hello {name}'
print(greeting)

name = 'Justin'
print(greeting)
print(f'Hello {name}')

greeting = 'Hello, {}'
with_name = greeting.format('James')
print(with_name)
