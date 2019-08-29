import abc
from clean_arch.workers.entities.interfaces import EmployeeInterface

class EmployeeRepositoryInterface(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def find(self, email: 'email') -> EmployeeInterface:
		pass


class UseCaseInterface(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def execute(self):
		pass