import zipfile
import time
file = input("Enter the zipfile that you want to extract?\n>> ")
def main(zipfile_name):
	charlist = 'abcdefghijklmnopqrstuvwxyz'
	complete = []
	print("Searching....")
	for current in range(3):
		a = [i for i in charlist]
		for x in range(current):
			a = [y + i for i in charlist for y in a]
		complete = complete + a


	tries = 0
	z = zipfile.ZipFile(f'{zipfile_name}.zip')
	initial_time = time.time()
	for password in complete:
		try:

			tries+=1
			z.setpassword(password.encode("ascii"))
			z.extract(f'{zipfile_name}.txt')

			print(f"password was found: {password}\nTries taken: {tries}")
			input(f"time taken {time.time() - initial_time} seconds!")

			break
		except:
			print(f"password generated: {password}")
			pass

main(file)
