from rest_framework import serializers

from work.models import WorkArrangement, EmployeeWorkArrangement


class WorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArrangement
        exclude = ['date_added', 'date_modified']


def validate_total_work_percentage(employee, percentage):
    per = employee.get_total_employee_work_percentage()
    if per + percentage > 100:
        return False
    return True


class EmployeeWorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeWorkArrangement
        exclude = ['date_added', 'date_modified']

    def create(self, validated_data):
        employee = validated_data['employee']
        percentage = validated_data['percentage']
        if not validate_total_work_percentage(employee, percentage):
            raise serializers.ValidationError('Error: No employee can have total work percentage greater than 100')
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        percentage = validated_data.get('percentage')
        employee = instance.employee
        # if the update data includes the employee
        payload_employee = validated_data.get('employee')
        if validated_data.get('percentage'):
            employee = payload_employee
        if percentage:
            if not validate_total_work_percentage(employee, percentage):
                raise serializers.ValidationError('Error: No employee can have total work percentage greater than 100')
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
