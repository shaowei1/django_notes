from rest_framework import serializers
from .models import BookInfo


class BookSerializers(serializers.ModelSerializer):
    # 显示指明字段
    name = serializers.CharField(read_only=True)  # 添加新字段

    # is_delete = serializers.BooleanField(default=False)  # 原有字段重写

    class Meta:
        model = BookInfo  # 指定模型类
        # fields = '__all__' # 指定到底将哪些模型类字段生成序列化器字段
        # fields=('bread','btitle','bpub_date','name')
        # read_only_fields=('bread',) # 给字段添加read_only=True的选项
        exclude = ('is_delete',)  # 取反 除了这个字段，其他字段都生成序列化器字段
        # 给字段添加额外选项
        extra_kwargs = {
            'bcomment': {
                'read_only': True
            }

        }


class HeroSerializers(serializers.Serializer):
    # 英雄序列化器
    name = serializers.CharField()
    hgender = serializers.IntegerField()
    hcomment = serializers.CharField()
    hbook = serializers.StringRelatedField()

# class BookSerializers(serializers.Serializer):
#     btitle = serializers.CharField(max_length=8, min_length=2)
#     bread = serializers.IntegerField(max_value=1000, min_value=1)
#     bpub_date = serializers.DateField()
#     bcomment = serializers.IntegerField(read_only=True)
#     is_delete = serializers.BooleanField(default=True, write_only=True)
#
#     heroinfo_set = HeroSerializers(many=True)
