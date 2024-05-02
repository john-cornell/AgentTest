from ollama import Client

class phi3:
	def __init__(self, format='', address="http://localhost", port=11434) -> None:
		self._connected = False
		self._client = None
		self._address = address
		self._port = port
		self._history = []
		self._format = format
  
	def connect(self):		
		self._client = Client(host=f'{self._address}:{self._port}')
		self._connected = True
  		
	def call(self, prompt):
		if not self._connected:
			raise Exception("Please connect to PHI3 before calling")
		
		self._history.append( {'role': 'user', 'content': prompt} );
		phi3response = self._client.chat(
    		model="phi3",
    		messages=self._history,
      		format=self._format
		)
  
		response = phi3response['message']
  
		self._history.append(response)
		return response['content'].strip()

	def set_format(self, format):
		self._format = format

	def set_system_prompt(self, system_prompt):
		self.reset(system_prompt)
     
	def reset(self, system_prompt = None):
		self._history = []
		if (system_prompt != None):
			self._history.append( {'role': 'system', 'content': system_prompt} );
   