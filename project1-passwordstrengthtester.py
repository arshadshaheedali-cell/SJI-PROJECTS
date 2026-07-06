# #PASSWORD STRENGTH CHECKER


def check_password_strength(password):
   score = 0
   feedback = []


   # #step 1/ Check if password is 8 characters or more
   if len(password) >= 8:
       score += 1
   else:
       feedback.append("Make it at least 8 characters long.")


   # #step 2 / Check for numbers
   has_number = False
   for char in password:
       if char.isdigit():
           has_number = True
           break


   if has_number:
       score += 1
   else:
       feedback.append("Add at least one number (0-9).")


   # #step 3 / Check for Symbols
   has_special = False
   for char in password:
       if char in "!@#$%^&*":
           has_special = True
           break


   if has_special:
       score += 1
   else:
       feedback.append("Add a special character (like !, @, #, $).")


   # #check final score
   if score == 3:
       return "STRONG", []
   elif score == 2:
       return "MEDIUM", feedback
   else:
       return "WEAK", feedback




# #front end
print("--- Password Strength Validator ---")
user_input = input("Enter a password to test: ")


strength, suggestions = check_password_strength(user_input)


print(f"\nPassword Strength: {strength}")
if suggestions:
   print("Suggestions to improve:")
   for tip in suggestions:
       print(f"- {tip}")






# #conditions to be met:
# # -password is to be 8 or more characters in length
# # -the password must contain one or more number
# # - it must contain one special character from "!@#$%^&*"
# #Made by Arshad Shaheed Ali, St Hildas Primary School


