import random

#Example One: Generate random floats
print("Random Floats")
print(random.random())
print(' ')

#Example Two: Generate random integers
print("Random Integers")
print(random.randint(1,100))
print(random.randint(1,100))
print('')

#Example Three: Generate random numbers within range
print("Random Range")
print(random.randrange(1,100))
print(random.randrange(1,10, 2))
print(random.randrange(0,101, 10))
print(' ')

#Example Four: Selecte random elements
print("Random Choice")
print(random.choice('computer'))
print(random.choice([12, 23, 45, 67, 65, 43]))
print(random.choice('12, 23, 45, 67, 65, 43'))
print(' ')

#Example Five: select random items from data set
print('select random items from data set')
print(random.sample([12, 23, 45, 67, 65, 43], 3))
print(' ')

#5.1 Select multiple itesm from a list without repetition
print('Select multiple items from a list without repetition')
aList =[20, 40, 80, 100, 120]
sample_list = random.sample(aList, 3)
print('aList random: ', sample_list)
print(' ')

#5.2 Generate the sampled list of random integers
print('Generate the sampled list of random integers')
num_list = random.sample(range(100), 5)
print(num_list)