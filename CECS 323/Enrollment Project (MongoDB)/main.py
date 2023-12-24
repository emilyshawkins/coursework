import pymongo
from pymongo import MongoClient
from pprint import pprint
import getpass
import datetime

from menu_definitions import menu_main
from menu_definitions import add_menu
from menu_definitions import delete_menu
from menu_definitions import list_menu


# Menu
def add(db):
  """
  Present the add menu and execute the user's selection.
  :param db:  The connection to the current database.
  :return:    None
  """
  add_action: str = ''
  while add_action != add_menu.last_action():
    add_action = add_menu.menu_prompt()
    exec(add_action)


def delete(db):
  """
  Present the delete menu and execute the user's selection.
  :param db:  The connection to the current database.
  :return:    None
  """
  delete_action: str = ''
  while delete_action != delete_menu.last_action():
    delete_action = delete_menu.menu_prompt()
    exec(delete_action)


def list_objects(db):
  """
  Present the list menu and execute the user's selection.
  :param db:  The connection to the current database.
  :return:    None
  """
  list_action: str = ''
  while list_action != list_menu.last_action():
    list_action = list_menu.menu_prompt()
    exec(list_action)


# Schemas & UK
def validator(collection_name: str):
  """Depending on what collection name is input, it will choose a validator below."""

  validate = None

  if collection_name == 'departments':

    validate = {
      '$jsonSchema': {
        'bsonType':
        'object',
        'description':
        'A division of a large organization like a university. For example, CSULB.',
        'required': [
          'name', 'abbreviation', 'chair_name', 'building', 'office',
          'description', 'courses', 'majors'
        ],
        'additionalProperties':
        False,
        'properties': {
          '_id': {},
          'name': {
            'bsonType': 'string',
            'description': 'A text string that identifies a department.',
            'minLength': 10,
            'maxLength': 50,
          },
          'abbreviation': {
            'bsonType': 'string',
            'description':
            'A shorted version of the departments name, also used to identify a department.',
            'maxLength': 6
          },
          'chair_name': {
            'bsonType': 'string',
            'description': 'The person who is the head of the department.',
            'maxLength': 80
          },
          'building': {
            'bsonType':
            'string',
            'description':
            'Name of the location where the department head is.',
            'enum': [
              'ANAC', 'CDC', 'DC', 'ECS', 'EN2', 'EN3', 'EN4', 'EN5', 'ET',
              'HSCI', 'NUR', 'VEC'
            ]
          },
          'office': {
            'bsonType':
            'int',
            'description':
            'The number for the room where the department head is.'
          },
          'description': {
            'bsonType': 'string',
            'description':
            'A text string providing information about the department.',
            'minLength': 10,
            'maxLength': 80
          },
          'courses': {  # one to many design
            'bsonType': 'array',
            'items': {
              'bsonType': 'objectId',
            }
          },
          'majors': {  # one to many design
            'bsonType': 'array',
            'items': {
              'bsonType': 'objectId'
            }
          }
        }
      }
    }

  if collection_name == 'majors':

    validate = {
      '$jsonSchema': {
        'bsonType': 'object',
        'description':
        'A course of study that is offered to students in higher education.',
        'required': ['name', 'description', 'department', 'student_majors'],
        'additionalProperties': False,
        'properties': {
          '_id': {},
          'name': {
            'bsonType': 'string',
            'description': 'A text string that identifies a major.',
          },
          'description': {
            'bsonType': 'string',
            'description':
            'A text string providing information about the major.'
          },
          'department': {  # For two way ref
            'bsonType':
            'objectId',
            'description':
            'The identifier of the department that the major belongs to.'
          },
          'student_majors': {
            'bsonType': 'array',
            'items': {
              'bsonType': 'objectId'
            }
          }
        }
      }
    }

  if collection_name == 'courses':

    validate = {
      '$jsonSchema': {
        'bsonType':
        'object',
        'description':
        'Specific subjects of study offered by a department that contribute to student learning of particular subjects.',
        'required': [
          'course_number', 'course_name', 'description', 'units',
          'department_abbr', 'sections'
        ],
        'additionalProperties':
        False,
        'properties': {
          '_id': {},
          'course_number': {
            'bsonType':
            'int',
            'description':
            'An integer, usually three digits, identifying the course among other courses in the department.'
          },
          'course_name': {
            'bsonType': 'string',
            'description': 'A textstring, identifying the course.',
            'minimum': 100,
            'maximum': 699
          },
          'description': {
            'bsonType':
            'string',
            'description':
            'A textstring that provides information about the course.'
          },
          'units': {
            'bsonType': 'int',
            'description':
            'An integer with how many credits that particular course is.',
            'minimum': 1,
            'maximum': 5
          },
          'department_abbr':
          {  # Denormalization of the abbreviation, no ID, abbreviation is unique
            'bsonType':
            'string',
            'description':
            'The abbreviation of the department that the course belongs to.'
          },
          'sections': {  # One to many
            'bsonType': 'array',
            'items': {
              'bsonType': 'objectId'
            }
          }
        }
      }
    }

  if collection_name == 'students':

    validate = {
      '$jsonSchema': {
        'bsonType':
        'object',
        'description':
        'A person who attends an educational facility.',
        'required':
        ['last_name', 'first_name', 'email', 'student_majors', 'enrollments'],
        'additionalProperties':
        False,
        'properties': {
          '_id': {},
          'last_name': {
            'bsonType':
            'string',
            'description':
            'A textstring that describes the surname of a student.'
          },
          'first_name': {
            'bsonType': 'string',
            'description': 'A textstring that the student is known by.'
          },
          'email': {
            'bsonType': 'string',
            'description': 'A textstring of the students contact.'
          },
          'student_majors': {
            'bsonType': 'array',
            'items': {
              'bsonType': 'object',
              'required': ['stud_major_id', 'major_name'],
              'additionalProperties': False,
              'properties': {
                'stud_major_id': {
                  'bsonType': 'objectId'
                },
                'major_name': {
                  'bsonType': 'string'
                }
              }
            }
          },
          'enrollments': {
            'bsonType': 'array',
            'items': {
              'bsonType': 'object',
              'required': ['enrollment_id', 'department_abbr', 'course_num'],
              'additionalProperties': False,
              'properties': {
                'enrollment_id': {
                  'bsonType': 'objectId'
                },
                'department_abbr': {
                  'bsonType': 'string'
                },
                'course_num': {
                  'bsonType': 'int'
                }
              }
            }
          }
        }
      }
    }

  if collection_name == 'sections':

    validate = {
      "$jsonSchema": {
        "bsonType":
        "object",
        "required": [
          'section_number', 'semester', 'section_year', 'building', 'room',
          'schedule', 'start_time', 'instructor', 'department_abbr',
          'course_num', 'enrollments'
        ],
        'additionalProperties':
        False,
        "properties": {
          '_id': {},
          'section_number': {
            'bsonType': 'int'
          },
          'semester': {
            'bsonType':
            'string',
            'enum': [
              'Fall', 'Spring', 'Summer I', 'Summer II', 'Summer III', 'Winter'
            ]
          },
          'section_year': {
            'bsonType': 'int'
          },
          'building': {
            'bsonType':
            'string',
            'enum': [
              'ANAC', 'CDC', 'DC', 'ECS', 'EN2', 'EN3', 'EN4', 'EN5', 'ET',
              'HSCI', 'NUR', 'VEC'
            ]
          },
          'room': {
            'bsonType': 'int',
            'minimum': 1,
            'maximum': 999
          },
          'schedule': {
            'bsonType': 'string',
            'enum': ['MW', 'TuTh', 'MWF', 'F', 'S']
          },
          'start_time': {
            'bsonType': 'object',
            'required': ['hour', 'minute'],
            'additionalProperties': False,
            'properties': {
              'hour': {
                'bsonType': 'int',
                'minimum': 8,
                'maximum': 19
              },
              'minute': {
                'bsonType': 'int',
                'minimum': 0,
                'maximum': 59
              }
            }
          },
          'instructor': {
            'bsonType': 'string',
          },
          'department_abbr': {
            'bsonType': 'string'
          },
          'course_num': {
            'bsonType': 'int'
          },
          'enrollments': {
            'bsonType': 'array',
            'items': {
              'bsonType': 'objectId'
            }
          }
        }
      }
    }

  if collection_name == 'student_majors':

    validate = {
      '$jsonSchema': {
        'bsonType': 'object',
        'required': ['major_name', 'student_id', 'declaration_date'],
        'additionalProperties': False,
        'properties': {
          'major_name': {
            'bsonType': 'string'
          },
          'student_id': {
            'bsonType': 'objectId'
          },
          'declaration_date': {
            'bsonType': 'date'
          }
        }
      }
    }

  if collection_name == 'enrollments':

    validate = {
      '$jsonSchema': {
        'bsonType':
        'object',
        'required': [
          'student_id', 'department_abbr', 'course_num', 'semester',
          'sec_year', 'sec_num'
        ],
        'additionalProperties':
        False,
        'properties': {
          '_id': {},
          'student_id': {
            'bsonType': 'objectId',
          },
          'department_abbr': {
            'bsonType': 'string'
          },
          'course_num': {
            'bsonType': 'int'
          },
          'semester': {
            'bsonType': 'string'
          },
          'sec_year': {
            'bsonType': 'int'
          },
          'sec_num': {
            'bsonType': 'int'
          },
          'category_data': {
            'oneOf': [{
              'bsonType': 'object',
              'required': ['month', 'day', 'year'],
              'additionalProperties': False,
              'properties': {
                'month': {
                  'bsonType': 'int'
                },
                'day': {
                  'bsonType': 'int'
                },
                'year': {
                  'bsonType': 'int'
                }
              }
            }, {
              'bsonType': 'object',
              'required': ['min_satisfactory'],
              'additionalProperties': False,
              'properties': {
                'min_satisfactory': {
                  'bsonType': 'string',
                  'enum': ['A', 'B', 'C']
                }
              }
            }]
          }
        }
      }
    }

  return validate


