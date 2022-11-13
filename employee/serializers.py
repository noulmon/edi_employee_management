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


class EmployeeMonthlyPaymentSerializer(serializers.ModelSerializer):
    works = serializers.SerializerMethodField()
    monthly_pay = serializers.SerializerMethodField(source='get_monthly_pay')
    is_team_leader_data = serializers.SerializerMethodField()

    class Meta(EmployeeSerializer.Meta):
        pass

    def get_works(self, instance):
        """return the work arrangement details of an employee"""
        return instance.employeeworkarrangement_set.all().values('work_arrangement__work',
                                                                 'work_arrangement__work_type', 'percentage')

    def get_monthly_pay(self, instance):
        """Return total amount payable to an employee in a month"""
        return instance.get_monthly_pay()

    def get_is_team_leader_data(self, instance):
        """Returns whether an employee is team leader or not"""
        return instance.is_team_leader()
