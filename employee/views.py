from rest_framework import generics

from employee.models import Employee
from employee.serializers import EmployeeSerializer, EmployeeReadSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        serializer = EmployeeSerializer
        if self.request.method == 'GET':
            serializer = EmployeeReadSerializer
        return serializer


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        serializer = EmployeeSerializer
        if self.request.method == 'GET':
            serializer = EmployeeReadSerializer
        return serializer
