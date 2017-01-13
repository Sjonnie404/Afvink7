#AfvinkOpdracht 7
#Auteur:        Shane Pullens


def main():
    getSequentie()
    isDNA()
    RNAconvert()
    StartStop()

def getSequentie():
    #sequentie bestand opvragen
    getBestand = input("Geef de naam van je bestand op.")
    gene = open(getBestand,"r")
    print (getBestand)
    gene.readline()
    
    seq = ""
    for c in gene:
        seq = seq + c
    seq = seq.replace("\n","")  #Dit zorgt ervoor dat de enters worden weggehaald
    global seq

def isDNA():
    gene = seq
    DNA = True
    
    for line in gene:
        line = line.lower()
        for char in line:
            if char != "g" and\
               char != "c" and\
               char != "a" and\
               char != "t" and\
               char != "n":             #Dit is voor sommige sequencies die niet volledig gesequenced zijn.
                DNA = False
    print ("")
    if DNA == True:
        print ("Dit is DNA.")
    elif DNA == False:
        print ("Dit is geen DNA")
    print ("")

def RNAconvert():
    rna = seq.replace("T","U")
    global rna

def StartStop():
    gene = rna
    start = gene.find("AUG")

    stop = 0
    while stop <= len(gene):        #Deze loop zoekt naar alle TAA tot er 1 is 
        stop = gene.find("UAA", stop)#gevonden boven het startcodon
        if stop >= start:
            break
        stop += 3
    
    stop1 = 0
    while stop1 <= len(gene):       #Deze loop zoekt naar alle TAC tot er 1 is
        stop1 = gene.find("UAC", stop1)#gevonden boven het startcodon
        if stop1 >= start:
            break
        stop1 += 3

    stop2 = 0
    while stop2 <= len(gene):       #Deze loop zoekt naar alle TAC tot er 1 is 
        stop2 = gene.find("UGA", stop2)#gevonden boven het startcodon
        if stop2 >= start:
            break
        stop2 += 3
      
    L = (stop,stop1,stop2)
    realStop = L.index(min(L))  #het stopcodon moet altijd groter zijn dan het startcodon
    realStop = L[realStop]
    print ("Eerste startcodon:\t",start)
    print ("Eerst volgende stopcodon",realStop) #Dit kiest de laagste stopcodon

    compstr = gene[start:realStop]
    global compstr
    print ("Transcriptie van RNA: ",compstr)
main()
