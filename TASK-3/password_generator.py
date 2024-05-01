import random
import string
ALL = string.ascii_letters + string.digits + string.punctuation
n=int(input("Enter length of Password : "))
pas=''.join(random.choices(ALL,k=n))
print(pas)
