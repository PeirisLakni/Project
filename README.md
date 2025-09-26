# Programming for Data Science – Coursework (2025.1)

This repo contains:
- **Q1:** Enhanced OOP University Management System (Python)
- **Q2:** E-commerce Data Analysis (scraping → cleaning → analysis → viz → simple prediction)
- **Q3:** AI Ethics in Healthcare (written report)

## Repository Structure
```
project/
├── question1_university_system/
│   ├── main.py
│   ├── person.py
│   ├── student.py
│   ├── faculty.py
│   └── department.py
├── question2_social_media_analysis/
│   ├── data_collection/
│   ├── data_processing/
│   ├── analysis/
│   └── visualizations/
├── question3_ethics_report/
│   └── healthcare_ethics_report.md
├── requirements.txt
└── README.md
```

## Setup
- Use **Python 3.11+** (or a conda env).
- Install dependencies from the project root:
  ```bash
  python -m pip install -r requirements.txt
  ```
  (Conda: `conda create -n pds python=3.11 -y && conda activate pds && pip install -r requirements.txt`)

## How to Run

### Q1 — University Management System
```bash
cd question1_university_system
python main.py
```
**Features:**  
- Inheritance: `Person → Student/Faculty/Staff`; `Faculty → Professor/Lecturer/TA`; `Student → Undergraduate/Graduate`  
- Student management: `enroll_course`, `drop_course`, `calculate_gpa`, `get_academic_status`  
- Encapsulation/validation with a secure student record (private GPA, enrollment limits)  
- Polymorphism: role-specific `get_responsibilities()` and `calculate_workload()`  
- Department/Course management with capacity and prerequisite checks

### Q2 — E-commerce Data Analysis
- **data_collection/**: web/RSS scrapers (requests + BeautifulSoup), polite delays, retries, pagination  
- **data_processing/**: cleaning (text normalize, missing/dupes, keywords, timestamp standardization)  
- **analysis/**: descriptive stats, outliers, correlations, frequency distributions, hypothesis tests  
- **visualizations/**: histograms/boxplots, scatter with trend line, category bars, interactive Plotly  
- **prediction**: simple linear regression (price ~ rating), category patterns, basic recommendation idea

### Q3 — AI Ethics in Healthcare
Write the 1000-word report covering privacy (incl. HIPAA context), algorithmic bias + mitigation, an ethical checklist/“right to explanation,” and stakeholder impacts/equity.

## Requirements
- See `requirements.txt`.  
- Q1 uses only the Python standard library.  
- Q2 typically needs: `requests`, `beautifulsoup4`, `pandas`, `numpy`, `matplotlib`, `plotly`, `scipy` (add others only if used).

## Workflow (Git)
```bash
git add .
git commit -m "Meaningful message"
git push
```