def unique_constraints(collection_name: str):
  """Enforces constraints when called with the collection name."""

  if collection_name == 'departments':

    departments_indexes = departments.index_information()

    if 'departments_name' in departments_indexes.keys():
      print("name index present.")
    else:
      departments.create_index([('name', pymongo.ASCENDING)],
                               unique=True,
                               name="departments_name")
    if 'departments_abbreviation' in departments_indexes.keys():
      print("abbreviation index present.")
    else:
      departments.create_index([('abbreviation', pymongo.ASCENDING)],
                               unique=True,
                               name='departments_abbreviation')
    if 'departments_chair_name' in departments_indexes.keys():
      print("chair name index present.")
    else:
      departments.create_index([('chair_name', pymongo.ASCENDING)],
                               unique=True,
                               name='departments_chair_name')
    if 'departments_building_and_office' in departments_indexes.keys():
      print("building and office index present.")
    else:
      departments.create_index([('building', pymongo.ASCENDING),
                                ('office', pymongo.ASCENDING)],
                               unique=True,
                               name='departments_building_and_office')

  if collection_name == 'majors':

    majors_indexes = majors.index_information()

    if 'majors_name' in majors_indexes.keys():
      print("name index present.")
    else:
      majors.create_index([('name', pymongo.ASCENDING)],
                          unique=True,
                          name="majors_name")

  if collection_name == 'courses':

    courses_indexes = courses.index_information()

    if 'department_abbr_and_course_num' in courses_indexes.keys():
      print('dept abbr and course num index present.')
    else:
      courses.create_index([('department_abbr', pymongo.ASCENDING),
                            ('course_number', pymongo.ASCENDING)],
                           unique=True,
                           name='department_abbr_and_course_num')
    if 'department_abbr_and_course_name' in courses_indexes.keys():
      print('dept abbr and course name index present.')
    else:
      courses.create_index([('department_abbr', pymongo.ASCENDING),
                            ('course_name', pymongo.ASCENDING)],
                           unique=True,
                           name='department_abbr_and_course_name')

  if collection_name == 'sections':

    sections_indexes = sections.index_information()

    if 'dept_course_secNum_sem_secYear' in sections_indexes.keys():
      print('dept_course_secNum_sem_secYear index is present.')
    else:
      sections.create_index([('department_abbr', pymongo.ASCENDING),
                             ('course_num', pymongo.ASCENDING),
                             ('section_number', pymongo.ASCENDING),
                             ('semester', pymongo.ASCENDING),
                             ('section_year', pymongo.ASCENDING)],
                            unique=True,
                            name='dept_course_secNum_sem_secYear')
    if 'sem_secYear_build_room_sched_start' in sections_indexes.keys():
      print('sem_secYear_build_room_sched_start index is present.')
    else:
      sections.create_index([('semester', pymongo.ASCENDING),
                             ('section_year', pymongo.ASCENDING),
                             ('building', pymongo.ASCENDING),
                             ('room', pymongo.ASCENDING),
                             ('schedule', pymongo.ASCENDING),
                             ('start_time', pymongo.ASCENDING)],
                            unique=True,
                            name='sem_secYear_build_room_sched_start')
    if 'sem_secYear_sched_start_instruct' in sections_indexes.keys():
      print('sem_secYear_sched_start_instruct index is present.')
    else:
      sections.create_index([('semester', pymongo.ASCENDING),
                             ('section_year', pymongo.ASCENDING),
                             ('schedule', pymongo.ASCENDING),
                             ('start_time', pymongo.ASCENDING),
                             ('instructor', pymongo.ASCENDING)],
                            unique=True,
                            name='sem_secYear_sched_start_instruct')

  if collection_name == 'students':

    students_indexes = students.index_information()

    if 'last_first' in students_indexes.keys():
      print('last_first index is present.')
    else:
      students.create_index([('first_name', pymongo.ASCENDING),
                             ('last_name', pymongo.ASCENDING)],
                            unique=True,
                            name='last_first')
    if 'email' in students_indexes.keys():
      print('email index is present.')
    else:
      students.create_index([('email', pymongo.ASCENDING)],
                            unique=True,
                            name='email')

  if collection_name == 'student_majors':

    studentmajors_indexes = studentmajors.index_information()

    if 'student_major' in studentmajors_indexes.keys():
      print('student_majors index is present.')
    else:
      studentmajors.create_index([('student_id', pymongo.ASCENDING),
                                  ('major_name', pymongo.ASCENDING)],
                                 unique=True,
                                 name='student_major')

  if collection_name == 'enrollments':

    enrollments_indexes = enrollments.index_information()

    if 'student_section' in enrollments_indexes.keys():
      print('student_section index is present.')
    else:
      enrollments.create_index([('student_id', pymongo.ASCENDING),
                                ('department_abbr', pymongo.ASCENDING),
                                ('course_num', pymongo.ASCENDING),
                                ('sec_num', pymongo.ASCENDING),
                                ('semester', pymongo.ASCENDING),
                                ('sec_year', pymongo.ASCENDING)],
                               unique=True,
                               name='student_section')
    if 'stu_dept_course_sem_year' in enrollments_indexes.keys():
      print('stu_dept_course_sem_year index is present.')
    else:
      enrollments.create_index([('student_id', pymongo.ASCENDING),
                                ('department_abbr', pymongo.ASCENDING),
                                ('course_num', pymongo.ASCENDING),
                                ('semester', pymongo.ASCENDING),
                                ('sec_year', pymongo.ASCENDING)],
                               unique=True,
                               name='stu_dept_course_sem_year')


