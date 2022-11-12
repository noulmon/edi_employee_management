from rest_framework import generics

from work.models import WorkArrangement, EmployeeWorkArrangement
from work.serializers import WorkArrangementSerializer, EmployeeWorkArrangementSerializer


class WorkArrangementListCreateView(generics.ListCreateAPIView):
    queryset = WorkArrangement.objects.all()
    serializer_class = WorkArrangementSerializer


class WorkArrangementRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkArrangement.objects.all()
    serializer_class = WorkArrangementSerializer


class EmployeeWorkArrangementListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeWorkArrangement.objects.all()
    serializer_class = EmployeeWorkArrangementSerializer


class EmployeeWorkArrangementRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeWorkArrangement.objects.all()
    serializer_class = EmployeeWorkArrangementSerializer
