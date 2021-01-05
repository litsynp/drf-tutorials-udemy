- Below two codes give the same results

  - Using python default library: json

    ```python
    import json
    from django.http import HttpResponse


    def json_example_view(request):
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
    ```

  - Using a shortcut called JsonResponse

    ```python
    from django.http import JsonResponse


    def json_example_view(request):
        data = {
            'count': 1000,
            'content': 'Some new content'
        }

        return JsonResponse(data)
    ```

  - Using django.views.generic.View

    ```python
    from django.http import JsonResponse
    from django.views.generic import View

    class JsonCBV(View):
        def get(self, request, *args, **kwargs):
            data: dict = {
                'count': 1000,
                'content': 'Some new content'
            }
            return JsonResponse(data)
    ```

    - Creating and inheriting a custom mixin

      ```python
      from django.http import JsonResponse


      class JsonResponseMixin(object):
          def render_to_json_response(self, context, **response_kwargs):
              return JsonResponse(self.get_data(context), **response_kwargs)

          def get_data(self, context):
              return context


      class JsonCBV2(JsonResponseMixin, View):
          def get(self, request, *args, **kwargs):
              data = {
                  'count': 1000,
                  'content': 'Some new content'
              }

              return self.render_to_json_response(data)
      ```

## Serialized Data

- Check serialized data using the command:

  - `$ python .\manage.py dumpdata --format json --indent 4`

  - `$ python .\manage.py dumpdata updates.Update --format json --indent 4`

- This is the same as:

  ```python
  from django.core.serializers import serialize


  data = serialize('json', qs, fields=('user', 'content'))
  ```

- Now check this out

  ```python
  import json


  from django.core.serializers import serialize
  from django.http import HttpResponse
  from django.views.generic import View

  from .models import Update


  class SerializedDetailView(View):
      def get(self, request, *args, **kwargs):
          obj = Update.objects.get(id=1)
          data = serialize('json', [obj, ], fields=('model', 'user', 'content'))
          json_data = data
          return HttpResponse(json_data, content_type='application/json')


  class SerializedListView(View):
      def get(self, request, *args, **kwargs):
          qs = Update.objects.all()
          data = serialize('json', qs, fields=('model', 'user', 'content'))

          json_data = data
          return HttpResponse(json_data, content_type='application/json')
  ```

  - or define your own `serialize()` in the model class in models.py
  - Plus, implement QuerySet and Manager for serialization

## Error handling

- By default, Django returns an HTML doc when an error is thrown.
- For CSRF verification error, you need to allow API methods to be CSRF exempt. (NOT for production)
