def count_recursive(sentence, index):
	z = 'z'
	if index >= len(sentence):
		return 0
	elif sentence[index] == z:
		index += 1
		return 1 + count_recursive(sentence, index)
	else:
		index += 1
		return count_recursive(sentence, index)

print(count_recursive("this iz z, this iz anozher z", 0))
