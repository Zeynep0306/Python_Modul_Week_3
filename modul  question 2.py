class School :
    def __init__(self, name, foundation_year):
        self.name= name
        self.foundation_year = foundation_year

        self.students=[]
        self.teachers=[]

    def add_new_student(self, student_name,class_name):
        student= {"name": student_name , "class": class_name}
        self.students.append(student)
        print(f"{student_name} adli ogrenci {class_name} sinifina eklendi.")

    def add_new_teacher(self, teacher_name, branch):
        teacher= {"name": teacher_name, "branch": branch}
        self.teachers.append(teacher)
        print(f" {teacher_name} adli ogretmen {branch} bransiyla  eklendi.")

    def view_student_list(self):
        for student in self.students:
            print(f"{ student["name"]} {student["class"]}")

    def view_teacher_list(self):
        for teacher in self.teachers:
            print(f"{teacher["name"]} {teacher["branch"]}")

my_school= School( "anadolu lisesi ", 1998 )
my_school.add_new_student("ayse yilmaz", "10/A")
my_school.add_new_student("zeynep can", "8/C")

my_school.add_new_teacher("ahmet yilmaz", "fizik")
my_school.add_new_teacher("murat yildirim", "matematik")

my_school.view_student_list()
my_school.view_teacher_list()