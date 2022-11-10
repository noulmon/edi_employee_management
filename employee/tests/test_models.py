from decimal import Decimal

from django.db.utils import IntegrityError
from django.test import TestCase

from employee.models import Team, Employee, TeamLeader


class TeamModelTest(TestCase):
    """Testing Team Model"""

    def setUp(self):
        """
        Creating a default team for comparison
        """
        self.team = Team.objects.create(name="ENGINEERING")

    def test_team_instance_creation(self):
        """
        Testing if the created team is an instance of Team model
        """
        self.assertTrue(isinstance(self.team, Team))

    def test_team_code_signal(self):
        """
        Testing if the team code generated via signal is correct
        """
        self.assertEqual(self.team.code, 'EDI-TM-1')

    def test_team_name_uniqueness(self):
        """
        Testing if the team name hold unique constraint
        """
        with self.assertRaises(IntegrityError):
            Team.objects.create(name="ENGINEERING")

    def test_team_code_uniqueness(self):
        """
        Testing if the team code generated via signal are unique
        """
        qa_team = Team.objects.create(name="QUALITY")
        self.assertNotEqual(self.team.code, qa_team.code)


class EmployeeModelTest(TestCase):
    """Testing Employee Model"""

    def setUp(self):
        """
        Creating a default employee for comparison
        """
        self.employee = Employee.objects.create(employee_name="HUGO", hourly_rate=Decimal(200))

    def test_employee_instance_creation(self):
        """
        Testing if the created employee is an instance of Employee model
        """
        self.assertTrue(isinstance(self.employee, Employee))

    def test_employee_id_signal(self):
        """
        Testing if the employee code generated via signal is correct
        """
        self.assertEqual(self.employee.employee_id, 'EDI-EMP-1')

    def test_employee_name_uniqueness(self):
        """
        Testing if the employee name hold unique constraint
        """
        with self.assertRaises(IntegrityError):
            Employee.objects.create(employee_name="HUGO", hourly_rate=Decimal(200))

    def test_hourly_rate(self):
        """
        Testing mandatory parameter hourly_rate
        """
        with self.assertRaises(IntegrityError):
            Employee.objects.create(employee_name="SAM")

    def test_employee_id_uniqueness(self):
        """
        Testing if the employee_id generated via signal are unique
        """
        new_employee = Employee.objects.create(employee_name="Hobbo", hourly_rate=Decimal(200))
        self.assertNotEqual(self.employee.employee_id, new_employee.employee_id)


class TeamLeaderTest(TestCase):
    """Testing TeamLeader model"""

    def setUp(self):
        """Setting initial data for comparison"""
        self.team = Team.objects.create(name="ENGINEERING")
        self.employee = Employee.objects.create(employee_name="HUGO", hourly_rate=Decimal(200))
        self.team_leader = TeamLeader.objects.create(team=self.team, employee=self.employee)

    def test_team_lead_instance_creation(self):
        """Testing is the initial creation is successful"""
        self.assertTrue(isinstance(self.team_leader, TeamLeader))

    def test_one_to_one_field_team(self):
        """Testing if the duplicate team can be inserted into the table"""
        employee = Employee.objects.create(employee_name="SAMUEL", hourly_rate=Decimal(200))
        with self.assertRaises(IntegrityError):
            TeamLeader.objects.create(team=self.team, employee=employee)

    def test_one_to_one_field_employee(self):
        """Testing if the duplicate employee can be inserted into the table"""
        team = Team.objects.create(name="QA")
        with self.assertRaises(IntegrityError):
            TeamLeader.objects.create(team=team, employee=self.employee)
