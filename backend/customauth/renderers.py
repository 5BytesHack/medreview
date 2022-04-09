import json

from rest_framework.renderers import JSONRenderer


class CustomUserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get('errors', None)
        token = data.get('token', None)

        if errors is not None:
            return super(CustomUserJSONRenderer, self).render(data)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return json.dumps({
            'user': data
        })
