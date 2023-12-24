from Menu import Menu
from Option import Option

menu_main = Menu('main', 'Please select one of the following options:',
                 [
                     Option("Add Student to Pass/Fail", "add_student_pass_fail(sess)"),
                     Option("Add Student to Letter Grade", "add_student_letter_grade(sess)"),
                     Option("Add Section to Student", "add_section_to_student(sess)"),
                     Option("Add Student to Section", "add_student_to_section(sess)"),
                     Option("Delete Enrollment with Student First", "delete_with_student(sess)"),
                     Option("Delete Enrollment with Section First", "delete_with_section(sess)"),
                     Option("List Enrollments of Student", "list_student_enrollments(sess)"),
                     Option("List Enrollments in Section", "list_section_enrollments(sess)"),
                     Option("List All Enrollments", "list_enrollments(sess)"),
                     Option("Delete Section", "delete_section(sess)"),
                     Option("Delete Student", "delete_student(sess)"),
                     Option("Prefill Data", "auto_add(sess)"),
                     Option("Exit", "pass")
                 ])

debug_select = Menu('debug select', 'Please select a debug level:',
                    [
                        Option("Informational", "logging.INFO"),
                        Option("Debug", "logging.DEBUG"),
                        Option("Error", "logging.ERROR")
                    ])