#!/usr/bin/env python

import smtplib
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.template import loader, Context
from invites.models import Party

DELAY = 30  # seconds


class Command(BaseCommand):
    args = '[unsent|unseen|unanswered|all|party:N]'
    help = """
        Email invites to recipients who have not yet been sent an email or have
        not seen the invite yet, or to a specific party unconditionally.
    """

    VALID_KINDS = ('unsent', 'unseen', 'unanswered', 'all')

    def handle(self, *args, **options):
        kind = args[0]

        query = {'emailInvite': True}
        if kind.startswith('party:'):
            query['pk'] = int(kind[6:])
        elif kind == 'unsent':
            query['emailSent'] = False
        elif kind == 'unseen':
            query['viewDate'] = None
        elif kind == 'unanswered':
            query['submitDate'] = None
        elif kind != 'all':
            raise CommandError(
                'First argument must be "party:NN" or one of: %s' %
                ', '.join(self.VALID_KINDS))

        for party in Party.objects.filter(**query):
            print 'Sending email to: %s (%s)' % (party.head.name, party.email)
            email = self.make_email(
                party.email,
                self.render(party, settings.EMAIL_TEMPLATE_HTML),
                self.render(party, settings.EMAIL_TEMPLATE_TEXT))
            self.send_email(email, party.email)
            party.emailSent = True
            party.save()
            time.sleep(DELAY)

    @staticmethod
    def render(party, template):
        return loader.get_template(template).render(Context({
            'party': party,
            'settings': settings
        }))

    @staticmethod
    def make_email(recipient, html, text):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "You are cordially invited to %s" % settings.EVENT_NAME
        msg['From'] = settings.SMTP_FROM
        msg['To'] = recipient

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        return msg

    @staticmethod
    def send_email(msg, recipient):
        s = smtplib.SMTP(settings.SMTP_SERVER)
        s.starttls()
        s.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        s.sendmail(settings.SMTP_FROM, recipient, msg.as_string())
