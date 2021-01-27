from django.contrib.auth.models import Group, User
from rest_framework import serializers

# 在这个例子中我们用到了超链接关系，使用 HyperlinkedModelSerializer。你还可以使用主键和各种其他关系，但超链接是好的RESTful设计。


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        # fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')