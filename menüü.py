#funktsioon mis loeb albumite failist kõik vajaliku
def loeAlbumid():
    järk = []
    with open("albumid", "rt") as f:
        for line in f:
            järk.append(line)
            print(järk[-1])

