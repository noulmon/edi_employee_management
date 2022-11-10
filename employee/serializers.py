from rest_framework import serializers

from employee.models import Employee, Team, TeamLeader


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ['date_added', 'date_modified']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['date_added', 'date_modified']


class EmployeeReadSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta(EmployeeSerializer.Meta):
        pass


class TeamLeaderSerializer(serializers.ModelSerializer):
    employee_data = EmployeeSerializer(source='employee', read_only=True)
    team_data = TeamSerializer(source='team', read_only=True)

    class Meta:
        model = TeamLeader
        exclude = ['date_added', 'date_modified']
