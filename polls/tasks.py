from celery import shared_task
from twilio.rest import Client

from polls.models import Phone, Sms, Approved


@shared_task
def send_phone():
    number = Phone.objects.latest('id').phone
    account_sid = "YOUR KEYS"
    auth_token = "YOUR KEYS"
    verify_sid = "YOUR KEYS"
    client = Client(account_sid, auth_token)
    verification = client.verify.v2.services(verify_sid) \
        .verifications \
        .create(to=number, channel="sms")
    print(verification.status)


@shared_task
def smss():
    number = Phone.objects.latest('id').phone
    sms = Sms.objects.latest('id').sms
    account_sid = "YOUR KEYS"
    auth_token = "YOUR KEYS"
    verify_sid = "YOUR KEYS"
    client = Client(account_sid, auth_token)
    verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=number, code=sms)
    print(verification_check.status)
    Approved.objects.create(phone=number, approved=verification_check.status)
