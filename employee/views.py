from rest_framework import generics

from employee.models import Employee, Team, TeamLeader
from employee.serializers import EmployeeSerializer, EmployeeReadSerializer, TeamSerializer, TeamLeaderSerializer


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


class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamLeaderListCreateView(generics.ListCreateAPIView):
    queryset = TeamLeader.objects.all()
    serializer_class = TeamLeaderSerializer


class TeamLeaderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamLeader.objects.all()
    serializer_class = TeamLeaderSerializer
