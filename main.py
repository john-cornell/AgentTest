from agents.prompt_expander_agent import prompt_expander_agent
from agents.question_agent import question_agent
from agents.summary_agent import summary_agent
import json
import sys
import time
import re

def main(prompt):         
	print("\n")   
	
	
	pea = prompt_expander_agent()
	qa = question_agent(prompt)
	sa = summary_agent(prompt)
 
	response = pea.call(prompt)		

	response = response.replace('\n', '').replace('\t', '')
	json_response = None
	loaded_prompts = []
	loaded_answers = []
	try:
		json_response = json.loads(response)
		print("Loaded response")
	except:
		print(f"Error handling response: \n{response}")

	try:
		prompts = json_response['prompts']

		# Loop over each prompt object in the array
		for prompt_obj in prompts:
			# Get the first key in the prompt_obj dictionary
			label = list(prompt_obj.keys())[0]
			
			# Access the value using the retrieved label
			prompt = prompt_obj[label]
			print(f"Question: {prompt}")
			answer = qa.call(prompt)
			print(f"Answer: {answer}")
			
			loaded_prompts.append(prompt)
			loaded_answers.append(f"{answer}")
   
		print("Loaded expanded prompts")
	except:
		print(f"Error handling response prompt: \n{json_response['prompts']}")

	print(f"ANSWER: {sa.summarise(loaded_answers)}")

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        main("Explain quantum physics")
    else:
    	main(sys.argv[1])