# Adding to a collection
def add_department(db):

  collection = db["departments"]

  error = True

  while error:

    name = input('Department Name -> ')
    abbreviation = input('Department Abbreviation -> ')
    chair_name = input('Department Chair Name -> ')
    building = input('Department Building -> ')
    office = int(input('Department Office -> '))
    description = input('Department Description -> ')

    department = {
      "name": name,
      "abbreviation": abbreviation,
      "chair_name": chair_name,
      "building": building,
      "office": office,
      "description": description,
      "courses": [],
      "majors": []
    }

    try:
      collection.insert_one(department)
      error = False
    except Exception as error_msg:
      pprint(f'\n{error_msg}')
      print('\nInvalid Data. Please try again.\n')


def add_major(db):

  print('Select the department that the major is a part of: ')
  department = select_department(db)

  collection = db["majors"]

  error = True

  while error:

    name = input('Major Name -> ')
    description = input('Major Description -> ')

    major = {
      "name": name,
      "description": description,
      "department": department.get('_id'),
      'student_majors': []
    }

    try:
      collection.insert_one(major)
      error = False
    except Exception as error_msg:
      pprint(f'\n{error_msg}')
      print('\nInvalid Data. Please try again.\n')

  # Appends the major id to the majors array in department
  db['departments'].update_many(
    {'abbreviation': department.get('abbreviation')},
    {'$push': {
      'majors': collection.find_one({
        "name": name
      }).get('_id')
    }})


