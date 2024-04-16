class StudentList:
    def __init__(self):
        self.List1 = []
        self.List2 = []

    def take_exam(self, student_id, last_name, grade):
        for student in self.List1:
            if student[0] == student_id and student[1] == last_name:
                self.List1.remove(student)
                self.List2.append([student_id, last_name, grade])
                break

    def print_lists(self):
        print("Сдают экзамен:")
        for student in self.List1:
            print(student)
        print("\nСдали экзамен:")
        for student in self.List2:
            print(student)


student_list = StudentList()
student_list.List1 = [["001", "Иванов"], ["002", "Крылов"], ["003", "Васильев"]]
print("Изначальные списки:")
student_list.print_lists()

student_list.take_exam("001", "Иванов", "5")
print("\nСписки после того как кто-то сдал экзамен:")
student_list.print_lists()
