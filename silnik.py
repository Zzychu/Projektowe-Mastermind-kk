import rnd
szuk=[]
for i in range(4):
	szuk.append(rnd(0,9))
with open("szuk.txt", "w", encoding="utf-8") as plik:
    for i in szuk:
    	plik.write(i /n)
