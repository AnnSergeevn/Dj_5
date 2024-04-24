# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
import datetime
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from django.http import HttpResponse
from rest_framework.response import Response


class AddMeasurement(CreateAPIView):
    """
        Ввод показаний датчика
        """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class ListSensor(ListCreateAPIView):
    """
            Список всех датчиков и создание нового датчика.
            """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdateView(RetrieveUpdateAPIView):
    """
    Получение информации по датчику
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, description):
        Sensor.objects.filter(description=description).update(descr="Перенес датчик на кухню")

