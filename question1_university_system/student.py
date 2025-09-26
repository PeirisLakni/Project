from __future__ import annotations
from typing import Dict, List, Tuple, Optional, Set
from person import Person #import base class Person

#GPA Calculation across multiple semesters
#A helper class SecureStudentRecord (keeps a student’s grades, GPA, and current enrollments safe and private).

GradeEntry = Tuple[str, int, str]  # creating a tuple to store (course_code, credits, letter_grade) in one code

LETTER_TO_GPA = {
    "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7, "D": 1.0, "F": 0.0
}

#setting up enrollment limit for 5 courses
class SecureStudentRecord:
    def __init__(self, enrollment_limit: int = 5) -> None: 
        self.__gpa: float = 0.0
        self.__enrollment_limit: int = enrollment_limit
        self.__transcript: Dict[str, List[GradeEntry]] = {}          # semester -> [grade entries]
        self.__current_enrollments: Dict[str, Set[str]] = {}         # semester -> {course_codes}

    # ---- GPA ----
    @property
    def gpa(self) -> float:
        return self.__gpa

    @gpa.setter
    def gpa(self, value: float) -> None:
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0")
        self.__gpa = round(value, 2)

    # ---- Enrollment Limit ----
    @property
    def enrollment_limit(self) -> int:
        return self.__enrollment_limit

    @enrollment_limit.setter
    def enrollment_limit(self, value: int) -> None:
        if value < 1:
            raise ValueError("Enrollment limit must be positive")
        self.__enrollment_limit = value

    # ---- Transcript (safe accessors) ----
    def add_grade(self, semester: str, course_code: str, credits: int, letter: str) -> None:
        if letter not in LETTER_TO_GPA:
            raise ValueError("Invalid letter grade")
        self.__transcript.setdefault(semester, []).append((course_code, credits, letter))

    def get_transcript(self) -> Dict[str, List[GradeEntry]]:
        # return a shallow copy to protect internal structure
        return {sem: entries.copy() for sem, entries in self.__transcript.items()}

    def completed_courses(self) -> Set[str]:
        # consider any grade (even F) as "taken" for prereq purposes; adjust if needed
        return {code for entries in self.__transcript.values() for (code, _, _) in entries}

    # ---- Current Enrollments (with limits) ----
    def enroll(self, semester: str, course_code: str) -> None:
        s = self.__current_enrollments.setdefault(semester, set())
        if len(s) >= self.__enrollment_limit:
            raise ValueError(f"Enrollment limit ({self.__enrollment_limit}) reached for {semester}")
        s.add(course_code)

    def drop(self, semester: str, course_code: str) -> None:
        s = self.__current_enrollments.get(semester, set())
        s.discard(course_code)

    def current_enrollments(self, semester: Optional[str] = None) -> Dict[str, Set[str]] | Set[str]:
        if semester is None:
            return {sem: codes.copy() for sem, codes in self.__current_enrollments.items()}
        return self.__current_enrollments.get(semester, set()).copy()


class Student(Person):
    def __init__(self, person_id: str, name: str, email: str) -> None:
        super().__init__(person_id, name, email)
        self.record = SecureStudentRecord(enrollment_limit=5)

    # ---- Part B methods ----
    def enroll_course(self, course: "Course", semester: str) -> None:
        # prereqs & capacity will be checked by Department/Course; this enforces per-student limit
        self.record.enroll(semester, course.code)

    def drop_course(self, course_code: str, semester: str) -> None:
        self.record.drop(semester, course_code)

    def add_grade(self, semester: str, course_code: str, credits: int, letter: str) -> None:
        self.record.add_grade(semester, course_code, credits, letter)

    def calculate_gpa(self, semester: Optional[str] = None) -> float:
        transcript = self.record.get_transcript()
        entries: List[GradeEntry] = []
        if semester:
            entries = transcript.get(semester, [])
        else:
            for e in transcript.values():
                entries.extend(e)
        if not entries:
            self.record.gpa = 0.0
            return 0.0
        total_points = sum(LETTER_TO_GPA[letter] * credits for _, credits, letter in entries)
        total_credits = sum(credits for _, credits, _ in entries)
        gpa = total_points / total_credits if total_credits else 0.0
        self.record.gpa = gpa
        return self.record.gpa

    def get_academic_status(self) -> str:
        g = self.record.gpa
        if g >= 3.7:
            return "Dean's List"
        if g >= 2.0:
            return "Good Standing"
        return "Probation"

    def get_responsibilities(self) -> str:
        return "Attend classes, complete assessments, maintain academic standing."


class UndergraduateStudent(Student):
    def get_responsibilities(self) -> str:
        return "Complete undergraduate coursework and foundational projects."


class GraduateStudent(Student):
    def get_responsibilities(self) -> str:
        return "Complete advanced coursework, research, and thesis/dissertation."
