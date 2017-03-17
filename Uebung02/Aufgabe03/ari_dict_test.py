from Uebung02.Aufgabe03.ari_dict import AriDict

adict1 = AriDict({ "Addierbar": 2, "AuchAddierbar": 3.5, "NichtAddierbar": {1:2}})
adict2 = AriDict({"Addierbar":1 , "AuchAddierbar":4.1 , "NichtAddierbar":{3:4}})
adict3 = {"Addierbar":3 , "AuchAddierbar":5.2 , "NichtAddierbar":{5:6}}
print(adict1 + adict2)
print(adict1 + adict3)
print(adict3 + adict2)
print(len(adict1))

