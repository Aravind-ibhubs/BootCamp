from rest_framework import serializers
from book.models import Author

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    
    class Meta:
        fields = ['id', 'name', 'category', 'age']
    
    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.age = validated_data.get("age", instance.age)
        instance.save()
        
        return instance
    