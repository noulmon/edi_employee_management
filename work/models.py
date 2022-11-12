from django.core.validators import MaxValueValidator, ValidationError
from django.db import models
from django.db.models import Sum

from base.models import DatedModel, StatusModel
from employee.models import Employee


# Work Arrangement Model
class WorkArrangement(DatedModel, StatusModel):
    PART_TIME = 'PT'
    FULL_TIME = 'FT'
    WORK_TYPE = (
        (PART_TIME, 'PART TIME'),
        (FULL_TIME, 'FULL TIME'),
    )
    work = models.CharField(max_length=25, blank=False)
    work_type = models.CharField(max_length=25, blank=False, null=False, choices=WORK_TYPE, default=FULL_TIME)

    class Meta:
        unique_together = ('work', 'work_type',)

    def save(self, *args, **kwargs):
        work_types = [self.PART_TIME, self.FULL_TIME]
        if self.work_type not in work_types:
            raise ValidationError(f'Error: work_type should be an element of {work_types}')
        super(WorkArrangement, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.work} - {self.work_type}'


# Employee Work Arrangement
class EmployeeWorkArrangement(DatedModel, StatusModel):
    employee = models.ForeignKey(Employee, null=False, on_delete=models.CASCADE)
    work_arrangement = models.ForeignKey(WorkArrangement, null=False, on_delete=models.CASCADE)
    percentage = models.DecimalField(null=False, max_digits=10, decimal_places=2, validators=[MaxValueValidator(100)])

    def get_total_employee_work_percentage(self):
        """
        Returns total work arrangement percentage of an employee
        """
        return self.employee.employeeworkarrangement_set.all().aggregate(Sum("percentage"))['percentage__sum']

    def save(self, *args, **kwargs):
        if self.percentage > 100:
            raise ValidationError('Error: Percentage should not be greater than 100')

        if EmployeeWorkArrangement.objects.filter(employee=self.employee).exists():
            if self.get_total_employee_work_percentage() + self.percentage > 100:
                raise ValidationError('Error: No employee can have total work percentage greater than 100')
        super(EmployeeWorkArrangement, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.employee.employee_id} - {self.work_arrangement.work} ({self.percentage})'
