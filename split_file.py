lst = ["1","2","3","4","5","6","7","8","9","10"]


xx = [lst[i:i+3] for i in range(0,len(lst), 3)]

for chunk in xx:
    print("\n".join(chunk))