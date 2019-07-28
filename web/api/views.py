from django.views.generic import View
from django.core.mail import send_mail
from django.http import JsonResponse


class SendMailView(View):

    def get(self, request):

        subject = 'subject'
        message = 'some message...'
        from_email = 'foobar@gmail.com'
        recipient = ['bizzbuzz@gmail.com']
        send_mail(subject, message, from_email, recipient)

        return JsonResponse({'success': True})
