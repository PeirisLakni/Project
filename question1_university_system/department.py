from __future__ import annotations
from typing import List, Dict, Set
from faculty import Faculty
from dataclasses import dataclass

@dataclass
class Course:
    code: str
    title: str
    credits: int
    capacity: int
    prerequisites: List[str]

    def __post_init__(self) -> None:
        if self.credits <= 0:
            raise ValueError("Course credits must be positive")
        if self.capacity <= 0:
            raise ValueError("Course capacity must be positive")
        self.enrolled_ids: Set[str] = set()
        self.assigned_faculty_id: str | None = None

    def add_prerequisite(self, course_code: str) -> None:
        if course_code not in self.prerequisites:
            self.prerequisites.append(course_code)

    def can_enroll(self, student: Student) -> bool:
        # Check capacity and prereqs
        if len(self.enrolled_ids) >= self.capacity:
            return False
        completed = student.record.completed_courses()
        return all(req in completed for req in self.prerequisites)

    def enroll(self, student: Student, semester: str) -> None:
        if not self.can_enroll(student):
            raise ValueError(f"Cannot enroll {student.person_id} in {self.code} (capacity/prereqs).")
        self.enrolled_ids.add(student.person_id)
        student.enroll_course(self, semester)

    def drop(self, student: Student, semester: str) -> None:
        self.enrolled_ids.discard(student.person_id)
        student.drop_course(self.code, semester)


class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.faculty: Dict[str, Faculty] = {}
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}

    # --- Management ---
    def add_course(self, course: Course) -> None:
        self.courses[course.code] = course

    def add_faculty(self, f: Faculty) -> None:
        self.faculty[f.person_id] = f

    def register_student(self, s: Student) -> None:
        self.students[s.person_id] = s

    def assign_faculty_to_course(self, faculty_id: str, course_code: str) -> None:
        f = self.faculty[faculty_id]
        c = self.courses[course_code]
        c.assigned_faculty_id = f.person_id
        f.assign_course(course_code)

    # --- Registration with prereq checking ---
    def enroll(self, student_id: str, course_code: str, semester: str) -> None:
        s = self.students[student_id]
        c = self.courses[course_code]
        c.enroll(s, semester)

    def drop(self, student_id: str, course_code: str, semester: str) -> None:
        s = self.students[student_id]
        c = self.courses[course_code]
        c.drop(s, semester)

    # --- Grading ---
    def record_grade(self, student_id: str, semester: str, course_code: str, letter: str) -> None:
        s = self.students[student_id]
        c = self.courses[course_code]
        s.add_grade(semester, course_code, credits=c.credits, letter=letter)
