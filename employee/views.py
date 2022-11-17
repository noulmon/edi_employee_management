from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from employee.models import Employee, Team, TeamLeader
from employee.serializers import EmployeeSerializer, EmployeeReadSerializer, TeamSerializer, TeamLeaderSerializer, \
    EmployeeMonthlyPaymentSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.active_objects.all()

    def get_serializer_class(self):
        serializer = EmployeeSerializer
        if self.request.method == 'GET':
            serializer = EmployeeReadSerializer
        return serializer


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.active_objects.all()

    def get_serializer_class(self):
        serializer = EmployeeSerializer
        if self.request.method == 'GET':
            serializer = EmployeeReadSerializer
        return serializer


class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.active_objects.all()
    serializer_class = TeamSerializer


class TeamRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.active_objects.all()
    serializer_class = TeamSerializer


class TeamLeaderListCreateView(generics.ListCreateAPIView):
    queryset = TeamLeader.active_objects.all()
    serializer_class = TeamLeaderSerializer


class TeamLeaderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamLeader.active_objects.all()
    serializer_class = TeamLeaderSerializer


class EmployeeMonthlyPaymentList(APIView):
    def get(self, request):
        """Returns all the employee list with total amount payable at the end of a month"""
        employees = Employee.active_objects.all()
        serializer = EmployeeMonthlyPaymentSerializer(employees, many=True)
        return Response(serializer.data)
