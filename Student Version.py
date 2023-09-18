# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953920
# Date: 12/14/2022
def take_input(credit1, credit2):
    while True:
        try:
            credit1 = int(input(f"Please enter your credits at {credit2}: "))
            if credit1 % 20 == 0 and 0 <= credit1 <= 120:
                break
            else:
                print("Out of range\n")
        except ValueError:
            print("Integer required\n")
    return credit1


while True:
    student_id = input("Enter Student ID: ")         #gets Student ID
    if len(student_id) == 0:
        print("Please enter Student ID\n")
        continue
    elif student_id.lower()[0] != "w" or len(student_id) != 8:          #check whether the ID is valid
        print("Student ID not valid. Please enter again.\neg:- w1234567\n")
        continue
    else:
        break
while True:
    Pass = take_input("P", "pass")           #gets Pass, Defer, Fail
    Defer = take_input("D", "defer")
    Fail = take_input("F", "fail")
    if Pass + Defer + Fail != 120:          #checks the total
        print("Total incorrect.\n")
        continue
    else:
        break
if Pass == 120:                       #outcomes
    print("Progress")
elif Pass == 100:
    print("Progress (module trailer)")
elif Pass <= 80 and Fail <= 60:
    print("Do not Progress – module retriever")
else:
    print("Exclude")
