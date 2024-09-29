from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

# View para listar e criar (GET e POST)
class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# View para recuperar, atualizar e deletar um item específico (GET, PUT, DELETE)
class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
