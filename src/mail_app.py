import smtplib
from configparser import ConfigParser

parser = ConfigParser()
parser.read('envvars.ini')

EMAIL = parser.get('envvars', 'EMAIL_ADDRESS')
PWD = parser.get('envvars', 'EMAIL_PASSWORD')


def email_service(name, url, price):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(EMAIL, PWD)

	server.sendmail(EMAIL,
		EMAIL,
		message_builder(name, url, price))

	print('email sent')

	server.quit()


def message_builder(name, url, price):
	subject = f'Price update on Amazon website for {name}, now down to {price.encode('utf-8')}'
	body = f'Check the link: {url}'
	msg = f'Subject: {subject}\n\n{body}'
	return msg
