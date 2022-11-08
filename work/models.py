from django.db import models
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
    work = models.CharField(max_length=25, unique=True, blank=False)
    work_type = models.CharField(max_length=25, blank=False, null=False, choices=WORK_TYPE, default=FULL_TIME)

    def __str__(self):
        return f'{self.work} - {self.work_type}'


# Employee Work Arrangement
class EmployeeWorkArrangement(DatedModel, StatusModel):
    employee = models.ForeignKey(Employee, null=False, on_delete=models.CASCADE)
    work_arrangement = models.ForeignKey(WorkArrangement, null=False, on_delete=models.CASCADE)
    percentage = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.employee.employee_id} - {self.work_arrangement.work} ({self.percentage})'
