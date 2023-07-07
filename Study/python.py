def prog():
	files = open("autok.txt")
	record = files.readlines()
	second(record)
	third(record)
	fourth(record)
	fifth(record)

def second(kiki):
	print("2. feladat")
	szam = " "
	for i in kiki:
		if i.endswith("0\n"):
			szam = i
	data = szam.split()
	print(data[0] + ". nap rendszám: " + data[2])

def third(harom):
	print("3. feladat")
	nap = input("nap: ")
	print("Forgalom a(z) " + nap + ".napon:")
	for i in harom:
		data = i.split()
		if data[0] == nap:
			if data[5] == "0":
				print(data[1] + " " + data[2] + " " + data[3] + " " + "ki")
			if data[5] == "1":
				print(data[1] + " " + data[2] + " " + data[3] + " " + "be")

def fourth(negy):
	print("4. feladat")
	ki = 0
	be = 0
	for i in negy:
		data = i.split()
		if data[5] == "0":
			ki += 1
		elif data[5] == "1":
			be += 1
	print("A hónap végén " + str(ki - be) + " autót nem hoztak vissza")

def fifth(ot):
	print("5. feladat")
	rendszamok = ""
	for line in ot:
		data = line.split()
		if data[2] not in rendszamok:
			rendszamok += data[2] + " "
	rendszam = rendszamok.split()
	rendszam.sort()
	for r in rendszam:
		first = ""
		last = ""
		for i in ot:
			if r in i:
				if first == "":
					first = i
				else: 
					last = i
		firstone = first.split()
		lastone = last.split()
		print(r + " " + str(int(lastone[4]) - int(firstone[4])) + " km")		
			














def kettto(csiga):
	print("4. feladat")
	ki = 0
	for szamlalo in csiga:
		data = szamlalo.split()
		if szamlalo.endswith("0\n"):
			ki += 1
		else:
			ki -= 1
	print("A hónap végén " + str(ki) + " autót nem hoztak vissza")
	























def kettes(file):
	temp = " "
	for i in file:
		if i.endswith("0\n"):
			temp = i
	data = temp.split()
	print("2. feladat\n" + data[0] + ". nap rendszám: " + data[2])


def harmas(file):
	print("3. feladat")
	nap = input("Nap: ")
	print("Forgalom a(z) " + nap + ".  napon:")
	for line in file:
		data = line.split()
		if data[0] == nap:
			if data[5] == "0":
				print(data[1] + " " + data[2] + " " + data[3] + " " + "ki") 
			if data[5] == "1" :
				print(data[1] + " " + data[2] + " " + data[3] + " " + "be") 
def negy(file):
	print("4. feladat")
	ki = 0
	be = 0
	for line in file:
		data = line.split()
		if data[5] == "0":
			ki += 1
		elif data[5] == "1":
			be += 1
	print("A hónap végén " + str(ki - be) + " autót nem hoztak vissza.")

	


prog() 

