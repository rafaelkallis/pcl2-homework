from Uebung02.Aufgabe03.ari_dict import AriDict

adict1 = AriDict({ "Addierbar": 2, "AuchAddierbar": 3.5, "NichtAddierbar": {1:2}})
adict2 = AriDict({"Addierbar":1 , "AuchAddierbar":4.1 , "NichtAddierbar":{3:4}})
adict3 = {"Addierbar":3 , "AuchAddierbar":5.2 , "NichtAddierbar":{5:6}}

assert (adict1 + adict2)["Addierbar"] == 3
assert (adict1 + adict2)["AuchAddierbar"] == 7.6
assert (adict1 + adict2)["NichtAddierbar"] == {1:2}
# print(adict1 + adict2)


assert (adict1 + adict3)["Addierbar"] == 5
assert (adict1 + adict3)["AuchAddierbar"] == 8.7
assert (adict1 + adict3)["NichtAddierbar"] == {1:2}
# print(adict1 + adict3)


assert (adict3 + adict2)["Addierbar"] == 4
assert (adict3 + adict2)["AuchAddierbar"] == 9.3
assert (adict3 + adict2)["NichtAddierbar"] == {5:6}
# print(adict3 + adict2)


assert (len(adict1)) == 3
# print(len(adict1))

print("All tests passed!")
