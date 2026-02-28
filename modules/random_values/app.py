import random

for i in range(3):
    print(random.random())

# random.ranint() method
for i in range(3):
    print(random.randint(10, 20))
  # This will generate int values

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)