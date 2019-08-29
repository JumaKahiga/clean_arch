from clean_arch.workers.entities.employee import Employee
from clean_arch.workers.usecases.interfaces import (
	EmployeeRepositoryInterface, UseCaseInterface)


class CreateEmployee(UseCaseInterface):
	def __init__(
		self,
		repository=EmployeeRepositoryInterface,
		first_name: str,
		last_name: str,
		email: str,
		age: int,
		department: str,
		supervisor: str,
		is_active: bool,
		is_available: bool)

		self.__first_name = first_name
		self.__last_name = last_name
		self.email = email
		self.__age = age
		self.__department = department
		self.__supervisor = supervisor
		self.__is_active = is_active
		self.__is_available = is_available
		self.__repository = repository

		@property
		def repository(self) -> EmployeeRepositoryInterface:
			return self.__repository

		def execute(self) -> Employee:
			if self.__repository.find(self.email):
				raise Exception('Employee already exists')

			employee = self._factory_employee()
			return self.__repository.create(employee)

		def _factory_employee(self) -> Employee:
			instance = Employee(self.__first_name, self.__last_name, ...)
			return instance
