import datetime

user_input = input("Enter yout goal with a deadline separated by colon, for example: learn pyhton:20.12.2023\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today = datetime.datetime.today()
time_till = deadline_date - today

print(f'Time remaining for your goal {goal} is : {time_till}')