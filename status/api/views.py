import json
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

# CreateModelMixin: handles POST data
# UpdateModelMixin: handles PUT data
# DestroyModelMixin: DELETE method


class StatusAPIDetailView(
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

    passed_id = None

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, instance):
    #     serializer.save(updated_by_user=self.request.user)

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         instance.delete()
    #     return None


# Login required mixin / decorator
class StatusAPIView(
        mixins.CreateModelMixin,
        generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer

    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # this fills user field which is read-only
        serializer.save(user=self.request.user)
