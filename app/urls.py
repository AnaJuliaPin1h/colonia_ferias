from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/<int:id>/', views.gerar_pdf, name='gerar_pdf'),
    path('api/', include(router.urls)),
]