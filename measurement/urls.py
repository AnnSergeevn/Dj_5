from django.urls import path
from measurement.views import AddMeasurement, SensorUpdateView, ListSensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ListSensor.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', AddMeasurement.as_view()),

]