def add_student(db):

  collection = db["students"]

  error = True

  while error:

    last_name = input('Student\'s Last Name ->')
    first_name = input('Student\'s First Name ->')
    email = input('Student\'s Email Address ->')

    student = {
      "last_name": last_name,
      "first_name": first_name,
      "email": email,
      'student_majors': [],
      'enrollments': []
    }

    try:
      collection.insert_one(student)
      error = False
    except Exception as error_msg:
      pprint(f'\n{error_msg}')
      print('\nInvalid Data. Please try again.\n')


def add_course(db):

  print('Select the department that the course is a part of: ')
  department = select_department(db)

  collection = db["courses"]

  error = True

  while error:

    course_number = int(input('Course Number -> '))
    course_name = input('Course Name -> ')
    description = input('Course Description -> ')
    units = int(input('Course Units -> '))

    course = {
      'course_number': course_number,
      'course_name': course_name,
      'description': description,
      'units': units,
      'department_abbr': department.get('abbreviation'),
      'sections': []
    }

    try:
      collection.insert_one(course)
      error = False
    except Exception as error_msg:
      pprint(f'\n{error_msg}')
      print('\nInvalid Data. Please try again.\n')

  # Appends the course id to the courses array in department
  db['departments'].update_many(
    {'abbreviation': department.get('abbreviation')}, {
      '$push': {
        'courses':
        collection.find_one({
          'department_abbr': department.get('abbreviation'),
          'course_number': course_number
        }).get('_id')
      }
    })


def add_section(db):

  collection = db["sections"]
  print('Select the course that this section is a part of: ')

  error = True

  while error:

    course = select_course(db)

    sec_num = int(input('Section Number-> '))
    semester = input('Semester-> ')
    sec_year = int(input('Section Year-> '))
    building = input('Building-> ')
    room = int(input('Room-> '))
    schedule = input('Schedule-> ')
    start_time = input('Start Time-> ')
    instructor = input('Instructor-> ')

    section = {
      'section_number': sec_num,
      'semester': semester,
      'section_year': sec_year,
      'building': building,
      'room': room,
      'schedule': schedule,
      'start_time': {
        'hour': int(start_time[0:2]),
        'minute': int(start_time[3:5])
      },
      'instructor': instructor,
      'department_abbr': course['department_abbr'],
      'course_num': course['course_number'],
      'enrollments': []
    }

    try:
      collection.insert_one(section)
      error = False
    except Exception as error_msg:
      pprint(f'\n{error_msg}')
      print('\nInvalid Data. Please try again.\n')

  db['courses'].update_many(
    {
      'department_abbr': course.get('department_abbr'),
      'course_number': course.get('course_number')
    }, {
      '$push': {
        'sections':
        collection.find_one({
          'department_abbr': course.get('department_abbr'),
          'course_num': course.get('course_number'),
          'section_number': sec_num,
          'semester': semester,
          'section_year': sec_year
        }).get('_id')
      }
    })


