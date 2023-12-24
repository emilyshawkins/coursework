import logging
from sqlalchemy import select
from menu_definitions import menu_main, debug_select
from db_connection import engine, Session
from orm_base import metadata

from Department import Department
from Course import Course
from Section import Section
from Student import Student
from Enrollment import Enrollment
from LetterGrade import LetterGrade
from PassFail import PassFail

from Option import Option
from Menu import Menu

from datetime import time, datetime


def add_student_letter_grade(sess):

    grade = ''
    unique_student_section: bool = False
    valid_grade = False

    while not unique_student_section or not valid_grade:
        print('Please select a student:')
        student: Student = select_student(sess)
        print('Please select a section')
        section: Section = select_section(sess)

        count: int = sess.query(Enrollment).filter(Enrollment.studentID == student.studentId,
                                                   Enrollment.section_id == section.section_id).count()

        unique_student_section = count == 0
        if not unique_student_section:
            print("That section already has that student enrolled in it. Please try again.")

        if unique_student_section:
            grade = input('Letter Grade--> ').upper()
            if grade not in ['A', 'B', 'C', 'D', 'F']:
                print('That is not a valid grade. Please try again.')
            else:
                valid_grade = True

    letter_grade = LetterGrade(section, student, grade)
    sess.add(letter_grade)
    sess.flush()

def add_student_pass_fail(sess):

    unique_student_section: bool = False

    while not unique_student_section:
        print('Please select a student:')
        student: Student = select_student(sess)
        print('Please select a section')
        section: Section = select_section(sess)

        count: int = sess.query(Enrollment).filter(Enrollment.studentID == student.studentId,
                                                   Enrollment.section_id == section.section_id).count()

        unique_student_section = count == 0
        if not unique_student_section:
            print("That section already has that student enrolled in it. Please try again.")
    pass_fail = PassFail(section, student, datetime.now())
    sess.add(pass_fail)
    sess.flush()

def add_section_to_student(sess): # Finished

    unique_enrollment: bool = False
    student_is_in_course = False
    while not unique_enrollment or not student_is_in_course:
        print('Please select a section: ')
        section = select_section(sess)
        print('Please select the student you want to add the section to: ')
        student = select_student(sess)

        enrollment_count = sess.query(Enrollment).filter(Enrollment.section_id == section.section_id,
                                                         Enrollment.studentID == student.studentId).count()

        unique_enrollment: bool = enrollment_count == 0

        if not unique_enrollment:
            print("The student already has that section. Please try again.")
        if unique_enrollment:
            courses = sess.query(Enrollment).filter(Enrollment.studentID == student.studentId)
            student_is_in_course = True
            for sec in courses:
                if (section.departmentAbbreviation == sec.section.departmentAbbreviation and
                        section.courseNumber == sec.section.courseNumber and
                        section.sectionYear == sec.section.sectionYear and section.semester == sec.section.semester):
                    student_is_in_course = False
                    break

            if not student_is_in_course:
                print("A section cannot be added to a student that is already taking that course through another section this semester.")

    student.add_section(section)
    sess.add(student)
    sess.flush()

def add_student_to_section(sess): # Finished

    unique_enrollment: bool = False
    student_is_in_course = False
    while not unique_enrollment or not student_is_in_course:
        print('Please select a student: ')
        student = select_student(sess)
        print('Please select the student you want to add the section to: ')
        section = select_section(sess)

        enrollment_count = sess.query(Enrollment).filter(Enrollment.section_id == section.section_id,
                                                         Enrollment.studentID == student.studentId).count()

        unique_enrollment: bool = enrollment_count == 0

        if not unique_enrollment:
            print("The section already has that student. Please try again.")
        if unique_enrollment:
            courses = sess.query(Enrollment).filter(Enrollment.studentID == student.studentId)
            student_is_in_course = True
            for sec in courses:
                if (section.departmentAbbreviation == sec.section.departmentAbbreviation and
                        section.courseNumber == sec.section.courseNumber and
                        section.sectionYear == sec.section.sectionYear and section.semester == sec.section.semester):
                    student_is_in_course = False
                    break

            if not student_is_in_course:
                print("A student cannot be added to a section that they are already taking through another section this semester.")

    section.add_student(student)
    sess.add(section)
    sess.flush()

