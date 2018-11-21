from rest_framework import serializers
from booksManager.models import Books


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
