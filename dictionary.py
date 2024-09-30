print("U15IG22S0054")
d={}
s=input("Enter the sentence")
words=s.split(" ")
for w in words:
    if w in d:
        c=d.get(w)
        c=c+1
        d.update({w:c})
    else:
        d.update({w:1})
print(d)
print("The words present in sentence are as follows")
print(d.keys())
print("The words and its count are as follows")
for key,value in d.items():
    print(f"The word {key} present {value} times in the sentence")