def delete_with_student(sess):

    print("Choose the student you want to delete a section from.")
    student = select_student(sess)
    print("Choose the section you want to remove from the student.")
    section = select_section(sess)
    student.remove_section(section)

def delete_with_section(sess):

    print("Choose the section you want to delete a student from.")
    section = select_section(sess)
    print("Choose the student you want to remove from the section.")
    student = select_student(sess)
    section.remove_student(student)

def list_student_enrollments(sess):

    print("Choose student that you want to see the sections of.")
    student = select_student(sess)
    combine = sess.query(Student).join(Enrollment, Student.studentId == Enrollment.studentID).join(
        Section, Enrollment.section_id == Section.section_id).add_columns(
        Student.studentId, Student.lastName, Student.firstName, Student.eMail, Section.departmentAbbreviation,
        Section.courseNumber, Section.sectionNumber, Section.semester, Section.sectionYear, Section.building,
        Section.room, Section.schedule, Section.startTime, Section.instructor).filter(
        Student.studentId == student.studentId).all()

    print(f"\n{student}\n is enrolled in section(s): ")
    for enrollments in combine:
        print(f"Department Abbreviation: {enrollments.departmentAbbreviation}\n"
              f"Course Number: {enrollments.courseNumber}\n"
              f"Section Number: {enrollments.sectionNumber}\n"
              f"Semester: {enrollments.semester}\n"
              f"Section Year: {enrollments.sectionYear}\n"
              f"Building: {enrollments.building}\n"
              f"Room: {enrollments.room}\n"
              f"Schedule: {enrollments.schedule}\n"
              f"Start Time: {enrollments.startTime}\n"
              f"Instructor: {enrollments.instructor}\n")

def list_section_enrollments(sess):

    print("Choose section that you want to see the students of.")
    section = select_section(sess)

    combine = sess.query(Section).join(Enrollment, Section.section_id == Enrollment.section_id).join(
        Student, Enrollment.studentID == Student.studentId).add_columns(
        Student.studentId, Student.lastName, Student.firstName, Student.eMail, Section.departmentAbbreviation,
        Section.courseNumber, Section.sectionNumber, Section.semester, Section.sectionYear, Section.building,
        Section.room, Section.schedule, Section.startTime, Section.instructor).filter(
        Section.section_id == section.section_id).all()

    print(f"\n{section}student(s) are: \n")
    for enrollments in combine:
        print(f"ID: {enrollments.studentId}\n"
              f"Name: {enrollments.lastName}, {enrollments.firstName}\n"
              f"E-mail: {enrollments.eMail}\n")

def list_enrollments(sess: Session):

    enrollments = sess.query(Enrollment).order_by(Enrollment.studentID, Enrollment.section_id).all()

    for enrollment in enrollments:
        print(enrollment)

def delete_section(sess):

    print('Deleting a Section')
    section = select_section(sess)
    n_enrollments = sess.query(Enrollment).filter(Enrollment.section_id == section.section_id).count()

    if n_enrollments > 0:
        print(f'Sorry, there are {n_enrollments} student(s) in that section. Delete them first then return here to delete'
              f' the section.')
    else:
        sess.delete(section)

def delete_student(sess):

    print('Deleting a Student')
    student = select_student(sess)
    n_enrollments = sess.query(Enrollment).filter(Enrollment.studentID == student.studentId).count()

    if n_enrollments > 0:
        print(f'Sorry, there are {n_enrollments} section(s) for that student. Delete them first then return here to delete'
              f' the student.')
    else:
        sess.delete(student)

def select_student(sess: Session) -> Student: # Helper Function
    found: bool = False

    student_lastName = ''
    student_firstName = ''

    while not found:
        student_lastName = input("Student Last Name-->")
        student_firstName = input('Student First Name-->')

        count = sess.query(Student).filter(Student.lastName == student_lastName, Student.firstName == student_firstName).count()

        found = count == 1
        if not found:
            print("No student with that name. Please try again.")

    student = sess.query(Student).filter(Student.lastName == student_lastName, Student.firstName == student_firstName).first()
    return student

