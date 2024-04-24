from django.urls import path
from measurement.views import DemoView, AddMeasurement, SensorUpdateView, ListSensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', DemoView.as_view()),
    #path('sensors/<int:pk>', DemoView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', AddMeasurement.as_view()),
    path('sensors/', ListSensor.as_view()),

]