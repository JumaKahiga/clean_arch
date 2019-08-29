from interfaces import EmployeeInterface

class Employee(EmployeeInterface):
	def __init__(
		self,
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

	@property
	def first_name(self) -> str:
		return self.__first_name

	@property
	def last_name(self) -> str:
		return self.__last_name
