from django.core.mail import send_mail

from django.conf import settings
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView, Response
from rest_framework import status

from .serializers import ReviewSerializer, Review, AnswerSerializer, Answer


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
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class CreateAnswerAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = (AllowAny,)
    serializer_class = AnswerSerializer

    def post(self, request):
        data = request.data.get('answer', {})
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        review = Review.objects.get(answer=serializer.data)
        send_mail(
            'Ответ на ваше заявление',
            f'{data["text"]}',
            settings.EMAIL_HOST_USER,
            review.get_email()
        )
        return Response(status=status.HTTP_201_CREATED)


class UserAnswersAPIView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = (AllowAny,)
    serializer_class = AnswerSerializer(many=True)

    def get(self, request, page: int):
        user = request.user
        answers = Answer.objects.filter(author=user)[page * 20:(page + 1) * 20]
        ctx = {
            'user': user,
            'answers': answers
        }
        return Response(ctx)
