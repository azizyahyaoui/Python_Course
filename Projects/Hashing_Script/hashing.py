import sys
import hashlib
from colorama import init, Fore

init(autoreset=True)

print(Fore.GREEN + '*********** YAHYA ***********')
print(Fore.CYAN + (
    'Description:\n'
    'This program enables you to hash a password or crack it from a wordlist.\n'
    'Usage:\n'
    '[1] - Hash a password\n'
    '[2] - Crack a hashed password using a wordlist\n'
))

def hash_password(hash_type, password):
    try:
        hash_obj = hashlib.new(hash_type)
        hash_obj.update(password.encode())
        hashed = hash_obj.hexdigest()
        print(Fore.YELLOW + f'Hash type: {hash_type}')
        print(Fore.YELLOW + f'Hashed password: {hashed}')
        print(Fore.YELLOW + f'Hash length: {len(hashed)}')
    except ValueError:
        print(Fore.RED + f"Hash type '{hash_type}' is not supported.")
        print(Fore.YELLOW + f"Try one of: {', '.join(hashlib.algorithms_guaranteed)}")

def crack_password(hash_type, target_hash, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            print(Fore.CYAN + 'Starting brute force...')
            for i, line in enumerate(file):
                password = line.strip()
                try:
                    test_hash = hashlib.new(hash_type)
                    test_hash.update(password.encode())
                except ValueError:
                    print(Fore.RED + f"Hash type '{hash_type}' is not supported.")
                    return
                if test_hash.hexdigest() == target_hash:
                    print(Fore.GREEN + f"Password found: {password}")
                    return
                print(Fore.LIGHTBLACK_EX + f"[{i}] Tried: {password}")
            print(Fore.RED + "Password not found in wordlist.")
    except FileNotFoundError:
        print(Fore.RED + f"Wordlist file '{wordlist_path}' not found.")

def main():
    choice = input("Choose your process:\n[1] Hashing\n[2] Cracking\n--> ").strip()
    if choice == '1':
        hash_type = input("Enter hash type (e.g., md5, sha1, sha256):\n--> ").strip()
        password = input("Enter the password to hash:\n--> ").strip()
        hash_password(hash_type, password)

    elif choice == '2':
        target_hash = input("Enter the hashed password:\n--> ").strip()
        hash_type = input("Enter the hash type used (e.g., md5, sha1, sha256):\n--> ").strip()
        wordlist_path = input("Enter the path to the wordlist:\n--> ").strip()
        crack_password(hash_type, target_hash, wordlist_path)

    else:
        print(Fore.RED + "Invalid choice. Please select 1 or 2.")

if __name__ == '__main__':
    main()
