
#Loeme albumite failist laulud,albumid ja nende aastad
def loeAlbumid():
    järk = []
    with open("albumid", "rt") as f:
        for line in f:
            järk.append(line)
            print(järk[-1])

