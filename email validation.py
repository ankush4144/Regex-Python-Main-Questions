#Write a python code to find a valid email address from a text.
import re
e_mail=input("Enter your text : ")
search=r"[a-zA-Z0-9-_.]+@[a-zA-Z-_.]+[a-zA-Z]"
print(re.findall(search,e_mail))
    
