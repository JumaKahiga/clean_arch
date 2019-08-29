from clean_arch.infrastructure.employees.models import Employee
from clean_arch.workers.entities.interfaces import EmployeeInterface
from clean_arch.workers.usecases.interfaces import(
	EmployeeRepositoryInterface, UseCaseinterface)

class DjangoEmployeeRepository(EmployeeRepositoryInterface):

	def find(self, email: 'email') -> EmployeeInterface:
		pass