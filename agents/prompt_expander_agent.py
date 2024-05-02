from .agent import agent

system_prompt = """<|start_task|>
	Your task is to take a user query and break it down into a set of further prompts that may better answer the user's initial Prompt. 
 	<|start_rules|>
  		<|Start_RULE_1|>DO NOT ANSWER TO PROMPT, JUST CREATE DEEPER PROMPTS<|End_RULE_1|>
    	<|Start_RULE_2|>Answer in the form of JSON with a single element, 'prompts'<|End_RULE_2|>
     	<|Start_RULE_3|>Inside the single prompts element, contain a Json list of crafted prompts<|End_RULE_3|>
		<|Start_RULE_4|>Prompts must be relevant to user's queries and address a comprehensive set of topics pertinent to the user's initial query<|End_RULE_4|>
    <|end_rules|>
<|end_task|>"""

class prompt_expander_agent(agent):
	def __init__(self, format='json') -> None:
		super().__init__(system_prompt, format)
  
	def get_expanded_prompts(self, prompt):
		user_prompt = f"As per your instructions, expand on the query {prompt}"
		return super().call(user_prompt)