def select_section(sess: Session) -> Section: # Helper function
    found: bool = False

    dep_abbr: str = ''
    course_num: int = 0
    section_num: int = 0
    semester: str = ''
    section_year: int = 0

    while not found:
        dep_abbr = input("Department abbreviation-->")
        course_num = int(input("Course number-->"))
        section_num = int(input("Section number-->"))
        semester = input("Semester-->")
        section_year = int(input("Section Year-->"))

        count = sess.query(Section).filter(Section.departmentAbbreviation == dep_abbr,
                                           Section.courseNumber == course_num,
                                           Section.sectionNumber == section_num,
                                           Section.semester == semester,
                                           Section.sectionYear == section_year).count()

        found = count == 1
        if not found:
            print("No section with that section number, semester, and year under that department and course.")

    section = sess.query(Section).filter(Section.departmentAbbreviation == dep_abbr,
                                         Section.courseNumber == course_num,
                                         Section.sectionNumber == section_num,
                                         Section.semester == semester,
                                         Section.sectionYear == section_year).first()
    return section

def select_department(sess: Session) -> Department:   # Required
    """
    Prompts the user for a specific department using its abbreviation.
    :param sess: Connection to the database.
    :return: The selected department
    """
    found: bool = False
    abbreviation: str = ''

    while not found:
        abbreviation = input('Enter the department abbreviation--> ')
        abbreviation_count: int = sess.query(Department).filter(Department.abbreviation == abbreviation).count()
        found = abbreviation_count == 1

        if not found:
            print('There is no department with that abbreviation. Please try again.')

    return_department: Department = sess.query(Department).filter(Department.abbreviation == abbreviation).first()
    return return_department

def select_course(sess: Session) -> Course:
    """
    Selects a course using the department abbreviation and course number.
    :param sess: Connection to the database.
    :return: The selected course
    """
    found: bool = False
    department_abbreviation: str = ''
    course_number: int = -1

    while not found:
        department_abbreviation = input('Department Abbreviation--> ')
        course_number = int(input('Course Number--> '))
        name_count: int = sess.query(Course).filter(Course.departmentAbbreviation == department_abbreviation,
                                                    Course.courseNumber == course_number).count()
        found = name_count == 1
        if not found:
            print('No courses by that number in that department. Please try again.')

    course = sess.query(Course).filter(Course.departmentAbbreviation == department_abbreviation,
                                       Course.courseNumber == course_number).first()
    return course

def add_student(session: Session):

    unique_name: bool = False
    unique_email: bool = False
    last_name: str = ''
    first_name: str = ''
    email: str = ''
    while not unique_email or not unique_name:
        last_name = input("Student last name--> ")
        first_name = input("Student first name-->")
        email = input("Student e-mail address--> ")
        name_count: int = session.query(Student).filter(Student.lastName == last_name,
                                                        Student.firstName == first_name).count()
        unique_name = name_count == 0
        if not unique_name:
            print("We already have a student by that name.  Try again.")
        if unique_name:
            email_count = session.query(Student).filter(Student.email == email).count()
            unique_email = email_count == 0
            if not unique_email:
                print("We already have a student with that email address.  Try again.")
    new_student = Student(last_name, first_name, email)
    session.add(new_student)

