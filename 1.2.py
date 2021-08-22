stringa = "hasan"
stringb = "nsaha"
def checker(stringa,stringb):
    diccta = {}
    dicctb = {}
    for i in (stringa):
        diccta[i] = 0
    for i in (stringa):
            diccta[i]+=1
    for i in (stringb):
        dicctb[i] = 0
    for i in (stringb):
        dicctb[i]+=1
    for i in (stringb):
        if (dicctb[i]!=diccta[i]):
            return False
    print(diccta)
    return True
if(checker(stringa,stringb)):
    print("alhamdulillah")
    

