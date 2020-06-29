import random
x=[1,2,3,4]
random.shuffle(x)# not repeat choose
y=random.choice(x)# repeat choose
print(y)
y=random.randrange(1,2,1)#int not include 2
print(y)
y=random.uniform(1,9)#float
print(y)