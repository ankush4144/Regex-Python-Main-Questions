#Write a python program to find a valid Indian phone number from a text.
#(Valid Indian numbers will start with "+91-" and after that [6-9]
#followed by 9 digits.)
import re
i=input("Enter Text From Which You Want To Search Indian Number: ")
search=r"[+]{1}91-[6-9]{1}\d{9}"
print(re.findall(search,i))
    

