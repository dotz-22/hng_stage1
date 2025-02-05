from rest_framework import serializers

class NumberSerializer(serializers.Serializer):
    number = serializers.IntegerField()

    # def validate_number(self, value):
    #     return abs(value)