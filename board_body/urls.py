from django.urls import path
from .views import index, PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    # path('', index, name='index'),
    path('', PostListView.as_view(), name='index'),
    path('', PostDetailView.as_view(), name='index'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
]