import random
import string

mdp = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
print("Your password :", mdp)