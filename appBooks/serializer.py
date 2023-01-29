from rest_framework import serializers
from .models import Book
from django.forms import ValidationError


class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == "cringe2":
            raise ValidationError("No Abusive People Please...!")
        return value

    def validate(self, data):
        if data["number_of_pages"] < 100 or data["quantity"] < 100:
            raise ValidationError("Too less for bussiness Purpose...!")
        return data

    def get_description(self, data):
        return "This book is called " + str(data.title) + " and it has " +  str(data.number_of_pages) + " pages"