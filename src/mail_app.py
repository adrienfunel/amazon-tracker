import smtplib

def email_service():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('funel.adrien@gmail.com', 'pwd')

	subject = ''
	body = ''

	msg = f'Subject: {subject}\n\n{body}'

	server.sendmail(
		'',
		'',
		msg)

	server.quit()