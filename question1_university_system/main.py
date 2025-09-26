from person import Staff
from faculty import Professor, Lecturer, TA
from student import Student, UndergraduateStudent, GraduateStudent
from department import Department, Course

def seed_demo():
    # Department
    cs = Department("Computer Science")

    # Faculty
    prof = Professor("F001", "Dr. Ada Lovelace", "ada@uni.edu")
    lect = Lecturer("F002", "Ms. Grace Hopper", "grace@uni.edu")
    ta   = TA("F003", "Mr. Alan Turing", "alan@uni.edu")
    cs.add_faculty(prof); cs.add_faculty(lect); cs.add_faculty(ta)

    # Staff (to show another Person branch)
    admin = Staff("S001", "Ms. Admin", "admin@uni.edu")

    # Courses (with prereqs)
    cs101 = Course("CS101", "Intro to CS", credits=3, capacity=2, prerequisites=[])
    cs201 = Course("CS201", "Data Structures", credits=3, capacity=2, prerequisites=["CS101"])
    cs301 = Course("CS301", "Algorithms", credits=3, capacity=2, prerequisites=["CS201"])
    cs.add_course(cs101); cs.add_course(cs201); cs.add_course(cs301)

    # Assign faculty
    cs.assign_faculty_to_course("F001", "CS301")  # Professor
    cs.assign_faculty_to_course("F002", "CS201")  # Lecturer
    cs.assign_faculty_to_course("F003", "CS101")  # TA assists

    # Students
    ug = UndergraduateStudent("U100", "Alice", "alice@uni.edu")
    pg = GraduateStudent("G200", "Bob", "bob@uni.edu")
    cs.register_student(ug); cs.register_student(pg)

    # Enrollments (show prereq enforcement)
    cs.enroll("U100", "CS101", "2025-Spring")  # OK
    cs.enroll("G200", "CS101", "2025-Spring")  # OK

    # Attempt to enroll in CS201 without CS101 would fail; record grade first
    cs.record_grade("U100", "2025-Spring", "CS101", "A")
    cs.record_grade("G200", "2025-Spring", "CS101", "B+")

    # Next semester
    cs.enroll("U100", "CS201", "2025-Fall")    # Now the prereq (CS101) is satisfied
    cs.enroll("G200", "CS201", "2025-Fall")

    # Finish grades and compute GPA
    cs.record_grade("U100", "2025-Fall", "CS201", "A-")
    cs.record_grade("G200", "2025-Fall", "CS201", "B")

    ug_gpa = ug.calculate_gpa()  # across all semesters
    pg_gpa = pg.calculate_gpa()

    print("--- Polymorphism demo ---")
    people = [ug, pg, prof, lect, ta, admin]
    for p in people:
        print(f"{p}: {p.get_responsibilities()}")

    print("--- Workloads ---")
    for f in [prof, lect, ta]:
        print(f"{f.name} workload = {f.calculate_workload()}")

    print("--- Student status ---")
    print(f"{ug.name} GPA={ug_gpa}, Status={ug.get_academic_status()}")
    print(f"{pg.name} GPA={pg_gpa}, Status={pg.get_academic_status()}")

if __name__ == "__main__":
    seed_demo()
