def main():
    name = input("camelCase: ")
    print("snake_case:", python_style(name))

def python_style(name):
   result = ""
   for char in name:
       if char.isupper():
           result += "_" + char.lower()
       else:
           result += char.lower()
   return result
main()