def add_student_major(db):

  collection = db['studentmajors']

  error = True

  while error:

    print('Please select the student that is declaring a major.')
    student = select_student(db)
    print('Please select the major that the student is declaring.')
    major = select_major(db)

    student_major = {
      'major_name': major['name'],
      'student_id': student['_id'],
      'declaration_date': datetime.date.today().isoformat()
    }

    try:
      collection.insert_one(student_major)
      error = False
    except Exception as error_msg:
      pprint(f'\n{error_msg}')
      print('\nInvalid Data. Please try again.\n')

  db['majors'].update_many({'name': major['name']}, {
    '$push': {
      'student_majors':
      collection.find_one({
        'major_name': major['name'],
        'student_id': student['_id']
      }).get('_id')
    }
  })

  db['students'].update_many({'_id': student['_id']}, {
    '$push': {
      'student_majors': {
        'stud_major_id': (collection.find_one({
          'major_name': major['name'],
          'student_id': student['_id']
        }).get('_id')),
        'major_name': (collection.find_one({
          'major_name': major['name'],
          'student_id': student['_id']
        }).get('major_name'))
      }
    }
  })


def add_enrollment(db):

  collection = db['enrollments']

  error = True

  while error:
    print('Please select the student that is enrolling in a section.')
    student = select_student(db)
    print('Please select the section the student is enrolling in.')
    section = select_section(db)

    while True:
      grading_type = int(
        input('Please choose one:\n  1. Pass/Fail\n  2. Letter Grade\n'))
      if grading_type == 1 or grading_type == 2:
        break
      else:
        print(
          'That is not a valid option, please choose one of the listed options.'
        )

    if grading_type == 1:
      enrollment = {
        'student_id': student['_id'],
        'department_abbr': section['department_abbr'],
        'course_num': section['course_num'],
        'semester': section['semester'],
        'sec_year': section['section_year'],
        'sec_num': section['section_number'],
        'category_data': {
          'month': int(datetime.date.today().month),
          'day': int(datetime.date.today().day),
          'year': int(datetime.date.today().year)
        }
      }
    if grading_type == 2:
      data = input('Please input the minimum satisfactory grade: ')

      enrollment = {
        'student_id': student['_id'],
        'department_abbr': section['department_abbr'],
        'course_num': section['course_num'],
        'semester': section['semester'],
        'sec_year': section['section_year'],
        'sec_num': section['section_number'],
        'category_data': {
          'min_satisfactory': data
        }
      }

    try:
      collection.insert_one(enrollment)
      error = False
    except Exception as error_msg:
      pprint(f'\n{error_msg}')
      print('\nInvalid Data. Please try again.\n')

  db['sections'].update_many(
    {
      'department_abbr': section['department_abbr'],
      'course_num': section['course_num'],
      'semester': section['semester'],
      'section_year': section['section_year'],
      'section_number': section['section_number']
    }, {
      '$push': {
        'enrollments':
        collection.find_one({
          'student_id': student['_id'],
          'department_abbr': section['department_abbr'],
          'course_num': section['course_num'],
          'semester': section['semester'],
          'sec_year': section['section_year'],
          'sec_num': section['section_number']
        }).get('_id')
      }
    })

  db['students'].update_many({'_id': student['_id']}, {
    '$push': {
      'enrollments': {
        'enrollment_id':
        collection.find_one({
          'student_id': student['_id'],
          'department_abbr': section['department_abbr'],
          'course_num': section['course_num'],
          'semester': section['semester'],
          'sec_year': section['section_year'],
          'sec_num': section['section_number']
        }).get('_id'),
        'department_abbr':
        collection.find_one({
          'student_id': student['_id'],
          'department_abbr': section['department_abbr'],
          'course_num': section['course_num'],
          'semester': section['semester'],
          'sec_year': section['section_year'],
          'sec_num': section['section_number']
        }).get('department_abbr'),
        'course_num':
        collection.find_one({
          'student_id': student['_id'],
          'department_abbr': section['department_abbr'],
          'course_num': section['course_num'],
          'semester': section['semester'],
          'sec_year': section['section_year'],
          'sec_num': section['section_number']
        }).get('course_num')
      }
    }
  })


