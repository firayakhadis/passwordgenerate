import random
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
symbol = "()[]{}@!?€%&/`´^¨'_-:.;,"

ans = upper_case + lower_case + num + symbol

length = 9
password = "".join(random.sample(ans, length))
print("Generate password is", password)
