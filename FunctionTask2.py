
import random

numbers = []

for count in range(10):
	numbers.append(random.randint(1,50))
	
print(numbers)



counter = 0

for counting in (numbers):
	counter += 1

print(counter)



even_sum = 0

for number in numbers:
	if number % 2 == 0:
		even_sum = even_sum + 1

print(even_sum)






numbers = list(range(1, 16))

print(numbers)



def add_every_third(numbers):
    
    total = 0
    
    for index in range(2, len(numbers), 3):
     total += numbers[index]

    return total

the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

result = add_every_third(the_list)

print(result)


