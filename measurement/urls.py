from django.urls import path
from measurement.views import DemoView, SensorView, SensorUpdateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', DemoView.as_view()),
    path('sensor/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', SensorView.as_view()),

]