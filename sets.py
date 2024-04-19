#set_collection = {"charan",13,5,3}
#print(set_collection)
#empty_set = set()
#empty_set.add("charan")
#empty_set.add("charan")
#print(empty_set)
#set1 = {1,2,3,4,5}
#set2 = {4,5,6,7,8}
#print(set1.intersection(set2))
dictionary = {}
subject1 = input("Enter the subject1 name:")
subject2 = input("Enter the subject2 name:")
subject3 = input("Enter the subject3 name:")
subject_marks1 = int(input(f"Enter the marks of {subject1}:"))
subject_marks2 = int(input(f"Enter the marks of {subject2}:"))
subject_marks3 = int(input(f"Enter the marks of {subject3}:"))

dictionary.update({subject1:subject_marks1})
dictionary.update({subject2:subject_marks2})
dictionary.update({subject3:subject_marks3})

print(dictionary)

