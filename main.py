import random
pass_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# int, str
pass_length = int(input("Podaj proszę długość hasła: ")) # 8
generated_password = ''
for i in range(pass_length): # 0, 1, 2, 3, 4, 5, 6, 7
    generated_password = generated_password + random.choice(pass_characters)
print(generated_password)
