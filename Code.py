string=[]
string=list(input("Enter your string: "))
reverse_string=""
while string:
    reverse_string+=str(string.pop())

print("\n",reverse_string)
