from rest_framework import serializers

from work.models import WorkArrangement


class WorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArrangement
        exclude = ['date_added', 'date_modified']
