from agents.prompt_expander_agent import prompt_expander_agent
from agents.question_agent import question_agent
from agents.summary_agent import summary_agent
import json
import sys
import time
import re

def main(prompt, verbose : bool):         
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
		if (verbose):
			print("Loaded response")
		else:
			print(".", end="", flush=True)
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
   
			if (verbose): 
				print(f"Question: {prompt}")
			else:
				print(".", end="", flush=True)
			answer = qa.call(prompt)
			if (verbose):
				print(f"Answer: {answer}")
			else:
				print(".", end="", flush=True)
			loaded_prompts.append(prompt)
			loaded_answers.append(f"{answer}")
   
		if (verbose):	
			print("Loaded expanded prompts")
		else:
				print(".", end="", flush=True)
	except:
		print(f"Error handling response prompt: \n{json_response['prompts']}")

	print(f"ANSWER: {sa.summarise(loaded_answers)}")

if __name__ == "__main__":
    
    verbose = False
    prompt = "Explain quantum physics"
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "-v":
            verbose = True
            if len(sys.argv) > 2:
                prompt = sys.argv[2]
        else:
            prompt = sys.argv[1]
            if len(sys.argv) > 2 and sys.argv[2] == "-v":
                verbose = True
    main(prompt, verbose=verbose)
	