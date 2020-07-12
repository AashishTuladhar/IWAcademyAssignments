import csv
import os.path
import academy as academy

class Courses():

    def __init__(self):
        self.courses = []
        path = os.path.dirname(os.path.abspath(__file__))
        
        with open(path + '/Records/Courses.csv', 'r') as csvfile: 

            csvreader = csv.reader(csvfile) 
            _ = next(csvreader) 
  
            for row in csvreader: 
                self.courses.append(row)

    def main(self): 
        self.displaycourses()
        print('\nDo you want to: \n1. Get details of one of the courses? \n2. Go to main menu')        
        courseListChoice = input('\nYour choice (1 or 2): ')

        while courseListChoice not in ['1', '2']:
            courseListChoice = input('Invalid choice. Please select 1 or 2: ')

        if courseListChoice == '1':
            courseCode = input('Enter course code for the course you want to know about: ')
            self.displaycourseinfo(courseCode)
            courseDetailsChoice = input('\nPress 1 and Enter to go to main menu: ')
            
            while courseDetailsChoice != '1':
                courseDetailsChoice = input('Option unavailable. Press 1 and Enter to go to main menu: ')
            
            academy.Academy().main()
        else:
            print('\n')
            academy.Academy().main()


    def getcourses(self):
        return self.courses
    
    def getcourseinfo(self,courseCode):
        for course in self.getcourses():
            if course[0] == courseCode:
                return course
            else:
                pass
        return []

    def displaycourses(self):
        courses = self.getcourses()

        print('Here is a list of our available courses:\n')
        for course in courses:
            print(f'Course (Code: {course[0]}) : {course[1]}')


    def displaycourseinfo(self,courseCode):
        course = self.getcourseinfo(courseCode)

        if len(course) > 0:
            print(f'\nCourse Details of {courseCode}: \n\n{course[1]} \n\nDuration (months): {course[2]} \nTime (hours): {course[3]} \nFee: 20000')
        else:
            courseCode = input('Please enter a valid course code: ')
            self.displaycourseinfo(courseCode)              