# Deleting from a collection
def delete_department(db):
  """
  Delete a deparment from the database.
  :param db:  The current database connection.
  :return:    None
  """
  department = select_department(db)
  departments = db["departments"]

  for major_id in department['majors']:
    major_doc = db['majors'].find_one({'_id': major_id})
    for studentmajor_id in major_doc['student_majors']:
      studentmajor_doc = db['studentmajors'].find_one({'_id': studentmajor_id})
      student = db['students'].find_one(
        {'_id': studentmajor_doc['student_id']})

      db['students'].update_many({'_id': student['_id']}, {
        '$pull': {
          'student_majors': {
            'stud_major_id': studentmajor_doc['_id'],
            'major_name': studentmajor_doc['major_name']
          }
        }
      })
      db['studentmajors'].delete_one({'_id': studentmajor_doc['_id']})
    db['majors'].delete_one({'_id': major_doc['_id']})

  for course_id in department['courses']:
    course_doc = db['courses'].find_one({'_id': course_id})
    for section_id in course_doc['sections']:
      section_doc = db['sections'].find_one({'_id': section_id})
      for enrollment_id in section_doc['enrollments']:
        enrollment_doc = db['enrollments'].find_one({'_id': enrollment_id})
        student = db['students'].find_one(
          {'_id': enrollment_doc['student_id']})

        db['students'].update_many({'_id': student['_id']}, {
          '$pull': {
            'enrollments': {
              'enrollment_id': enrollment_doc['_id'],
              'department_abbr': enrollment_doc['department_abbr'],
              'course_num': enrollment_doc['course_num']
            }
          }
        })
        db['enrollments'].delete_one({'_id': enrollment_doc['_id']})
      db['sections'].delete_one({'_id': section_doc['_id']})
    db['courses'].delete_one({'_id': course_id})

  deleted = departments.delete_one({"_id": department["_id"]})
  print(f"\nWe just deleted: {deleted.deleted_count} departments.\n")


def delete_major(db):

  major = select_major(db)
  majors = db['majors']
  department = db['departments'].find_one({'_id': major['department']})

  for studentmajor_id in major['student_majors']:
    studentmajor_doc = db['studentmajors'].find_one({'_id': studentmajor_id})
    student = db['students'].find_one({'_id': studentmajor_doc['student_id']})

    db['students'].update_many({'_id': student['_id']}, {
      '$pull': {
        'student_majors': {
          'stud_major_id': studentmajor_doc['_id'],
          'major_name': studentmajor_doc['major_name']
        }
      }
    })
    db['studentmajors'].delete_one({'_id': studentmajor_doc['_id']})

  deleted = majors.delete_one({'_id': major['_id']})

  db['departments'].update_many(
    {'abbreviation': department.get('abbreviation')},
    {'$pull': {
      'majors': major['_id']
    }})

  print(f"\nWe just deleted: {deleted.deleted_count} majors.\n")


def delete_student(db):
  student = select_student(db)
  students = db['students']

  for studentmajor_obj in student['student_majors']:
    studentmajor_doc = db['studentmajors'].find_one(
      {'_id': studentmajor_obj.get('stud_major_id')})

    db['majors'].update_many(
      {'name': studentmajor_doc['major_name']},
      {'$pull': {
        'student_majors': studentmajor_doc['_id']
      }})
    db['studentmajors'].delete_one({'_id': studentmajor_doc['_id']})

  for enrollment_obj in student['enrollments']:
    enrollment_doc = db['enrollments'].find_one(
      {'_id': enrollment_obj.get('enrollment_id')})

    db['sections'].update_many(
      {
        'department_abbr': enrollment_doc['department_abbr'],
        'course_num': enrollment_doc['course_num'],
        'section_number': enrollment_doc['sec_num'],
        'semester': enrollment_doc['semester'],
        'section_year': enrollment_doc['sec_year']
      }, {'$pull': {
        'enrollments': enrollment_doc['_id']
      }})
    db['enrollments'].delete_one({'_id': enrollment_doc['_id']})

  deleted = students.delete_one({'_id': student['_id']})

  print(f"\nWe just deleted: {deleted.deleted_count} students.\n")


def delete_course(db):

  course = select_course(db)
  courses = db['courses']
  department = db['departments'].find_one(
    {'abbreviation': course['department_abbr']})

  for section_id in course['sections']:
    section_doc = db['sections'].find_one({'_id': section_id})
    for enrollment_id in section_doc['enrollments']:
      enrollment_doc = db['enrollments'].find_one({'_id': enrollment_id})
      student = db['students'].find_one({'_id': enrollment_doc['student_id']})

      db['students'].update_many({'_id': student['_id']}, {
        '$pull': {
          'enrollments': {
            'enrollment_id': enrollment_doc['_id'],
            'department_abbr': enrollment_doc['department_abbr'],
            'course_num': enrollment_doc['course_num']
          }
        }
      })
      db['enrollments'].delete_one({'_id': enrollment_doc['_id']})
    db['sections'].delete_one({'_id': section_doc['_id']})

  deleted = courses.delete_one({'_id': course['_id']})

  db['departments'].update_many(
    {'abbreviation': department.get('abbreviation')},
    {'$pull': {
      'courses': course['_id']
    }})

  print(f"\nWe just deleted: {deleted.deleted_count} courses.\n")


def delete_section(db):

  section = select_section(db)
  sections = db['sections']
  course = db['courses'].find_one({
    'department_abbr': section['department_abbr'],
    'course_number': section['course_num']
  })

  for enrollment_id in section['enrollments']:
    enrollment_doc = db['enrollments'].find_one({'_id': enrollment_id})
    student = db['students'].find_one({'_id': enrollment_doc['student_id']})

    db['students'].update_many({'_id': student['_id']}, {
      '$pull': {
        'enrollments': {
          'enrollment_id': enrollment_doc['_id'],
          'department_abbr': enrollment_doc['department_abbr'],
          'course_num': enrollment_doc['course_num']
        }
      }
    })
    db['enrollments'].delete_one({'_id': enrollment_doc['_id']})

  deleted = sections.delete_one({'_id': section['_id']})

  db['courses'].update_many(
    {
      'department_abbr': course.get('department_abbr'),
      'course_number': course.get('course_number')
    }, {'$pull': {
      'sections': section['_id']
    }})
  print(f"\nWe just deleted: {deleted.deleted_count} sections.\n")


