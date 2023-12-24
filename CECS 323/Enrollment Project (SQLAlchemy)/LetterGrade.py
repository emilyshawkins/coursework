from sqlalchemy import ForeignKeyConstraint, CheckConstraint
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from Enrollment import Enrollment


class LetterGrade(Enrollment):
    __tablename__ = "letter_grade"

    studentID: Mapped[int] = mapped_column('student_id', Integer, nullable=False, primary_key=True)
    sectionID: Mapped[int] = mapped_column('section_id', Integer, nullable=False, primary_key=True)
    grade: Mapped[str] = mapped_column('grade', String(1), CheckConstraint("grade IN ('A', 'B', 'C', 'D', 'F')"), nullable=False)

    __tableargs__ = (ForeignKeyConstraint([studentID, sectionID], [Enrollment.studentID, Enrollment.section_id], ondelete="CASCADE"))

    __mapper_args__ = {"polymorphic_identity": "letter_grade"}

    def __init__(self, section, student, grade: str):
        super().__init__(section, student)
        self.grade = grade

    def __str__(self):
        return f"\nLetter Grade Enrollment: \n{super().__str__()}"
