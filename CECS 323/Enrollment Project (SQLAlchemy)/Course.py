from orm_base import Base
from sqlalchemy import Integer, UniqueConstraint, ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from Department import Department
from typing import List


class Course(Base):
    """A catalog entry.  Each course proposes to offer students who enroll in
    a section of the course an organized sequence of lessons and assignments
    aimed at teaching them specified skills."""
    __tablename__ = "courses"  # Give SQLAlchemy th name of the table.

    departmentAbbreviation: Mapped[str] = mapped_column('department_abbreviation', ForeignKey("departments.abbreviation"), primary_key=True)
    courseNumber: Mapped[int] = mapped_column('course_number', Integer, nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column('name', String(50), nullable=False)
    description: Mapped[str] = mapped_column('description', String(500), nullable=False)
    units: Mapped[int] = mapped_column('units', Integer, nullable=False)

    department: Mapped["Department"] = relationship(back_populates="courses")
    sections: Mapped[List["Section"]] = relationship(back_populates="course")

    # __table_args__ can best be viewed as directives that we ask SQLAlchemy to
    # send to the database.  In this case, that we want two separate uniqueness
    # constraints (candidate keys).
    __table_args__ = (UniqueConstraint("department_abbreviation", "name", name="courses_uk_01"),)

    def __init__(self, department: Department, courseNumber: int, name: str, description: str, units: int):
        self.set_department(department)
        self.courseNumber = courseNumber
        self.name = name
        self.description = description
        self.units = units

    def set_department(self, department: Department):
        """
        Accept a new department withoug checking for any uniqueness.
        I'm going to assume that either a) the caller checked that first
        and/or b) the database will raise its own exception.
        :param department:  The new department for the course.
        :return:            None
        """
        self.department = department
        self.departmentAbbreviation = department.abbreviation

    def add_section(self, section):
        if section not in self.sections:
            self.sections.add(section)

    def remove_section(self, section):
        if section in self.sections:
            self.sections.remove(section)

    def get_sections(self):
        return self.sections

    def __str__(self):
        return f"Department abbrev: {self.departmentAbbreviation} number: {self.courseNumber} name: {self.name} units: {self.units}"
