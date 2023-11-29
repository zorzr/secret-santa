import random
from cryptography.fernet import Fernet

def fernet_encrypt(text):
	key = 'YOUR-FERNET-KEY'
	return Fernet(key).encrypt(text.encode('utf-8')).decode('utf-8')


# print(Fernet.generate_key().decode('utf-8')); exit(0)

random.seed(0)
participants = ["Alice", "Bob", "Charlie"]


secret_santa = dict()
while True:
	extraction = participants[:]
	random.shuffle(extraction)

	check = True
	temp_santa = dict()
	for p in participants:
		temp_santa[p] = extraction.pop(0)
		if p == temp_santa[p]:
			check = False
			break
	
	if check:
		for p in participants:
			secret_santa[p] = fernet_encrypt(temp_santa[p])
		break


for key in secret_santa.keys():
	print(key + '\n' + secret_santa[key] + '\n\n')
