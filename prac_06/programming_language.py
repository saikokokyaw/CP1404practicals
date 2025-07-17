"""
programming_language
Estimate: 25 minutes
Actual: 35 minutes
"""


class ProgrammingLangugage:

    def __init__(self, name='', typing='', reflection=True, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.title() == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
