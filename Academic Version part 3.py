# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953920
# Date: 12/14/2022
Q = "y"
progress_count = 0
progress_trailer_count = 0
module_retriever_count = 0
exclude_count = 0
outcomes = 0
list_progress = []
list_trailer = []
list_retriever = []
list_exclude = []



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


while Q.lower() == "y":
    while True:
        student_id = input("Enter Student ID: ")
        if len(student_id) == 0:
            print("Please enter Student ID\n")
            continue
        elif student_id.lower()[0] != "w" or len(student_id) != 8:
            print("Student ID not valid. Please enter again.\neg:- w1234567\n")
            continue
        else:
            break
    while True:
        Pass = take_input("P", "pass")
        Defer = take_input("D", "defer")
        Fail = take_input("F", "fail")
        if Pass + Defer + Fail != 120:
            print("Total incorrect.\n")
            continue
        else:
            break
    if Pass == 120:
        print("Progress")
        progress_count += 1
        list_progress.append([Pass, Defer, Fail])
    elif Pass == 100:
        print("Progress (module trailer)")
        progress_trailer_count += 1
        list_trailer.append([Pass, Defer, Fail])
    elif Pass <= 80 and Fail <= 60:
        print("Do not Progress – module retriever")
        module_retriever_count += 1
        list_retriever.append([Pass, Defer, Fail])
    else:
        print("Exclude")
        exclude_count += 1
        list_exclude.append([Pass, Defer, Fail])
    print("")
    while True:
        Q = input(
            "Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        print("")
        if Q.lower() == "y" or Q.lower() == "q":
            break
        else:
            print("Wrong input")
            continue
print("-" * 60)
print("Histogram")
print("Progress", progress_count, "                          :", "*" * progress_count)
print("Progress(module trailer)", progress_trailer_count, "          :", "*" * progress_trailer_count)
print("Do not Progress – module retriever", module_retriever_count, ":", "*" * module_retriever_count)
print("Exclude", exclude_count, "                           :", "*" * exclude_count)
outcomes = int(progress_count) + int(progress_trailer_count) + int(module_retriever_count) + int(exclude_count)
print("")
if outcomes == 1:
    print(outcomes, "outcome in total.")
else:
    print(outcomes, "outcomes in total.")
print("-" * 60)
text_file = open("output data.txt", "w")
print("")
text_file.write("part 3:\n")


def write_text_file(list, credit):
    for i in list:
        text_file.write(f"{credit} - ")
        text_file.write(str(i[0]))
        text_file.write(", ")
        text_file.write(str(i[1]))
        text_file.write(", ")
        text_file.write(str(i[2]))
        text_file.write("\n")


write_text_file(list_progress, "Progress")                         #writes to the file
write_text_file(list_trailer, "Progress(module trailer)")
write_text_file(list_retriever, "Do not Progress – module retriever")
write_text_file(list_exclude, "Exclude")
text_file.close()

text_file = open("output data.txt", "r")           #reads from the file
data = text_file.read()
print(data)
text_file.close()