def delete_student_major(db):

  print('Select the student that is undeclaring the major: ')
  student = select_student(db)
  print('Select the major the student is undeclaring: ')
  major = select_major(db)

  studentmajor = db['studentmajors'].find_one({
    'student_id': student['_id'],
    'major_name': major['name']
  })
  studentmajors = db['studentmajors']

  db['students'].update_many({'_id': student['_id']}, {
    '$pull': {
      'student_majors': {
        'stud_major_id': studentmajor['_id'],
        'major_name': studentmajor['major_name']
      }
    }
  })
  db['majors'].update_many({'name': studentmajor['major_name']},
                           {'$pull': {
                             'student_majors': studentmajor['_id']
                           }})

  deleted = studentmajors.delete_one({'_id': studentmajor['_id']})
  print(f"\nWe just deleted: {deleted.deleted_count} studentmajors.\n")


def delete_enrollment(db):

  print('Select the student that is unenrolling from the section: ')
  student = select_student(db)
  print('Select the section the student is unenrolling from: ')
  section = select_section(db)

  enrollment = db['enrollments'].find_one({
    'student_id':
    student['_id'],
    'department_abbr':
    section['department_abbr'],
    'course_num':
    section['course_num'],
    'sec_num':
    section['section_number'],
    'semester':
    section['semester'],
    'sec_year':
    section['section_year']
  })
  enrollments = db['enrollments']

  db['students'].update_many({'_id': student['_id']}, {
    '$pull': {
      'enrollments': {
        'enrollment_id': enrollment['_id'],
        'department_abbr': enrollment['department_abbr'],
        'course_num': enrollment['course_num']
      }
    }
  })
  db['sections'].update_many(
    {
      'department_abbr': enrollment['department_abbr'],
      'course_num': enrollment['course_num'],
      'section_number': enrollment['sec_num'],
      'semester': enrollment['semester'],
      'section_year': enrollment['sec_year']
    }, {'$pull': {
      'enrollments': enrollment['_id']
    }})

  deleted = enrollments.delete_one({'_id': enrollment['_id']})
  print(f"\nWe just deleted: {deleted.deleted_count} enrollments.\n")


# List docs from a collection
def list_department(db):
  """
  List all of the students, sorted by last name first, then the first name.
  :param db:  The current connection to the MongoDB database.
  :return:    None
  """
  # No real point in creating a pointer to the collection, I'm only using it
  # once in here.  The {} inside the find simply tells the find that I have
  # no criteria.  Essentially this is analogous to a SQL find * from departments.
  # Each tuple in the sort specification has the name of the field, followed
  # by the specification of ascending versus descending.
  departments = db["departments"].find({}).sort([("name", pymongo.ASCENDING)])
  # pretty print is good enough for this work.  It doesn't have to win a beauty contest.
  for department in departments:
    print()
    pprint(department)
  print()


def list_major(db):

  majors = db['majors'].find({}).sort([('name', pymongo.ASCENDING)])

  for major in majors:
    print()
    pprint(major)
  print()


def list_student(db):
  students = db['students'].find({}).sort([('last_name', pymongo.ASCENDING),
                                           ("first_name", pymongo.ASCENDING)])

  for student in students:
    print()
    pprint(student)
  print()


def list_course(db):

  courses = db['courses'].find({}).sort([('course_number', pymongo.ASCENDING)])

  for course in courses:
    print()
    pprint(course)
  print()


def list_section(db):
  sections = db['sections'].find({}).sort([('section_number',
                                            pymongo.ASCENDING)])

  for section in sections:
    print()
    pprint(section)
  print()


def list_student_in_major(db):
    major_name = input(
    "Please input the major you would like to select from--> ")
    majors = db['studentmajors'].find({'major_name': major_name})
    for major in majors:
        student_id = major['student_id']
        student = db['students'].find_one({'_id': student_id})
        print()
        pprint(student)
    print()



def list_major_for_student(db):
    student = select_student(db)
    student_id = student['_id']
    student_majors = db['studentmajors'].find({'student_id':student_id})
    for student_major in student_majors:
        major_name = student_major['major_name']
        major = db['majors'].find_one({'name':major_name})
        print()
        pprint(major)
    print()



def list_sections_of_student(db):
    student = select_student(db)
    student_id = student['_id']
    enrollments = db['enrollments'].find({'student_id':student_id})
    for enrollment in enrollments:
        print()
        pprint(enrollment)
    print()



