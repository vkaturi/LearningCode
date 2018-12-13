import sys
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)


def getTranslatedMessage(mode, message, key):
	translated = ''
	if mode[0] == 'd':
		key = -key

	for symbol in message:
		symbolIndex = SYMBOLS.find(symbol)

		if symbolIndex == -1:# Symbol not found in SYMBOLS.
			# Just add this symbol without any change.
			translated += symbol
		else:
			# Encrypt or decrypt.
			symbolIndex += key

			if symbolIndex >= MAX_KEY_SIZE:
				symbolIndex -= MAX_KEY_SIZE
			elif symbolIndex < 0:
				symbolIndex += MAX_KEY_SIZE

			translated += SYMBOLS[symbolIndex]
	return translated

	
print getTranslatedMessage('e', 'The sky above the port was the color of television, tuned to a dead channel.', 13)
print getTranslatedMessage('d', 'gur FxL noBIr Gur CBEG JnF Gur pByBE Bs GryrIvFvBA, GHArq GB n qrnq punAAry.', 13)
