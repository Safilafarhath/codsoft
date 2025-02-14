import random
import string
len=int(input("Enter the length of the password:"))
p=''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=len))
print("Password:",p)
