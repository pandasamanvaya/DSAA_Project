true = 0
false = 0


with open("mismatch.txt","w") as of:
	with open("2018121002.txt","r") as f:
		lno = 0
		for l in f:
			lno += 1
			a = l.split(" ")
			a1 = a[0].split("_")
			a2 = a[1].split("_")

			if a1[0] == a2[0] and a1[1] == a2[1]:
				true+=1
			else:
				false += 1
				of.write(l)


print(true, false)
print(true*100.0/(true+false))