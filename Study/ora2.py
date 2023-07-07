def prog():
	files = open("tavirathu13.txt")
	records = files.readlines()
	ketto(records)
	harom(records)
	negy(records)
	benya(records)

def ketto(lista):
	print("2.feladat")
	varos = input("Adja meg egy település kódját! Település: ")
	temp = ""
	for sor in lista:
		if sor.startswith(varos):
			temp = sor 
	data = temp.split()
	dataido = data[1]
	print("Az utolsó mérési adat a megadott településről " + dataido[0] + dataido[1] + ":" + dataido[2] + dataido[3] + "-kor érkezett")

def harom(lista):
	print("3.feladat")
	magas = ""
	maxfok = 0
	alacsony = ""
	minfok = 50

	for line in lista:
		data = line.split()
		if int(data[3]) > int(maxfok):
			maxfok = data[3]
			magas = line
		if int(data[3]) < int(minfok):
			minfok = data[3]
			alacsony = line
		nagy = magas.split()
		kicsi = alacsony.split()
		nagyido = nagy[1]
		kicsiido = kicsi[1]
	print(" A legalacsonyabb hőmérséklet: " + kicsi[0] + " " + kicsiido[0] + kicsiido[1] + ":" + kicsiido[2] + kicsiido[3] + " " + kicsi[3] + " fok")
	print(" A legmagasabb hőmérséklet: " + nagy[0] + " " + nagyido[0] + nagyido[1] + ":" + nagyido[2] + nagyido[3] + " " + nagy[3] + " fok")

def negy(lista):
	print("4.Feladat")
	for line in lista:
		data = line.split()
		ido = data[1]
		if data[2] == "00000":
			print(data[0] + " " + ido[0] + ido[1] + ":" + ido[2] + ido[3])
		


























def benya(lista):
	print("4. feladat")
	for line in lista:
		kutya = line.split()
		ido = kutya[1]
		if kutya[2] == "00000":
			print(kutya[0] + " " + ido[0] + ido[1] + ":" + ido[2] + ido[3])
	print("Benyó csinálta geciiiii")
	
















prog()
