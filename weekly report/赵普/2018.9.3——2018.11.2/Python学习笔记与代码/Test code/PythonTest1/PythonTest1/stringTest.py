print("this is stringTest.py start")

name= "ada lovelace"
print(name.title())
name= "ada lovELace"
print(name.title())#强制编程只有首字母大写的情况
name= "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name="ada"
last_name="lovelavc"
full_name=first_name+" "+last_name
print("the full name is"+" "+'"'+full_name.title()+'"')

print("Labguages:\n\tPython\n\tC\n\tJavaScript\n")

favorite_language = '  Python  '
favorite_language1 = favorite_language.rstrip()
favorite_language2 = favorite_language.lstrip()
favorite_language3 = favorite_language.strip()
print(favorite_language1)
print(favorite_language2)
print(favorite_language3)

print("ZhaoPu, "+"Happy "+str(23)+"rd Birthday")
print("this is stringTest.py end\n")