def list_students_in_section(db):
    section = select_section(db)
    department_abbreviation = section['department_abbr']
    course_num = section['course_num']
    section_number = section['section_number']
    enrollments = db['enrollments'].find({
        'department_abbr':department_abbreviation,
        'course_num':course_num,
        'sec_num':section_number
        })
    for enrollment in enrollments:
        student_id = enrollment['student_id']
        student = db['students'].find_one({'_id':student_id})
        print()
        pprint(student)
    print()



# Selectors, background usage
def select_department(db):
  """
    Select a department by the Department Abbreviation
    :param db:      The connection to the database.
    :return:        The selected department as a dict.  This is not the same as it was
                    in SQLAlchemy, it is just a copy of the Student document from
                    the database.
    """
  # Create a connection to the students collection from this database
  collection = db["departments"]
  found: bool = False
  department_abbreviation: str = ''
  while not found:
    department_abbreviation = input("Department abbreviation--> ")
    department_abbreviation_count: int = collection.count_documents(
      {"abbreviation": department_abbreviation})
    found = department_abbreviation_count == 1
    if not found:
      print("No department found by that abbreviation.  Try again.")
  found_department = collection.find_one(
    {"abbreviation": department_abbreviation})
  return found_department


def select_major(db):

  collection = db["majors"]

  found: bool = False
  major_name: str = ''

  while not found:

    major_name = input("Major Name--> ")
    major_count: int = collection.count_documents({"name": major_name})
    found = major_count == 1
    if not found:
      print("No major found by that name. Please try again.")

  found_major = collection.find_one({"name": major_name})
  return found_major


def select_student(db):

  collection = db["students"]

  found: bool = False

  while not found:

    last_name = input("Student's Last Name--> ")
    first_name = input("Student's First Name--> ")

    student_count = collection.count_documents({
      'first_name': first_name,
      'last_name': last_name
    })

    found = student_count == 1

    if not found:
      print("No student found by that name. Please try again.")

  found_student = collection.find_one({
    'first_name': first_name,
    'last_name': last_name
  })

  return found_student


def select_course(db):

  collection = db["courses"]

  found: bool = False

  while not found:

    department = select_department(db)
    course_num = int(input("Course Number--> "))
    course_count: int = collection.count_documents({
      'course_number':
      course_num,
      'department_abbr':
      department['abbreviation']
    })
    found = course_count == 1
    if not found:
      print(
        "No course found in that department with that number. Please try again."
      )

  found_course = collection.find_one({
    "course_number":
    course_num,
    'department_abbr':
    department['abbreviation']
  })
  return found_course


def select_section(db):

  course = select_course(db)

  collection = db["sections"]

  found: bool = False

  while not found:

    section_num = int(input("Section Number --> "))
    semester = input('Semester--> ')
    sec_year = int(input('Section Year--> '))

    section_count: int = collection.count_documents({
      'section_number':
      section_num,
      'course_num':
      course['course_number'],
      'department_abbr':
      course['department_abbr'],
      'semester':
      semester,
      'section_year':
      sec_year
    })

    found = section_count == 1
    if not found:
      print(
        "No section of that number found in this course and department. Try again."
      )

  found_course = collection.find_one({
    'section_number':
    section_num,
    'course_num':
    course['course_number'],
    'department_abbr':
    course['department_abbr'],
    'semester':
    semester,
    'section_year':
    sec_year
  })

  return found_course


if __name__ == '__main__':  # Won't run if IP not allowed on atlas, network access -> access from anywhere
  password: str = getpass.getpass('Mongo DB password -->')
  username: str = input(
    'Database username [username] -->') or "username"  # replace username
  project: str = input(
    'Mongo project name [projname] -->') or "projname"  # replace projname
  hash_name: str = input(
    '7-character database hash [hash] -->') or "hash"  # replace hash

  cluster = f"mongodb+srv://{username}:{password}@{project}.{hash_name}.mongodb.net/retryWrites=true&w=majority&authSource=admin"
  print(
    f"Cluster: mongodb+srv://{username}:<password>@{project}.{hash_name}.mongodb.net/?retryWrites=true&w=majority&authSource=admin"
  )

  client = MongoClient(cluster)
  print(client.list_database_names())

  db = client["EnrollmentProject"]  # Database names
  print(db.list_collection_names())

  collections = [
    'departments', 'majors', 'students', 'courses', 'sections',
    'studentmajors', 'enrollments'
  ]

  for i in collections:  # Creates the collections
    try:  # For error when creating existing collection
      db.create_collection(i)
    except Exception:
      print(f'The collection, {i}, exists.')

  departments = db["departments"]  # Exists on data insert
  majors = db["majors"]
  students = db["students"]
  courses = db["courses"]
  sections = db["sections"]
  studentmajors = db["studentmajors"]
  enrollments = db["enrollments"]

  for j in collections:  # Puts a validator on all the collections, None if there isn't one in the validator function
    db.command('collMod', j, validator=validator(
      j))  # doesn't work with prev lines if no data/new coll

  for k in collections:
    unique_constraints(k)

  main_action: str = ''
  while main_action != menu_main.last_action():
    main_action = menu_main.menu_prompt()
    print('next action: ', main_action)
    exec(main_action)
