import sys
from hashlib import md5
import base64
from cryptography.fernet import Fernet

filename = str()

def help():
	print("\nproper usage:")
	print("\npython3 de-encrypt-fernet.py (e/d) (filename)")
	print("\te - encrypt")
	print("\td - decrypt\n")

def write2file(data):
	with open (filename, "w") as fp:
		fp.write(data)
	print(f"\"{data}\"\n\nwriten to {filename}\n")
	exit()

def encrypt(fr, data):
	ciph_text = fr.encrypt(data).decode()
	write2file(ciph_text)

def decrypt(fr, data):
	try:
		plain_text = fr.decrypt(data).decode()
	except:
		print("\nWrong password\n")
		exit()
	write2file(plain_text)

def main():
	global filename
	if (len(sys.argv) == 3):
		print()
		if (sys.argv[1] == 'e' or sys.argv[1] == 'd'):
			filename = sys.argv[2]
			try:
				with open (filename, "r") as fp:
					data = fp.read()
			except FileNotFoundError:
				print(f"File \"{filename}\" not found")
				return 1

			print("\033c", end="")
			password = str(input("Password: "))
			print("\033c", end="")

			if (sys.argv[1] == 'e'):
				encrypt(Fernet(base64.b64encode(md5(password.encode("utf-8")).hexdigest().encode())), data.encode())	
			elif (sys.argv[1] == 'd'):
				decrypt(Fernet(base64.b64encode(md5(password.encode("utf-8")).hexdigest().encode())), data.encode())

		exit()

	
	help()

	return 0
main()
