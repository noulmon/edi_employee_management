from decimal import Decimal

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.test import TestCase

from employee.models import Employee
from work.models import WorkArrangement, EmployeeWorkArrangement


class TestWorkArrangementModel(TestCase):
    """Testing WorkArrangement Model"""

    def setUp(self):
        """
        Creating a default work arrangement for comparison
        """
        self.work_arrangement = WorkArrangement.objects.create(work="DATA ANALYSIS", work_type='PT')

    def test_work_arrangement_instance(self):
        """
        Testing WorkArrangement instance creation
        """
        self.assertTrue(isinstance(self.work_arrangement, WorkArrangement))

    def test_default_work_type(self):
        """
        Testing default work_type = FT
        """
        self.assertTrue(self.work_arrangement.work_type, WorkArrangement.FULL_TIME)

    def test_unique_together(self):
        """
        Testing unique togetherness of work and work_type
        """
        with self.assertRaises(IntegrityError):
            WorkArrangement.objects.create(work="DATA ANALYSIS", work_type='FT')
            WorkArrangement.objects.create(work="DATA ANALYSIS", work_type='FT')

    def test_create_a_unique_instance(self):
        """
        Testing a unique instance creation
        """
        work_arrangement_new = WorkArrangement.objects.create(work="APP TESTING", work_type='FT')
        self.assertTrue(isinstance(work_arrangement_new, WorkArrangement))
        self.assertNotEqual(work_arrangement_new.work, self.work_arrangement.work)
        self.assertNotEqual(work_arrangement_new.work_type, self.work_arrangement.work_type)


class TestEmployeeWorkArrangementModel(TestCase):
    def setUp(self):
        """
        Creating a default work arrangement for comparison
        """
        self.employee = Employee.objects.create(employee_name="HUGO", hourly_rate=Decimal(200))
        self.work_arrangement = WorkArrangement.objects.create(work="DATA ANALYSIS", work_type='PT')
        self.percentage = Decimal(50)
        self.emp_work_arrangement = EmployeeWorkArrangement.objects.create(employee=self.employee,
                                                                           work_arrangement=self.work_arrangement,
                                                                           percentage=self.percentage)

    def test_emp_work_arrangement_instance_creation(self):
        """
        Testing instance creation
        """
        self.assertTrue(isinstance(self.emp_work_arrangement, EmployeeWorkArrangement))

    def test_invalid_employee(self):
        """
        Testing invalid Employee FK
        """
        with self.assertRaises(ObjectDoesNotExist):
            self.emp_work_arrangement = EmployeeWorkArrangement.objects.create(employee_id=3,
                                                                               work_arrangement=self.work_arrangement,
                                                                               percentage=self.percentage)

    def test_invalid_work_arrangement(self):
        """
        Testing invalid WorkArrangement FK
        """
        with self.assertRaises(IntegrityError):
            self.emp_work_arrangement = EmployeeWorkArrangement.objects.create(employee=self.employee,
                                                                               percentage=self.percentage)

    def test_invalid_percentage(self):
        """
        Testing invalid work percentage. Percentage greater than 100 will throw ValidationError.
        """
        with self.assertRaises(ValidationError):
            self.emp_work_arrangement = EmployeeWorkArrangement.objects.create(employee=self.employee,
                                                                               work_arrangement=self.work_arrangement,
                                                                               percentage=Decimal(105))

    def test_invalid_total_work_arrangements(self):
        """
        Testing total work percentage of an employee. Total work percentage > 100 will throw ValidationError
        """
        with self.assertRaises(ValidationError):
            EmployeeWorkArrangement.objects.create(employee=self.employee,
                                                   work_arrangement=self.work_arrangement,
                                                   percentage=Decimal(60))
