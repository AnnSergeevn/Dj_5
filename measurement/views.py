# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
import datetime
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer
from django.http import HttpResponse
from rest_framework.response import Response


# def create_measurement(request):
#     Measurement(temperature=22.3, created_at=datetime.datetime.now().time()).save()
#     return HttpResponse("Все получилось!")
#
#
# def create_sensor(request):
#     measurements = Measurement.objects.all()
#     for measurement in measurements:
#         Sensor.objects.create(name="ESP32", description="Перенес датчик на балкон", measurement=measurement)
#     return HttpResponse("Все получилось!")


class DemoView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        Measurement(temperature=22.3, created_at=datetime.datetime.now().time()).save()
        measurements = Measurement.objects.all()
        for measurement in measurements:
            Sensor.objects.create(name="ESP32", description="Перенес датчик на балкон", measurement=measurement)
        return Response("Все получилось!")


class SensorView(CreateAPIView):
    # queryset = Measurement.objects.all()
    # serializer_class = MeasurementSerializer

    def post(self, request):
        Measurement(temperature=35.3, created_at=datetime.datetime.now().time()).save()


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, description):
        Sensor.objects.filter(description=description).update(descr="Перенес датчик на кухню")

