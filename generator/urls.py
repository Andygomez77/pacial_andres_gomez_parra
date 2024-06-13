from django.urls import path
from .views import models, models_info

app_name = 'modelos'

urlpatterns = [
    path('', models, name='models'),
    path('<int:carro_id>', models_info, name='modelos_info')
]
