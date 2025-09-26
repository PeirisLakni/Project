from __future__ import annotations
from abc import ABC, abstractmethod

"""person.py
Base module defining the Person class hierarchy for the University Management System.
"""

class Person(ABC): """Abstract base class for any person in the university."""

def __init__(self, person_id: str, name: str, email: str, age = int) -> None:
        self.person_id = person_id
        self.name = name
        self.age = age
        self.email = email

def contact_info(self) -> str: 
      return f"{self.name} <{self.email}>"

@abstractmethod
def get_responsibilities(self) -> str:
        ...

def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.person_id}, name={self.name}, age = {self.age})"


class Staff(Person):
    def get_responsibilities(self) -> str:
        return "Support operations and administration."
