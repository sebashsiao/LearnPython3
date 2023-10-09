# Project 003: MAGIC 8-BALL

import random

name = "Linus"
question = "Will I win the lottery this summer?"
answer = ""
# random number generator (1-9)
rn = random.randint(1,9)

# Print random (Magic Ball-8 logic)
if rn == 1 :
  answer = "Yes - definitely"
elif rn == 2:
  answer = "It is decidedly so"
elif rn == 3:
  answer = "Without a doubt"
elif rn == 4:
  answer = "Reply hazy, try again"
elif rn == 5:
  answer = "Ask again later"
elif rn == 6:
  answer = "Better not tell you now"
elif rn == 7:
  answer = "My sources say no"
elif rn == 8:
  answer = "Outlook not so good"
elif rn == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

# Print Answer
print(f'{name} is asking: {question}')
print(f'Shaking Magic 8-Ball... \nThe answer is \"{answer}\"')