length = int(input( "Enter the desired password length: "))
import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all_chars = lower + upper + digits + symbols
password = "".join(random.sample(all_chars, length))
print("Generated password: ", password)
