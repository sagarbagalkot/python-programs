print("U15IG22S0054")
import re
dob=input("enter your date of birth")
if re.match(r"^\d{2,2}\-\d{2,2}\-\d{4,4}$",dob):
    print(f"{dob} is valid date of birth")
else:
    print(f"{dob} is not valid date of birth \n please enter valid date of birth like a dd-mm-yyyy")    