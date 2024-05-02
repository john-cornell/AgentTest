from phi3 import phi3

from abc import ABC, abstractmethod

class agent(ABC):
	@abstractmethod
	def __init__(self, system_prompt, format='') -> None:
		self._client = phi3(format)
		self._client.connect()
		self._client.set_system_prompt(system_prompt=system_prompt)
  
	def call(self, prompt):
		return self._client.call(prompt=prompt)