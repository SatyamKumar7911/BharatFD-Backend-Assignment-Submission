from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Question (Hindi)"), blank=True)
    question_bn = models.TextField(_("Question (Bengali)"), blank=True)
    answer_hi = RichTextField(_("Answer (Hindi)"), blank=True)
    answer_bn = RichTextField(_("Answer (Bengali)"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_text(self, field, lang):
        if lang == 'hi' and getattr(self, f"{field}_hi"):
            return getattr(self, f"{field}_hi")
        elif lang == 'bn' and getattr(self, f"{field}_bn"):
            return getattr(self, f"{field}_bn")
        return getattr(self, field)

    def __str__(self):
        return self.question

