import hashlib
import argparse

def crack_password(known_hash: str, password_list: str) -> None:
    
    with open(password_list, "r") as _password_list:
        passwords = _password_list.readlines()

    for password in passwords:
        password = password.strip()

        password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

        if password_hash == known_hash:
            print(f"[SUCCESS]: {password}")
            break
    else:
        print(f"[FAILURE]: password not found in {password_list}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Crack SHA256 Encrypted Passwords using Dictionary Attack")

    parser.add_argument("-k", "--known-hash", type=str, required=True)
    parser.add_argument("-p", "--password-list", type=str, required=True, help="text file containing passwords")

    args = parser.parse_args()

    crack_password(args.known_hash, args.password_list)

# example
# $ python3 main.py -k=8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92 -p=passwords.txt 
# [SUCCESS]: 123456

# difference between dictionary attack and rainbow table attack
# https://security.stackexchange.com/questions/224364/is-there-a-difference-between-a-rainbow-table-and-a-dictionary-attack

# common password lists
# https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials

# download files with curl
# curl -o passwords.txt https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt

# How Hackers Can Still Break Your Passwords (YouTube)
# https://www.youtube.com/watch?v=cjdiIKFYeXQ
