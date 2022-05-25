def is_palindrome(word):
 
  if word == word[::-1]:
    return "True"
  else: 
    return "False"
       
result=is_palindrome('abba')
print(result)

