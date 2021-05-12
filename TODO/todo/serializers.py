from rest_framework import serializers
from todo.models import Todo, LANGUAGE_CHOICES, STYLE_CHOICES


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']



