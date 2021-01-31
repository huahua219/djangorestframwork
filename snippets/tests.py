from django.test import TestCase

# Create your tests here.

import json

import os,django

from pip._vendor.six import BytesIO

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# snippet = Snippet.objects.get(id=7)
# serializer = SnippetSerializer(snippet)   # 序列化查询对象
serializer = SnippetSerializer(Snippet.objects.all(), many=True)  # 序列化查询结果集
print(serializer.data)