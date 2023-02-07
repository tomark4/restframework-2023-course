from django.urls import path
from .views import PagesListView, PageDetailView, PageCreateView, PageEditView, PageDeleteView

pages_patterns = ([
    path('', PagesListView.as_view(), name='list'),
    path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='detail'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', PageEditView.as_view(), name='update'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='delete'),
], 'pages')