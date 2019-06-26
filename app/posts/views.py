from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import settings
from .models import BugsChart


class ChartListView(TemplateView):
    template_name = 'posts/chart-list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['bugs_chart_list'] = BugsChart.objects.all().order_by('pk').filter(active=True)

        return context_data


chart_list = ChartListView.as_view()


send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com']
)

# # AWS Config
# EMAIL_HOST = settings['EMAIL_HOST']
# EMAIL_HOST_USER = settings['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD = settings['EMAIL_HOST_PASSWORD']
# EMAIL_PORT = settings['EMAIL_PORT']
#
# msg = MIMEMultipart('alternative')
# msg['Subject'] = "Amazon SES Email"
# msg['From'] = "blessmht@gmail.com"
# msg['To'] = "sender_mail_address"
#
# html = open('index.html').read()
#
# mime_text = MIMEText(html, 'html')
# msg.attach(mime_text)
#
#
# def send_msg(requst, s, me, you):
#     s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
#     s.starttls()
#     s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
#     s.sendmail(me, you, msg.as_string())
#     s.quit()
#     return s
