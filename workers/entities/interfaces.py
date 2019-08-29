import abc


class EmployeeInterface(metaclass=abc.ABCMeta):

	@abc.abstractproperty
	def first_name(self) -> str:
		pass

	@abc.abstractproperty
	def last_name(self) -> str:
		pass

	@abc.abstractproperty
	def email(self) -> str:
		pass

	@abc.abstractproperty
	def age(self) -> int:
		pass

	@abc.abstractproperty
	def department(self) -> str:
		pass

	@abc.abstractproperty
	def supervisor(self) -> str:
		pass

	@abc.abstractproperty
	def is_active(self) -> bool:
		pass

	@abc.abstractproperty
	def is_available(self) -> bool:
		pass

	@abc.abstractmethod
	def set_not_available(self, supervisor: str, value: bool):
		pass

