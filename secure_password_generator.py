import secrets
import argparse
import string
import sys
import pyfiglet


BLUE = '\033[94m'
RESET = '\033[0m'


def print_banner():
    banner = pyfiglet.figlet_format('Generate')
    print(f'{BLUE}{banner}{RESET}')


# Show the banner only when help is being requested, before argparse prints its own help text
if '-h' in sys.argv or '--help' in sys.argv:
    print_banner()


parser = argparse.ArgumentParser(
    prog='Generate',
    epilog='Example: python secure_password_generator.py -l 16 -n 3 --no-symbols',
    description="""A lightweight command-line password generator 
    built with Python and argparse, designed to create strong, 
    customizable passwords for secure authentication."""
)
parser.add_argument('-g', '--generate', action='store_true', help='generates a random password from the %(prog)s program')
parser.add_argument('-l', '--length', type=int, default=16, help='specify the length of the password (default: 16)')
parser.add_argument('-n', '--number', type=int, default=1, help='specify the number of passwords to generate (default: 1)')
parser.add_argument('--no-digits', action='store_true', help='excludes numbers from password')
parser.add_argument('--no-symbols', action='store_true', help='excludes symbols from password')
parser.add_argument('--no-uppercase', action='store_true', help='excludes uppercase letters')
parser.add_argument('-e', '--exclude', action='append', help='specify characters to exclude')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')


def auto_generate(length=16, number=1):
    passwd_make = string.ascii_letters + string.digits + string.punctuation
    passwords = []
    for i in range(number):
        password = ''.join(secrets.choice(passwd_make) for i in range(length))
        passwords.append(password)
    return passwords


def build_pool(args):
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    if args.no_uppercase:
        pool = pool.replace(string.ascii_uppercase, '')
    if args.no_digits:
        pool = pool.replace(string.digits, '')
    if args.no_symbols:
        pool = pool.replace(string.punctuation, '')

    if args.exclude:
        excluded_chars = set(''.join(args.exclude))
        pool = ''.join(char for char in pool if char not in excluded_chars)

    if not pool:
        raise ValueError("Character pool is empty — check your exclusion flags, you excluded everything!")

    return pool


def generate_passwords(pool, length, number):
    passwords = []
    for i in range(number):
        password = ''.join(secrets.choice(pool) for i in range(length))
        passwords.append(password)
    return passwords


def uses_customization(args):
    return any([
        args.no_digits,
        args.no_symbols,
        args.no_uppercase,
        args.exclude,
    ])


def main():
    args = parser.parse_args()

    if args.length <= 0:
        parser.error("--length must be a positive integer")
    if args.number <= 0:
        parser.error("--number must be a positive integer")

    if uses_customization(args):
        try:
            pool = build_pool(args)
        except ValueError as e:
            parser.error(str(e))
        passwords = generate_passwords(pool, args.length, args.number)
    else:
        passwords = auto_generate(args.length, args.number)

    for password in passwords:
        print(password)


if __name__ == "__main__":
    main()
