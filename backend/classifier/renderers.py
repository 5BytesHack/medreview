import json

from rest_framework.renderers import JSONRenderer


class ReviewRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get('errors')
        if errors:
            return super(ReviewRenderer, self).render(data)
        return json.dumps({
            'review': data
        })
