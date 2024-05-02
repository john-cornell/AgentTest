from .agent import agent

from typing import List
system_prompt="""<TASK>You are an expert in answering the user-question '{0}', a world renowned number one at it. 
Answer helpfully, intelligently and indepth. You are the best hope at answer this, do your utmost best!
	<RULES>
		<RULE_1>You will be given some information relevant to the user-question given to you, above</RULE_1>
		<RULE_2>Answer the user-question with the context of the information provided in this information</RULE_2>
		<RULE_3>Answer in plain text</RULE_3>	
		<RULE_4>ANSWER THE user question rather than simply repeating the information given you verbatim</RULE_4>
		<RULE_5>ENSURE TO ACTUALLY ANSWER THE QUESTION RATHER THAN REGURITATE THE INFORMATION. 
			<RULE_5_1>THE ANSWER TO THE QUESTION IS THE MOST IMPORTANT THING HERE</RULE_5_1>
  		</RULE_5>
	</RULES>
</TASK>"""

class summary_agent(agent):
	def __init__(self, query, format='') -> None:
		super().__init__(system_prompt.format(query), format)
		self._format = format
		self._query = query
  
	def summarise(self, information : List[str]):
		prompt = f"Please CONCISELY ANSWER the user-question '{self._query}' based on the following information: "
		for i, qa in enumerate(information, start=1):
			prompt += f"{qa}\n"
   
		prompt += "\nThink step by step and ENSURE TO ACTUALLY ANSWER THE user-question"
		return super().call(prompt)