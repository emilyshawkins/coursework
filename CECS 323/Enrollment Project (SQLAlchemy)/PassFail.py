from sqlalchemy import Date, Integer, ForeignKeyConstraint
from sqlalchemy.orm import mapped_column, Mapped
from Enrollment import Enrollment


class PassFail(Enrollment):
    __tablename__ = "pass_fail"

    studentID: Mapped[int] = mapped_column('student_id', Integer, nullable=False, primary_key=True)
    sectionID: Mapped[int] = mapped_column('section_id', Integer, nullable=False, primary_key=True)
    applicationDate: Mapped[Date] = mapped_column('application_date', Date, nullable=False)

    __tableargs__ = (ForeignKeyConstraint([studentID, sectionID], [Enrollment.studentID, Enrollment.section_id], ondelete="CASCADE"))

    __mapper_args__ = {"polymorphic_identity": "pass_fail"}

    def __init__(self, section, student, application_date: Date):
        super().__init__(section, student)
        self.applicationDate = application_date

    def __str__(self):
        return f"\nPass Fail Enrollment: \n{super().__str__()}"
