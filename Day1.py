# Using the range() Function
for i in range( 16):
    print(i)
# Using range() to make list of numbers
numbers=list(range(1,21,3))
print(numbers)

# print  first 10 sqaure no in a list
squares=[]
for i in range(1,11):
    # square = i**2
    squares.append(i**2)
print(squares)

ls=[i**3 for i in range(1,11)]
print(ls)

#printing table of 2
table=[]
table=[i*2 for i in range(1,11)]
print(table)
# print million of numbers
for i in range(1,3):
    print(i)

#making list of one to million numbers
ls=list(range(1,1000000))
print(max(ls))
print(min(ls))
print(sum(ls))


#multiples of 3 from 3 to 30
multiple=list(range(3,31,3))
print(multiple)

# list slicing
friends=['kashi' , 'hammad' , 'hamid' , 'shah' , 'habibi']
print(friends[-4:])
for friend in friends[:]:
    print(friend)
print(f"My friends list are {friends}")
kashifriend=friends[:]
print(f"Kashi friend list is {kashifriend}")
