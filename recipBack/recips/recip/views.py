from django.http import JsonResponse
from .models import Category, Recips
from .serializers import CategorySerializer, RecipsSerializer
from rest_framework.viewsets import ModelViewSet


def api_users(request):
    if request.method == 'GET':
        users = Recips.objects.all()
        serializer = RecipsSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


class ApiCategoryViews(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ApiRecipsViews(ModelViewSet):
    queryset = Recips.objects.all()
    serializer_class = RecipsSerializer
