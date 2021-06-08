import re

def parse_email(address):
    RE_mail = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not RE_mail.match(address):
        raise ValueError(f'Неправильный адрес электронной почты: {address}')
    print(RE_mail.match(address).groupdict())

for i in ['alya@google.com', 'uly#@google.com', 'bloodbath@googlecom']:
    try:
        parse_email(i)
    except ValueError as error:
        print(error)
