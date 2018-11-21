from rest_framework import serializers

from books.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""

    class Meta:
        """
        model 指明该序列化器处理的数据字段从模型类BookInfo参考生成
        fields 指明该序列化器包含模型类中的哪些字段，'__all__'指明包含所有字段
        """
        model = BookInfo
        fields = '__all__'


"""注意：serializer不是只能为数据库模型类定义，也可以为非数据库模型类的数据定义。serializer是独立于数据库之外的存在。"""


# class HeroSerializers(serializers.Serializer):
#     # 英雄序列化器
#     name = serializers.CharField()
#     hgender = serializers.IntegerField()
#     hcomment = serializers.CharField()
#     hbook = serializers.StringRelatedField()
#
#
# class BookSerializers(serializers.Serializer):
#     """图书数据序列化器"""
#     id = serializers.IntegerField(label='ID', read_only=True)
#     btitle = serializers.CharField(label='名称', max_length=20)
#     bpub_date = serializers.DateField(label='发布日期', required=False)
#     bread = serializers.IntegerField(label='阅读量', required=False)
#     bcomment = serializers.IntegerField(label='评论量', required=False)
#     image = serializers.ImageField(label='图片', required=False)
#     # 关联嵌套序列化器字段指明
#     heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
#     # heroinfo_set = serializers.StringRelatedField(many=True)
#     # heroinfo_set = HeroSerializers(many=True)