def add_section(sess: Session): # Required
    """
      Prompt the user for information for the new section and validates it.
      :param sess: Connection to the database.
      :return: None
      """
    # uniqueness constraints:  {year, semester, schedule, start_time, building, room},
    # {year, semester, schedule, start_time, instructor}
    print('Which department and course offers this section?')
    course: Course = select_course(sess)
    unique_pk = False
    unique_const1 = False
    unique_const2 = False

    section_number = 0
    semester = ''
    section_year = 0
    building = ''
    room = 0
    schedule = ''
    start_time = time(0, 0, 0)
    instructor = ''

    while not unique_pk or not unique_const1 or not unique_const2:
        section_number = int(input('Section Number-->'))
        semester = input("Semester-->")
        section_year = int(input('Section Year-->'))
        if semester.upper() not in ['FALL', 'SPRING', 'WINTER', 'SUMMER I', 'SUMMER II']:
            print('That is not a valid semester [\'FALL\', \'SPRING\', \'WINTER\', \'SUMMER I\', \'SUMMER II\']. '
                  'Please try again.')
        if semester.upper() in ['FALL', 'SPRING', 'WINTER', 'SUMMER I', 'SUMMER II']:
            section_num_count = sess.query(Section).filter(Section.departmentAbbreviation == course.departmentAbbreviation,
                                                           Section.courseNumber == course.courseNumber,
                                                           Section.sectionNumber == section_number,
                                                           Section.semester == semester,
                                                           Section.sectionYear == section_year).count()
            unique_pk = section_num_count == 0

            if not unique_pk:
                print('That section already exists. Please try again.')
            if unique_pk:
                schedule = input("Schedule-->")
                if schedule not in ['MW', 'TuTh', 'MWF', 'F', 'S']:
                    print('That is not a valid schedule [\'MW\', \'TuTh\', \'MWF\', \'F\', \'S\']. Please try again.')
                if schedule in ['MW', 'TuTh', 'MWF', 'F', 'S']:
                    start_time = input('Start Time-->')
                    start_time = time(int(start_time[:2]), int(start_time[3:]), 0)
                    building = input("Building name-->")
                    room = int(input("Room number-->"))
                    sect_count1: int = sess.query(Section).filter(Section.sectionYear == section_year,
                                                                  Section.semester == semester,
                                                                  Section.schedule == schedule,
                                                                  Section.startTime == start_time,
                                                                  Section.building == building,
                                                                  Section.room == room).count()
                    unique_const1 = sect_count1 == 0

                    if not unique_const1:
                        print('We already have section of that course with that year, semester, schedule, start time, '
                              'building, and room in that department. Please try again.')
                    if unique_const1:
                        instructor = input("Instructor-->")
                        sect_count2: int = sess.query(Section).filter(Section.sectionYear == section_year,
                                                                      Section.semester == semester,
                                                                      Section.schedule == schedule,
                                                                      Section.startTime == start_time,
                                                                      Section.instructor == instructor).count()
                        unique_const2 = sect_count2 == 0
                        if not unique_const2:
                            print('We already have a section of this course in this department with the same year,'
                                  ' semester, schedule, start time, and instructor. Please try again.')

        section = Section(course, section_number, semester, section_year, building, room, schedule, start_time, instructor)
        sess.add(section)

def add_course(session: Session):
    """
    Prompt the user for the information for a new course and validate
    the input to make sure that we do not create any duplicates.
    :param session: The connection to the database.
    :return:        None
    """
    print("Which department offers this course?")
    department: Department = select_department(sess)
    unique_number: bool = False
    unique_name: bool = False
    number: int = -1
    name: str = ''
    while not unique_number or not unique_name:
        name = input("Course full name--> ")
        number = int(input("Course number--> "))
        name_count: int = session.query(Course).filter(Course.departmentAbbreviation == department.abbreviation,
                                                       Course.name == name).count()
        unique_name = name_count == 0
        if not unique_name:
            print("We already have a course by that name in that department.  Try again.")
        if unique_name:
            number_count = session.query(Course). \
                filter(Course.departmentAbbreviation == department.abbreviation,
                       Course.courseNumber == number).count()
            unique_number = number_count == 0
            if not unique_number:
                print("We already have a course in this department with that number.  Try again.")
    description: str = input('Please enter the course description-->')
    units: int = int(input('How many units for this course-->'))
    course = Course(department, number, name, description, units)
    session.add(course)

def add_department(sess: Session):  # Required
    """
    Prompts user for information for the new department and validates the department information that is given.
    :param sess: Connection to the database
    :return: None
    """
    unique_name: bool = False
    unique_abbreviation: bool = False
    unique_chair_name: bool = False
    unique_room: bool = False
    unique_description: bool = False

    name: str = ''
    abbreviation: str = ''
    chairName: str = ''
    building: str = ''
    office: int = 0
    description: str = ''

    while (not unique_name or not unique_abbreviation or not unique_chair_name or not unique_room or not
    unique_description):

        name = input('Department Name--> ')
        name_count: int = sess.query(Department).filter(Department.name == name).count()
        unique_name = name_count == 0
        if not unique_name:
            print('There is already a department with that name. Please try again.')
        if unique_name:

            abbreviation = input('Department Abbreviation--> ')
            abbreviation_count: int = sess.query(Department).filter(Department.abbreviation == abbreviation).count()
            unique_abbreviation = abbreviation_count == 0
            if not unique_abbreviation:
                print('There is already a department with that abbreviation. Please try again.')
            if unique_abbreviation:

                chairName = input('Department Chair Name--> ')
                chair_name_count: int = sess.query(Department).filter(Department.chairName == chairName).count()
                unique_chair_name = chair_name_count == 0
                if not unique_chair_name:
                    print('There is already a department with that chair name. Please try again.')
                if unique_chair_name:

                    building = input('Department Building--> ')
                    office = int(input('Department Office--> '))
                    room_count: int = sess.query(Department).filter(Department.building == building,
                                                                       Department.office == office).count()
                    unique_room = room_count == 0
                    if not unique_room:
                        print('There is already a department with that building and office. Please try again.')
                    if unique_room:
                        description = input('Department Description--> ')
                        description_count: int = sess.query(Department).filter(Department.description ==
                                                                                  description).count()
                        unique_description = description_count == 0
                        if not unique_description:
                            print('There is already a department with that description. Please try again.')

    newDepartment = Department(name, abbreviation, chairName, building, office, description)
    sess.add(newDepartment)

