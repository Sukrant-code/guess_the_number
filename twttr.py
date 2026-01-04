answer = input("Input: ")


for char in answer:
    if char in "aeiou":
        answer = answer.replace(char, "")
print("Output:", answer)
