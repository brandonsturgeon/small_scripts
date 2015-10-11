
print len([x for x in range(int(raw_input("Number to check: "))) if len([a for k, a in enumerate(str(x)[:-1]) if int(a) < int(str(x)[k+1])]) == len(str(x))-1])
