#lists - collection of items
names = ['Harry', 'Evelyn']
names.append('Emily')
# print(names)
# print(names[0])

#arrays - must be numerical data types, all items must be the same data type
from array import array
scores = array("d")
scores.append(97)
scores.append(98)
# print(scores)

#common operations
#length
# print(len(names))
#insert - index before the one specified
names.insert(0, 'Chris')
names.sort()
# print(names)
#ranges - all the way up to but not including
kids = names[2:4]
# print(kids)

#Dictionaries - key-value pairs
person = {'first': 'Emily'}
person['last'] = 'Lubkert'
# print(person)
# print(person['first'])

#loops
for name in names:
    print(name)

for num in range(0, 10):
    print(num)

index = 0

while index < len(names):
    print(names[index])
    #change the condition
    index = index + 1