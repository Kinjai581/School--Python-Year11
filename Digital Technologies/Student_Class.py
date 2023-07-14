'''Extend the student class so that we have methods to:
-  return a student�s name and connect group
-  set and return a student�s year and school




Use lists and loops appropriately for the following
-  Prints the names of any student who's first names comes before the letter 'M'
-  Neatly prints connect_groups and the list of members in that group
     e.g. :
       347: [�Jordan�, �Olivia�]
       764: [�Dominic�, �Rafi�]
       656: [�Markus�]
       etc.
-  Changes the school name of any Year 12 students to �Graduated� and prints the
   message: �(name) has graduated!� for these Year 12 students
'''




class Student:
    def __init__(self, name, year, connect_group, school):
        self.name = name
        self.year = year
        self.connect_group = connect_group
        self.school = school


    def study(self):
        print(self.name, 'is studying year', self.year, 'and is in connect group', self.connect_group, 'at', self.school)




    def get_connect(self):
         return self.connect_group




    def get_name(self):
        return self.name


    def set_student_year(self, year):
        self.year = year
        print (self.year)




    def get_school(self, school):
        self.school = school
        print(self.school)
        
    
    def change_grade(self):
        if self.year == 12:
            self.school = 'Graduated'
            print(f'{self.name} has graduated!')





jordan = Student('Jordan', 11, 347, 'Canberra College')
olivia = Student('Olivia', 11, 347, 'Canberra College')
dominic = Student('Dominic', 11, 764, 'Canberra College')
markus = Student('Markus', 12, 656, 'Canberra College')
finnegan = Student('Finnegan', 12, 236, 'Canberra College')
jamie = Student('Jamie', 11, 546, 'Canberra College')
rafi = Student('Rafi', 11, 764, 'Canberra College')
lachlan = Student('Lachlan', 11, 237, 'Canberra College')
inho = Student('Inho', 11, 546, 'Canberra College')
rafe = Student('Rafe', 11, 123, 'Canberra College')
vejhay = Student('Vejhay', 11, 826, 'Canberra College')


student_list = [jordan, olivia, dominic, markus, finnegan, jamie, rafi, lachlan, inho, rafe, vejhay]


connects = {}
for student in student_list: # putting an empty list for every connect group into a list
    connects[student.get_connect()] = []


for student in student_list: # adding the names of the students to the dictionary
    connects[student.get_connect()].append(student.get_name())


for k in connects: # prints the students in that neat format
    #print(k)
    print(k,':' , ', '.join(connects[k]))



for student in student_list:
    if student.get_name() < 'M':
        print(student.get_name())


#vejhay.study()








#markus.study()
#markus.change_grade()
#markus.student_letter_M(student.name)
#jordan.connect_group_list(student_list)



