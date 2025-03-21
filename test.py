import num2words as n2w

lt = []

converted=[]

for item in range(1, 10):
    lt.append(item)

    converted.append(n2w.num2words(item))

print (lt)
    
print (converted)