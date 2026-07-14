# SECURE_PASSWORD_GENERATOR
A lightweight command-line password generator built with Python and argparse, designed to create strong, customizable passwords for secure authentication.

## Features

- Cryptographically secure password generation using Python's `secrets` module (not `random`)
- Customizable password length
- Generate multiple passwords in a single run
- Exclude digits, symbols, or uppercase letters
- Exclude specific characters of your choice
- Colorful ASCII banner on `--help`

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/secure_password_generator.git
cd secure_password_generator
```

## Usage

Generate a default password (16 characters, all character types):

```bash
python secure_password_generator.py
```

### Options

| Flag | Description | Default |
|---|---|---|
| `-l`, `--length` | Length of the generated password | `16` |
| `-n`, `--number` | Number of passwords to generate | `1` |
| `--no-digits` | Exclude numbers | off |
| `--no-symbols` | Exclude special characters | off |
| `--no-uppercase` | Exclude uppercase letters | off |
| `-e`, `--exclude` | Exclude specific characters (repeatable) | none |
| `-h`, `--help` | Show help message |  |
| `--version` | Show program version | v1.0 |

### Examples

Generate a 20-character password:
```bash
python secure_password_generator.py -l 20
```

Generate 5 passwords at once:
```bash
python secure_password_generator.py -n 5
```

Generate a password without symbols or digits:
```bash
python secure_password_generator.py --no-symbols --no-digits
```

Exclude specific characters (e.g., ambiguous ones like `l`, `1`, `O`, `0`):
```bash
python secure_password_generator.py -e l -e 1 -e O -e 0
```

Combine options:
```bash
python secure_password_generator.py -l 24 -n 3 --no-uppercase -e "'" -e '"'
```

## Security notes

- Passwords are generated using Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module, which is designed for cryptographic use  unlike the `random` module, it is not predictable from previous outputs.
- By default, the character pool includes all of `string.punctuation`, which contains characters such as `\`, `"`, and `'` that can occasionally cause issues in certain shells, config files, or login forms. Use `-e` to exclude any characters that don't work for your use case.
- Generated passwords are printed to standard output. If you're using this in a script or workflow, be mindful of where that output ends up (terminal history, logs, etc.).

## Roadmap

- [ ] Copy-to-clipboard flag (`--copy`)
- [ ] Password strength/entropy estimation
- [ ] Web version built with Flask
- [ ] TOTP-based authenticator companion tool (like Google Authenticator)

## License

MIT
