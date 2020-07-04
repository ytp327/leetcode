input1="196.13.184.0"
input2="196.13.189.0"
input3="255.255.128.0"
import sys
def check(input1, input2, input3):
    input1 = list(map(int, input1.split('.')))
    input2 = list(map(int, input2.split('.')))
    input3 = list(map(int, input3.split('.')))
    for i in range(len(input1)):
        if not (input1[i]&input3[i]==input2[i]&input3[i]):
            return False
    return True
flag=-1
for line in sys.stdin:
    flag=(flag+1)%3
    if flag==0:
        input1=line
    elif flag==1:
        input2=line
    else:
        input3=line
        print(check(input1, input2, input3))
#print(check(input1, input2, input3))