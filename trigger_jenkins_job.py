import json
import requests
import time
import smtplib

url = "http://jenkins.example.com:8080/job/demo/buildWithParameters?VM_GEN=$VALID_ARGUMENT"

def trigger_job (VALID_ARGUMENT):
    if VALID_ARGUMENT.upper() == "M4" or VALID_ARGUMENT.upper() == "M5":
        try:
            while True:
                return_json= requests.get(url)
                if str (return_json.status_code) == "201":
                    start_log = "Jenkins job started sometime back."
                else:
                     start_log = "Failed to trigger the Jenkins job"
                     send_email()
                     return False
                if return_json['building']:
                    time.sleep(60)
                else:
                    if return_json['result'] == "SUCCESS":
                        print (start_log + 'Job is now successfull.')
                        return True
                    else:
                        print ("Job status - failed")
                        send_email()
                        return False
        except Exception:
            return False
    else:
        return 'Invalid argument. Only allowed values are M4 and M5.'

def send_email():
    sender = 'from@fromdomain.com'
    receivers = 'to@todomain.com'

    message = """From: Sender <from@fromdomain.com>
    To: Receiver <to@todomain.com>
    Subject: Jenkins Jobs faliure report

    Jenkins job has failed. Please take a look.
    """

    try:
       smtpObj = smtplib.SMTP('smtpserver.domain.com', 587)
       smtpObj.sendmail(sender, receivers, message)         
       print ("Successfully sent email")
    except Exception:
       print ("Error: unable to send email")
    
