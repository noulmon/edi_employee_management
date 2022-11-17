from rest_framework import serializers

from work.models import WorkArrangement, EmployeeWorkArrangement


class WorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArrangement
        exclude = ['date_added', 'date_modified']


def validate_total_work_percentage(employee, percentage):
    """returns true if the total assigned work percentage of an employee is lees than 100, else false"""
    total_percentage = employee.get_total_employee_work_percentage()
    if total_percentage + percentage > 100:
        return False
    return True


def validate_work_type_with_work_percentage(work_type, percentage):
    if work_type == 'FT':
        if percentage != 100:
            return True
    return False


class EmployeeWorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeWorkArrangement
        exclude = ['date_added', 'date_modified']

    def create(self, validated_data):
        """creates an EmployeeWorkArrangement object"""
        employee = validated_data['employee']
        percentage = validated_data['percentage']
        work_arrangement = validated_data['work_arrangement']
        if validate_work_type_with_work_percentage(work_type=work_arrangement.work_type, percentage=percentage):
            raise serializers.ValidationError(
                'Error: A full time work arrangement should always have 100% work percentage.')
        if not validate_total_work_percentage(employee, percentage):
            # validates if the total employee work percentage is less than 100
            raise serializers.ValidationError('Error: No employee can have total work percentage greater than 100')
        return self.Meta.model.active_objects.create(**validated_data)

    def update(self, instance, validated_data):
        """updates an existing EmployeeWorkArrangement instance"""
        percentage = validated_data.get('percentage')
        employee = instance.employee
        # if the update data includes the employee
        payload_employee = validated_data.get('employee')
        if payload_employee:
            employee = payload_employee
        # if
        work_arrangement = validated_data.get('work_arrangement')
        if not work_arrangement:
            work_arrangement = instance.work_arrangement

        if validate_work_type_with_work_percentage(work_type=work_arrangement.work_type, percentage=percentage):
            raise serializers.ValidationError(
                'Error: A full time work arrangement should always have 100% work percentage.')
        if percentage:
            # validates if the total employee work percentage is less than 100
            if not validate_total_work_percentage(employee, percentage):
                raise serializers.ValidationError('Error: No employee can have total work percentage greater than 100')
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
