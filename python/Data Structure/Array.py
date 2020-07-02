# https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/
# can use array library or just use list in python
import array
arr=array.array('i',[1,2,3])
print(arr[2])
li=[1,2,3]

# li.append(x) append x to the end of li
li.append(4)
print(li)

# li.insert(i,x) insert x to li in index i
li.insert(2,5)
print(li)

# li.pop(i) pop element of li in index i
# li.pop() pop the last element of li
print(li.pop(2))
print(li)

# li.remove(x) remove the first occurrence of the value
# mentioned in its arguments
li.remove(2)
print(li)

# li.index(x) returns the index of the first occurrence
# of value mentioned in arguments
print(li.index(3))

# li.reverse() reverse li and return nothing
li.reverse()
print(li)
