from rest_framework import serializers

# serializer는 django form과 비슷한 역할을 한다.
# 사용자로 부터 받는 데이터 validataion 등

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

