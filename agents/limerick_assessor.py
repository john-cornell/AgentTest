from .agent import agent

from typing import List
import json

system_prompt = """You are a master at assessing limericks, it gives you no end of joy.

RULES OF A LIMERICK:
1) Limerick poems are poems that follow the rhyming pattern of AABBA. 
	1.1) Each letter in that rhyming pattern (AABBA) represents a line of the poem. 
	1.2) The lines that are represented by the same letter (either A or B, AABBA) end with words that rhyme with each other.
2) Additionally, limerick poems follow a specific syllable count. 
	2.1) There can are strictly 8-9 syllables in the first, second, and fifth lines 
 	2.2) There can only be 5 syllables in the third and fourth lines. In order to count syllables, you need to count how many different sounds are in the line. 
  	2.3) Remember, the syllable count is not always the same as how many words you may have in the line. The easiest way to count syllables is to say each line out loud and count how many sounds it takes you to speak the words. 	

For example:
It's gravity, Newton, he said 
When an apple fell down on his head
But what a dismay
On that famous day
If a brick fell on him instead.

Task: It is your task assess the best of the limericks past to you 
Rules: 
	1) Only one single limerick may be chosen, and no extra commentary. 
 	2) Reply strictly in JSON
	3) Use two elements in your reply
     	3.1) The limerick itself, label: limerick
		3.2) Justification for chosing that limerick, label: justification
	4) You must chose based on:
		4.1) Relevance to initial_prompt
		4.2) Correct rhyming pattern
		4.3) Correct syllable count for the relevant line 
"""

class limerick_assessor(agent):
    def __init__(self):
        super().__init__(system_prompt, format='json')

    def assess(self, initial_prompt: str, limericks: List[str]):
        data = {
            "initial_prompt": initial_prompt,
            "limericks": limericks
        }
        prompt = json.dumps(data, indent=2)

        return super().call(prompt)
