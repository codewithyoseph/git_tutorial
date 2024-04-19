import random
import string

pwd_genx = "".join(random.choices(string.ascii_letters + string.digits, k=6))
print(pwd_genx)
