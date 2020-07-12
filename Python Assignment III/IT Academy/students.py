import csv
import os.path
import academy as academy
import courses as academyCourses
import csvfunctions as dbcontext

class Students:

    def __init__(self):
        self.students = []
        self.full_path = os.path.expanduser('~/Desktop/Insight Workshop/Assignments/Python/Python Assignment III/IT Academy/Records/Students.csv')
        
        with open(self.full_path, 'r') as csvfile: 

            csvreader = csv.reader(csvfile) 
            self.header = next(csvreader) 
  
            for row in csvreader: 
                self.students.append(row)


    def main(self,studentId):
        student = self.getstudentinfo(studentId)

        while len(student) == 0:
            studentId = input('Invalid Student ID. Please enter a valid ID, or press 4 and Enter to exit: ')
            if studentId == '4':
                break
            student = self.getstudentinfo(studentId)

        if studentId == '4':
            print('\n')
            academy.Academy().main()
        else:
            self.displaystudentinfo(studentId)

            print('What would you like to do?')
            if student[7] == '0':
                print(f'\n1. {"Mark the course as complete" if int(student[5]) == 20000 else "Pay remaining installment"} \n2. Leave the program')
            
            print('3. Go to main menu \n')
            
            studentChoice = input('Your choice: ')

            while studentChoice not in ['1', '2', '3', '4']:
                studentChoice = input('Invalid option. Please choose between the available options: ')

            if studentChoice == '1':
                studentIndex = self.students.index(student)
                if int(student[5]) == 20000:
                    self.students[studentIndex][5] = 0
                    self.students[studentIndex][6] = 20000
                    self.students[studentIndex][7] = 1
                    
                else:
                    self.students[studentIndex][5] = 20000
                    self.students[studentIndex][6] = 0

                dbcontext.CsvFunctions().writer(self.header,self.students,self.full_path)

                print('\nYour data has been updated!\n')
                self.main(studentId)
            elif studentChoice == '2':
                confirmChoice = input("\nIf you leave the program, your deposit won't be refunded. Do you want to continue? ('Y' - yes/'N' - no): ")

                while confirmChoice not in ('Y', 'N'):
                    confirmChoice = input("Please select either 'Y' or 'N'")
                
                if confirmChoice == 'Y':
                    studentIndex = self.students.index(student)
                    _ = self.students.pop(studentIndex)
                    dbcontext.CsvFunctions().writer(self.header,self.students,self.full_path)
                    print('\nYou have left the program. :( We hope to see you with us soon!\n')
                    academy.Academy().main()
                else:
                    self.main(studentId)
            elif studentChoice == '3':
                print('\n')
                academy.Academy().main()


    def getstudentinfo(self,studentid):
        for student in self.students:
            if student[0] == studentid:
                return student
        
        return []

    def displaystudentinfo(self,studentId):
        student = self.getstudentinfo(studentId)
        studentInfo = f'\n{student[1]} (Student ID: {student[0]}) \nAge: {student[2]} \nGender: {student[3]}'
        studentInfo += f'\n\nCourse: {academyCourses.Courses().getcourseinfo(student[4])[1]}'
        studentInfo += f'\nDeposit: {student[5]} \nBalance: {student[6]} \n'
        print(studentInfo)



    def enroll(self):
        academyCourses.Courses().displaycourses()

        courseCode = input('Which course do you want to enroll in (use course code)? ')
        studentName = input('Enter your full name: ')
        age = input('Age: ')
        gender = input('Gender (M/F): ')
        amount = input("""You can pay for this course in two installments. The total cost is 20,000, but you can pay an installment of 10,000.\nChoose 1 for full payment and 2 for paying in installment: """)
        
        while amount not in ['1', '2']:
            amount = input("Invalid option. Choose 1 for full payment and 2 for paying in installment: ")

        amount = 20000 if amount == "1" else 10000

        print(f'\nName: {studentName} \nAge: {age} \nGender: {"Male" if gender == "M" else "Female"} \nCourse: {academyCourses.Courses().getcourseinfo(courseCode)[1]} \nAmount: {amount} \n')
        print("""Would you like to continue with the enrollment? \n\n1.Yes, this looks good! \n2.I'd like to fill this form again """)
        enrollConfirm = int(input('\nYour choice: '))

        if enrollConfirm == 1:
            self.students.append([self.generatestudentid(), studentName, age, gender, courseCode, amount, 0 if amount == 20000 else 10000, '0'])
            dbcontext.CsvFunctions().writer(self.header,self.students,self.full_path)
            print(f'\nCongratulations! You have been enrolled! Your ID is {self.students[-1][0]}. You can use this ID to view your information from the main menu. \n')
            
            enrollCompleted = input('Press 1 and Enter to go to main menu: ')
            while enrollCompleted != '1':
                enrollCompleted = input('Option unavailable. Press 1 and Enter to go to main menu: ')
            print('\n')
            academy.Academy().main()
        elif enrollConfirm == 2:
            self.enroll()
        



    def generatestudentid(self):
        maxstudentid = self.students[-1][0] if len(self.students) > 1 else 'S000' if len(self.students) == 0 else self.students[0][0]
        suffix = int(maxstudentid[-3:])
        newid = 'S' + ('00' + str(suffix + 1))[-3:]
        return newid




    



