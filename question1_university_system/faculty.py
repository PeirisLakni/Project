from __future__ import annotations
from typing import List
from person import Person

class Faculty(Person):
    def __init__(self, person_id: str, name: str, email: str) -> None:
        super().__init__(person_id, name, email)
        self.courses_assigned: List[str] = []

    def assign_course(self, course_code: str) -> None:
        if course_code not in self.courses_assigned:
            self.courses_assigned.append(course_code)

    def get_responsibilities(self) -> str:
        return "Teach courses and contribute to the academic mission."

    def calculate_workload(self) -> int:
        """Default workload = number of courses assigned."""
        return len(self.courses_assigned)


class Professor(Faculty):
    def get_responsibilities(self) -> str:
        return "Teach, conduct research, supervise theses, serve on committees."

    def calculate_workload(self) -> int:
        # Assume fewer taught sections due to research load: weight 2 per course
        return max(1, len(self.courses_assigned) * 2)


class Lecturer(Faculty):
    def get_responsibilities(self) -> str:
        return "Teach multiple sections and focus on pedagogy."

    def calculate_workload(self) -> int:
        # Lecturers often teach more: weight 3 per course
        return len(self.courses_assigned) * 3


class TA(Faculty):
    def get_responsibilities(self) -> str:
        return "Assist teaching, hold labs/tutorials, grade under supervision."

    def calculate_workload(self) -> int:
        # Assist load per course is lighter: weight 1 per course
        return len(self.courses_assigned) * 1
