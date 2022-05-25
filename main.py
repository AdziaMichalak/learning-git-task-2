<<<<<<< HEAD
print("podaj slowo: ")
word = input()

if str(word) == "".join(reversed(word)): 
  print("Palindrome")
else: 
    print("Not Palindrome")

=======
def is_palindrome(word):
 
  if word == word[::-1]:
    return "True"
  else: 
    return "False"
       
result=is_palindrome('abba')
print(result)
>>>>>>> fddfc872a2e260e200accfa98a7901c8febfd94e
