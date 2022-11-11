from rest_framework import generics

from work.models import WorkArrangement
from work.serializers import WorkArrangementSerializer


class WorkArrangementListCreateView(generics.ListCreateAPIView):
    queryset = WorkArrangement.objects.all()
    serializer_class = WorkArrangementSerializer


class WorkArrangementRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkArrangement.objects.all()
    serializer_class = WorkArrangementSerializer
