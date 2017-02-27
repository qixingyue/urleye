import wrapper
import lib.mail
import json

@wrapper.hander_method
def mail_json(json_mails):
	mail_params = json.loads(json_mails)
	for mail_param in mail_params:
		subject = mail_param["subject"]
		content = mail_param["content"]
		toemail = mail_param["toemail"]
		lib.mail.send_mail(toemail,subject,content)

