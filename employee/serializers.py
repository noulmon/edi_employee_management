from rest_framework import serializers

from employee.models import Employee, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ['date_added', 'date_modified']


class EmployeeSerializer(serializers.ModelSerializer):
    # team_details = TeamSerializer()

    class Meta:
        model = Employee
        exclude = ['date_added', 'date_modified']


class EmployeeReadSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta(EmployeeSerializer.Meta):
        pass
