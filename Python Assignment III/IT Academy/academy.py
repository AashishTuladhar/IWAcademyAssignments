import courses as academyCourses
import students as academyStudents

class Academy:

    def main(self):
        print('Welcome to AT Academy! How can we help you? \n\n1. What are the courses available? \n2. Enroll me! \n3. Check my information \n4. Exit application \n')
        menuIndex = int(input('Menu number: '))
        
        while menuIndex not in [1,2,3,4]:
            menuIndex = int(input('Option unavailable. Please enter a valid option: '))
        
        print('\n')

        if menuIndex == 1:
            academyCourses.Courses().main()
        elif menuIndex == 2:
            academyStudents.Students().enroll()
        elif menuIndex == 3:
            studentId = input('Enter your student ID: ')
            academyStudents.Students().main(studentId)
        elif menuIndex == 4:
            print('We look forward to your visit again!')
        