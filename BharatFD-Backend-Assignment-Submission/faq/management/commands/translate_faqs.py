from django.core.management.base import BaseCommand
from faq.models import FAQ
from googletrans import Translator

class Command(BaseCommand):
    help = 'Translate FAQs to Hindi and Bengali'

    def handle(self, *args, **options):
        translator = Translator()
        faqs = FAQ.objects.all()

        for faq in faqs:
            if not faq.question_hi:
                faq.question_hi = translator.translate(faq.question, dest='hi').text
            if not faq.answer_hi:
                faq.answer_hi = translator.translate(faq.answer, dest='hi').text
            if not faq.question_bn:
                faq.question_bn = translator.translate(faq.question, dest='bn').text
            if not faq.answer_bn:
                faq.answer_bn = translator.translate(faq.answer, dest='bn').text
            faq.save()

        self.stdout.write(self.style.SUCCESS('Successfully translated FAQs'))

