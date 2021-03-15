import string
def atbash(txt):
	alphabet = list(string.ascii_lowercase)
	newTxt = ""
	for ch in txt:
		if ch.lower() not in alphabet:
			newTxt += ch
			continue
		if ch.isupper():
			newTxt += alphabet[25 - alphabet.index(ch.lower())].upper()
		else:
			newTxt += alphabet[25 - alphabet.index(ch)]
	return newTxt