def delete_department(sess: Session):   # Required
    """
    Prompt the user for a department to delete it.
    :param sess: Connection to the database
    :return: None
    """
    print('Deleting a Department')
    department = select_department(sess)
    n_courses = sess.query(Course).filter(Course.departmentAbbreviation == department.abbreviation).count()

    if n_courses > 0:
        print(f'Sorry, there are {n_courses} courses in that department. Delete them first then return here to delete'
              f' the department.')
    else:
        sess.delete(department)

def delete_course(sess: Session):   # Required
    """
    Prompt the user for a course using the abbreviation of the department of the course and delete it.
    :param sess: Connection to the database.
    :return:
    """
    print('Deleting a Course')
    course = select_course(sess)
    n_sections = sess.query(Section).filter(Section.departmentAbbreviation == course.departmentAbbreviation,
                                            Section.courseNumber == course.courseNumber).count()
    if n_sections > 0:
        print(f'Sorry, there are {n_sections} sections in that course. Please delete them first, then come back here to'
              f' delete the course.')
    else:
        sess.delete(course)

def auto_add(sess: Session):
    department: Department = Department('Computer Engineering & Computer Science', 'CECS', 'someone1', 'ECS', 105, 'computer goes beep boop')
    course1: Course = Course(department, 325, 'System Programming', 'Linux', 3)
    course2: Course = Course(department, 229, 'Discrete Structures II', 'Math', 3)
    course3: Course = Course(department, 328, 'Algorithms', 'Big-O', 3)
    section0: Section = Section(course1, 1, 'Spring', 2023, 'HC', 100, 'MW', time(18, 0, 0), 'Prof. Gold')
    section1: Section = Section(course1, 2, 'Spring', 2023, 'HSCI', 100, 'TuTh', time(17, 0, 0), 'Prof. Gold')
    section2: Section = Section(course2, 1, 'Spring', 2023, 'HC', 100, 'TuTh', time(12, 30, 0), 'Prof. Varela')
    section3: Section = Section(course3, 1, 'Spring', 2023, 'COB', 140, 'MW', time(18, 30, 0), 'Prof. Fahim')
    student1: Student = Student('Hawkins', 'Emily', 'emily.hawkins01@student.csulb.edu')
    student2: Student = Student('Noh', 'Yunjong', 'last.first01@mail.com')
    student3: Student = Student('Beup', 'Justin', 'last.first02@mail.com')
    sess.add(department)
    sess.add(course1)
    sess.add(course2)
    sess.add(course3)
    sess.add(section0)
    sess.add(section1)
    sess.add(section2)
    sess.add(section3)
    sess.add(student1)
    sess.add(student2)
    sess.add(student3)

    sess.flush()

if __name__ == '__main__':
    print('Starting off')
    logging.basicConfig()
    logging_action = debug_select.menu_prompt()
    logging.getLogger("sqlalchemy.engine").setLevel(eval(logging_action))
    logging.getLogger("sqlalchemy.pool").setLevel(eval(logging_action))

    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)

    with Session() as sess:
        main_action: str = ''
        while main_action != menu_main.last_action():
            main_action = menu_main.menu_prompt()
            print('next action: ', main_action)
            exec(main_action)
        sess.commit()
    print('Ending normally')
