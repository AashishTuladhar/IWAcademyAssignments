import courses as academyCourses
import students as academyStudents

class Academy:

    def main(self):
        print('Welcome to AT Academy! How can we help you? \n\n1. What are the courses available? \n2. Enroll me! \n3. Check my information \n4. Mark the program as completed \n5. Exit application \n')
        menuIndex = input('Menu number: ')
        
        while menuIndex not in ['1', '2', '3', '4', '5']:
            menuIndex = int(input('Option unavailable. Please enter a valid option: '))
        
        print('\n')

        if menuIndex == '1':
            academyCourses.Courses().main()
        elif menuIndex == '2':
            academyStudents.Students().enroll()
        elif menuIndex == '3':
            studentId = input('Enter your student ID: ')
            academyStudents.Students().main(studentId)
        elif menuIndex == '4':
            endProgram = input("The deposits of all the students will be refunded. Proceed? ('Y'-yes/'N'-no): ")
            while endProgram not in ['Y', 'N']:
                endProgram = input("Please enter either 'Y' for yes or 'N' for no: ")
            if endProgram == 'Y':
                academyStudents.Students().graduatestudents()
                print('The program has been marked complete successfully.')
            else:
                self.main()
        elif menuIndex == '5':
            print('We look forward to your visit again!')
        
        