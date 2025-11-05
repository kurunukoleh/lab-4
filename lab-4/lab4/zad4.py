text = input("Zdanie")
list = []
text.lower()
for i in text:
    list.append(i)
list.sort()
print(list)