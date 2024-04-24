# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
import datetime
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from django.http import HttpResponse
from rest_framework.response import Response


# def create_measurement(request):
#     Measurement(temperature=22.3, created_at=datetime.datetime.now().time(), sensor = 1).save()
#     return HttpResponse("Все получилось!")
#
#
# def create_sensor(request):
#     measurements = Measurement.objects.all()
#     for measurement in measurements:
#         Sensor.objects.create(name="ESP32", description="Перенес датчик на балкон", measurement=measurement)
#     return HttpResponse("Все получилось!")
#


class AddMeasurement(CreateAPIView):
    """
        Ввод показаний датчика
        """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class DemoView(ListCreateAPIView):
    """
            Информация по всем датчикам
            """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class ListSensor(ListCreateAPIView):
    """
    Список всех датчиков и создание нового датчика
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(CreateAPIView):

    def post(self, request):
        Measurement(temperature=35.3, created_at=datetime.datetime.now().time()).save()


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, description):
        Sensor.objects.filter(description=description).update(descr="Перенес датчик на кухню")

