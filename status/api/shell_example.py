from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import CustomSerializer, StatusSerializer
from status.models import Status

"""
Serializer a single object
"""
obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


"""
Serialize a queryset
"""
qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)


"""
Create obj
"""
data = {'user': 1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save()  # You can't save it before running `.is_valid()`

Status.objects.count()
Status.objects.all()


"""
Create obj
"""
obj = Status.objects.first()
data = {'user': 1, 'content': 'some new content'}
update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()
update_serializer.save()


"""
Delete obj
"""
data = {'user': 1, 'content': 'please delete me'}
create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()
print(create_obj)

obj = Status.objects.last()
get_data_serializer = StatusSerializer(obj)
# update_serializer.is_valid()
# update_serializer.save()
obj.delete()

"""
Test custom serializer
"""
data = {'email': 'hello@teamcfe.com', 'content': 'please delete me'}
create_obj_serializer = CustomSerializer(data=data)
if create_obj_serializer.is_valid():
    data = create_obj_serializer.data
    print(data)
    # {'content': 'please delete me', 'email': 'hello@teamcfe.com'}
