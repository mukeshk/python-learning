def changeCase(word):
   o = ''.join(c.upper() if c.islower() else c.lower() for c in word)
   print(o)

changeCase("Python")
