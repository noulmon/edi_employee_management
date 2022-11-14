from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.models import DatedModel, StatusModel
from employee.utils import MAX_WEEKLY_WORKING_HOURS, WEEKS_IN_A_MONTH, EMPLOYEE_CODE_CONST, TEAM_CODE_CONST


# team model
class Team(DatedModel, StatusModel):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.code})'


@receiver(post_save, sender=Team)
def generate_team_code(sender, instance, created, **kwargs):
    """
    post_save signal that generates team code when a Team instance is created
    """
    if created:
        instance.code = f'{TEAM_CODE_CONST}{instance.id}'
        instance.save()


# employee model
class Employee(DatedModel, StatusModel):
    employee_name = models.CharField(max_length=20, unique=True, blank=False, null=False)
    employee_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    hourly_rate = models.DecimalField(blank=False, null=False, max_digits=30, decimal_places=2)

    def get_total_employee_work_percentage(self):
        """
        total percentage of work an employee is doing
        """
        total_work_arrangement_percentage = Decimal(0)
        work_arrangements = self.employeeworkarrangement_set.all()
        if work_arrangements:
            total_work_arrangement_percentage = work_arrangements.aggregate(Sum("percentage"))['percentage__sum']
        return total_work_arrangement_percentage

    def is_team_leader(self):
        """
        Returns True if an employee is team leader, else returns false
        """
        try:
            team_leader = self.teamleader
            if team_leader:
                return True
        except Exception as e:
            return False

    def get_monthly_pay(self):
        """
        Returns total amount to be paid to the employee
        """
        monthly_pay = Decimal(0)
        work_percentage = self.get_total_employee_work_percentage()
        if not work_percentage:
            work_percentage = Decimal(0)
        monthly_pay = (work_percentage / 100) * MAX_WEEKLY_WORKING_HOURS * WEEKS_IN_A_MONTH * self.hourly_rate
        if self.is_team_leader():
            monthly_pay += (monthly_pay / 10)
        return monthly_pay

    def __str__(self):
        return f'{self.employee_name} {self.employee_id}'


@receiver(post_save, sender=Employee)
def generate_employee_id(sender, instance, created, **kwargs):
    """
    post_save signal that generates employee id when an Employee instance is created
    """
    if created:
        instance.employee_id = f'{EMPLOYEE_CODE_CONST}{instance.id}'
        instance.save()


# team leader model
class TeamLeader(DatedModel, StatusModel):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.team.name} - {self.employee.employee_name}'
