import hashlib

# initializing string 
str = "SASA"
  
# encoding GeeksforGeeks using encode() 
# then sending to SHA256() 
result = hashlib.sha512(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 