from orm_base import Base
from sqlalchemy import Integer, UniqueConstraint, ForeignKey, ForeignKeyConstraint
from sqlalchemy import String, Integer, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Enrollment(Base):
    """
    A registration of a student into a course.
    """

    __tablename__ = "enrollments"

    # Relations
    section: Mapped["Section"] = relationship(back_populates="students")
    student: Mapped["Student"] = relationship(back_populates="sections")

    # From section and student
    section_id: Mapped[int] = mapped_column('section_id', ForeignKey("sections.section_id"), nullable=False, primary_key=True)
    studentID: Mapped[int] = mapped_column('student_id', ForeignKey("students.student_id"), nullable=False, primary_key=True)

    type: Mapped[str] = mapped_column("type", String(50), nullable=False)

    __mapper_args__ = {"polymorphic_identity": "enrollment",
                       "polymorphic_on": "type"}

    def __init__(self, section, student):
        self.set_section(section)
        self.set_student(student)

    def set_section(self, section):
        self.section = section
        self.section_id = section.section_id

    def set_student(self, student):
        self.student = student
        self.studentID = student.studentId

    def __str__(self):
        return f'Student:\n{self.student}' \
               f'\n---enrolled in---\n' \
               f'Section:\n{self.section}'
