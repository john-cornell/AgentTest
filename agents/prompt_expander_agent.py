from .agent import agent

system_prompt = """<TASK>
	Your task is to take a user query and break it down into a set of further prompts that may better answer the user's initial Prompt. 
 	<RULES>
  		<RULE_1>DO NOT ANSWER TO PROMPT, JUST CREATE DEEPER PROMPTS</RULE_1>
    	<RULE_2>Answer in the form of JSON with a single element, 'prompts'
     	<RULE_3>Inside the single prompts element, contain a Json list of crafted prompts</RULE_2>
		<RULE_4>Prompts must be relevant to user's queries and address a comprehensive set of topics pertinent to the user's initial query</RULE_4>		
    </RULES>
</TASK>"""

class prompt_expander_agent(agent):
	def __init__(self, format='json') -> None:
		super().__init__(system_prompt, format)
  
	def get_expanded_prompts(self, prompt):
		user_prompt = f"As per your instructions, expand on the query {prompt}"
		return super().call(user_prompt)