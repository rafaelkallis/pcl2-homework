
from Uebung02.Aufgabe01.dictionary import Dictionary

dict = Dictionary("English", "Greek")
dict.add_card("science", "επιστήμη")
dict.add_card("water", "νερό")
dict.add_card("darkness", "σκοτάδι")
dict.add_card("star", "άστρο")
dict.add_card("economics", "οικονομικά")
dict.add_card("radius", "ακτίνα")
dict.add_card("computer", "υπολογιστής")
dict.add_card("sun", "ήλιος")
dict.add_card("circle", "κύκλος")
dict.add_card("light", "φώς")

print(*dict.cards, sep=',')

print(dict.translate("computer"))
print(dict.translate_back("υπολογιστής"))

dict.start_training(2)