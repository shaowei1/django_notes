from rest_framework import serializers
from books.models import BookInfo
from books.models import HeroInfo


class BookSerializers(serializers.ModelSerializer):
    # 显示指明字段
    name = serializers.CharField(read_only=True)  # 添加新字段
    is_delete = serializers.BooleanField(default=True)  # 原有字段重写

    class Meta:
        model = BookInfo  # 指定模型类
        # fields = '__all__' # 指定到底安歇模型类字段生成序列化器字段
        # fields = ('bread', 'btitle', 'bpub_data', 'name')
        # read_only_fields = ('bread') # 给字段添加read_only=True选项
        exclude = ('bread',)  # 取饭，除了这个字段，其他字段都生成序列化器字段
        # 给其他字段添加额外字段
        extra_kwargs = {
            'bcomment': {
                'read_only': True
            }
        }
#
# class HeroSerializers(serializers.Serializer):
#     # 英雄系列化器
#     name = serializers.CharField()
#     hgender = serializers.IntegerField()
#     hcomment = serializers.CharField()
#     hbook = serializers.StringRelatedField()
#
#     pass
#
#
# def test(value):
#     # 验证逻辑
#
#     return
#
# class BookSerializers(serializers.Serializer):
#     # 图书序列化器
#     # 定义序列化器字段
#     btitle = serializers.CharField(max_length=8, min_length=5)
#     bread = serializers.IntegerField(max_value=30, min_value=1)
#     bpub_date = serializers.DateField()
#     # bcomment = serializers.IntegerField(read_only=True)
#     bcomment = serializers.IntegerField(required=True)  # 如果read_only=True或者不传数据, validate中的attrs将会娶不到
#     is_delete = serializers.BooleanField(default=True, write_only=True)
#     # 关联嵌套序列化器的字段指明
#     heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
#
#     # heroinfo_set = serializers.StringRelatedField(many=True)
#     # heroinfo_set = HeroSerializers(many=True)
#
#     # 单一字段验证
#     def validate_btitle(self, value):
#         # 验证btitle是否是python
#         if value == 'python':
#             raise serializers.ValidationError('book name error')
#         return value  # 如果不反悔验证后的书, validated_data无法获取验证
#
#     # 多个字段验证
#     def validate(self, attrs):
#         # 验证阅读数和评论量的关系
#         if attrs['bread'] < attrs['bcomment']:
#             raise serializers.ValidationError('阅读量少于评论量')
#
#         return attrs
#
#     # 保存数据
#     def create(self, validated_data):
#         # 1. 保存图书数据
#         book = BookInfo.objects.create(
#             btitle=validated_data['btitle'],
#             bread=validated_data['bread'],
#             bpub_date=validated_data['bpub_date'],
#         )
#
#         return book
#
#     # 更新数据
#     def update(self, instance, validated_data):
#
#         instance.btitle = validated_data['btitle']
#         instance.bread = validated_data['bread']
#         instance.bpub_date = validated_data['bpub_date']
#
#         instance.save()
#
#         return instance
#         pass
