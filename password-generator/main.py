import random
import argparse

UPPER_CHARS   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CHARS   = "abcdefghijklmnopqrstuvwxyz"
NUMERIC_CHARS = "01234567890"
SPECIAL_CHARS = "@#?&!$%"

def generate_password(length=8, uppercase=True, lowercase=True, numeric=True, special_chars=True):
    
	ALL_CHARS = list(
	    "".join([
	    UPPER_CHARS   if uppercase     else "",
	    LOWER_CHARS   if lowercase     else "",
	    NUMERIC_CHARS if numeric       else "",
	    SPECIAL_CHARS if special_chars else ""
	    ])
	)

	random.shuffle(ALL_CHARS)

	return "".join(random.choices(ALL_CHARS, k=length))
	
if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("length", type=int, help="length of password")
	parser.add_argument("-u", "--uppercase", action="store_true", help="include uppercase characters in password")
	parser.add_argument("-l", "--lowercase", action="store_true", help="include lowercase characters in password")
	parser.add_argument("-n", "--numeric", action="store_true", help="include numeric characters in password")
	parser.add_argument("-s", "--special-chars", action="store_true", help="include special characters in password")

	args = parser.parse_args()

	optional_args_count = args.uppercase + args.lowercase + args.numeric + args.special_chars

	while True:
		if optional_args_count:
			print(generate_password(args.length, args.uppercase, args.lowercase, args.numeric, args.special_chars), end="")
		else:
			print(generate_password(args.length), end="")
		
		try:
			input()
		except:
			break

# TODO: add copy-to-clipboard support with pyperclip

# generate passwords of lenth 8 with uppercase, lowercase, numeric and lowercase characters
# -> python3 main.py 8 -u -l -n -s
