#gerenrating randorm password using python

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
sepecial_character = "!@#$%^&*|\/?<>.:;+=-_"

use_for = lower_case + upper_case + numbers + sepecial_character
len_for_pass = 12

password = "".join(random.sample(use_for, len_for_pass))

print("Your Generated Password :", password)