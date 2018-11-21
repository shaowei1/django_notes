from .models import BookInfo
from rest_framework import serializers


class HeroSerializers(serializers.Serializer):
    # 英雄序列化器
    name = serializers.CharField()
    hgender = serializers.IntegerField()
    hcomment = serializers.CharField()
    hbook = serializers.StringRelatedField()


class BookSerializers(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)

    heroinfo_set = HeroSerializers(many=True, read_only=True)

    class Meta:
        model = BookInfo
        # fields = '__all__'
        fields = ('id', 'btitle', 'bpub_date', 'bread', 'name', 'bcomment', 'heroinfo_set')
        # fields = ('id', 'btitle', 'bpub_date', 'bread', 'name', 'bcomment')
        # exclude = ('is_delete',)

        extra_kwargs = {
            'id': {
                'read_only': True
            },
        }
