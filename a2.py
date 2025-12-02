amount=int(input("Enter amount:"))
n1=amount//100
n2=(amount%100)//50
n3=((amount%100)%50)//10
print("No.of Hundred notes:",n1)
print("No.of Fifty notes:",n2)
print("No.of Ten notes:",n3)
