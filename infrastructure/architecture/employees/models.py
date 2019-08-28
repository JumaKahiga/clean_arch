from django.db import models

# Create your models here.

class Employee(models.Model):
	OPS, HR, SALES, IT, TECH = 'Ops', 'HR', 'Sales', 'IT', 'Tech'

	DEPARTMENTS = [
	(OPS, 'Operations'),
	(HR, 'Human Resource'),
	(SALES, 'Sales'),
	(IT, 'IT'),
	(TECH, 'Technology')]

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	age = models.PositiveIntegerField()
	department = models.CharField(
		choices=DEPARTMENTS, max_length=20, default=OPS)
	supervisor = models.ForeignKey(
		'self', on_delete=models.SET_NULL, null=True)
	is_active = models.BooleanField(default=False)
	is_available = models.BooleanField(default=False)

	class Meta:
		constraints = [
		models.CheckConstraint(
			check=models.Q(
				age__gte=18) | models.Q(age__gte=70), name='invalid age')]

	def save(self, *args, **kwargs):
		self.clean_fields()
		super().save(*args, **kwargs)
