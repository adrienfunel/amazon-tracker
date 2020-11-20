import smtplib
from configparser import ConfigParser


parser = ConfigParser()
parser.read('envvars.ini')

EMAIL = parser.get('envvars', 'EMAIL_ADDRESS')
PWD = parser.get('envvars', 'EMAIL_PASSWORD')


def email_service(name, url, price, currency):
    """Connect to mailing server and send bespoke update email."""
    server = ServerConnection(EMAIL, PWD).start_connection()

    server.sendmail(EMAIL,
                    EMAIL,
                    message_builder(name, url, price, currency)
                    )

    print('email sent')
    server.quit()


def message_builder(name, url, price, currency):
    """Build message with input information."""
    subject = f'Price update on Amazon website for {name}, now down to {currency}{price}'
    body = f'Check the link: {url}'
    msg = f'Subject: {subject}\n\n{body}'

    return msg


class ServerConnection:
    """Class to create a server connection object using credentials."""
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd

    def start_connection(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.email, self.pwd)
        return server
