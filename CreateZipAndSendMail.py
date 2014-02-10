import os
import sys
import email
import smtplib
import shutil


#Creating archive for the specified folder

def createZip(path):
	base_name = path
	format = "zip"
	root_dir = path
	shutil.make_archive(base_name,format,root_dir)
	sendEmail(base_name +".zip",path)




#Sending attachment in zip format to the specified list of recipients
def sendEmail(file_name,path):
	my_email = 'aryak12345@gmail.com'
	my_passw = '64321Helios'
	#recipients = ['sabyasengupta259@gmail.com', 'aryak.sengupta@gmail.com','anirbandey2010@gmail.com','anirbanavi1993@gmail.com','anshumalikumar9@gmail.com','arupam.sengupta@gmail.com','binghosh@gmail.com','kinjalbasu100@gmail.com','koustuvsinha@gmail.com','ppppallab@gmail.com','src0108@gmail.com','subhodip.kumar@gmail.com']
	recipients = ['sabyasengupta259@gmail.com', 'aryak.sengupta@gmail.com']
	subject = 'Sent from smtplib'
	message = 'This is the body of the email.'

	# build the message
	msg = email.MIMEMultipart.MIMEMultipart()
	msg['From'] = my_email
	msg['To'] = ', '.join(recipients)
	msg['Date'] = email.Utils.formatdate(localtime=True)
	msg['Subject'] = subject
	msg.attach(email.MIMEText.MIMEText(message))

	# build the attachment
	att = email.MIMEBase.MIMEBase('application', 'octet-stream')
	att.set_payload(open(file_name, 'rb').read())
	email.Encoders.encode_base64(att)
	att.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file_name))
	msg.attach(att)

	# send the message
	srv = smtplib.SMTP('smtp.gmail.com', 587)
	srv.ehlo()
	srv.starttls()
	srv.login(my_email, my_passw)
	try:
		srv.sendmail(my_email, recipients, msg.as_string())
		print "Email/attachment has been delivered"
	except:
		print "Problem is sending Email"
	cleaning_up(path,file_name)

def cleaning_up(folderPath,zipPath):
	shutil.rmtree(folderPath)
	os.remove(zipPath)


path = sys.argv[1]
createZip(path)