from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']

    def to_representation(self, instance):
        lang = self.context['request'].query_params.get('lang', 'en')
        ret = super().to_representation(instance)
        ret['question'] = instance.get_translated_text('question', lang)
        ret['answer'] = instance.get_translated_text('answer', lang)
        return ret

