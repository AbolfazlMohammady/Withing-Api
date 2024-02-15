from rest_framework import serializers

class WeightSerializer(serializers.Serializer):
    user_id = serializers.CharField()