from django.urls import path

from measurement.views import SensorsView, MeasurementView, SensorViewUpdate

urlpatterns = [
    path('sensors', SensorsView.as_view(), name='Новый датчик'),
    path('sensors/<int:pk>', SensorViewUpdate.as_view(), name='Изменить датчик'),
    path('measurement', MeasurementView.as_view(), name='Измерения'),
]
