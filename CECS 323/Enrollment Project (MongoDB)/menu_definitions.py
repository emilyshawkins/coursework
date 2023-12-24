from Menu import Menu
from Option import Option

menu_main = Menu('main', 'Please select one of the following options:', [
  Option("Add", "add(db)"),
  Option("List", "list_objects(db)"),
  Option("Delete", "delete(db)"),
  Option("Exit", "pass")
])

add_menu = Menu('add', 'Please indicate what you want to add:', [
  Option("Department", "add_department(db)"),
  Option("Major", "add_major(db)"),
  Option("Student", "add_student(db)"),
  Option("Course", "add_course(db)"),
  Option("Section", "add_section(db)"),
  
  Option("Student Major", "add_student_major(db)"),
  Option("Enrollment", "add_enrollment(db)"),
  
  Option("Exit", "pass")
])

delete_menu = Menu('delete', 'Please indicate what you want to delete from:', [
  Option("Department", "delete_department(db)"),
  Option("Major", "delete_major(db)"),
  Option("Student", "delete_student(db)"),
  Option("Course", "delete_course(db)"),
  Option("Section", "delete_section(db)"),
  
  Option("Student Major", "delete_student_major(db)"),
  Option("Enrollment", "delete_enrollment(db)"),
  
  Option("Exit", "pass")
])

list_menu = Menu('list', 'Please indicate what you want to list:', [
  Option("Department", "list_department(db)"),
  Option("Major", "list_major(db)"),
  Option("Student", "list_student(db)"),
  Option("Course", "list_course(db)"),
  Option("Section", "list_section(db)"),
  
  Option("Student in Major", "list_student_in_major(db)"),
  Option("Major for Student", "list_major_for_student(db)"),
  
  Option("Student Enrollment", "list_sections_of_student(db)"),
  Option("Section Enrollment", "list_students_in_section(db)"),
  
  Option("Exit", "pass")
])
