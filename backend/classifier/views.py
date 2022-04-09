from django.shortcuts import render

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView, Response

from .serializers import ReviewSerializer, Review


# Create your views here.


class ManagerReviewAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]
    serializer_class = ReviewSerializer(many=True)

    def get(self, request, format=None):
        user = request.user
        reviews = Review.objects.filter(reviewed=False).order_by('id')[:20]
        ctx = {
            'user': user,
            'reviews': reviews
        }
        return Response(ctx)


class ReviewAPIView(APIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    def get(self, request, id):
        '''Как сделать пермишен - если юзер модер, то пускаем, потом проверяем user == review.author'''
        user = request.user
        review = Review.objects.get(pk=id)
        answer = Review.objects.get(review=review)
        ctx = {
            'user': user,
            'review': review,
            'answer': answer
        }
        return ctx


class UserReviewsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]
    serializer_class = ReviewSerializer(many=True)

    def get(self, request):
        user = request.user
        reviews = Review.objects.filter(author=user).order_by('reviewed')
        ctx = {
            'user': user,
            'reviews': reviews
        }
        return ctx


class AllReviewsAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]
    serializer_class = ReviewSerializer(many=True)

    def get(self, request, page: int):
        user = request.user
        reviews = Review.objects.all()[page * 20, (page + 1) * 20]
        ctx = {
            'user': user,
            'reviews': reviews
        }
        return Response(ctx)


class CreateReviewAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = (AllowAny,)
    serializer_class = ReviewSerializer

    def post(self, request):
        data = request.data.get('review', {})
        serializer = self.serializer_class(data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
