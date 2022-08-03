from dataclasses import dataclass


# class Question:
#
#     def __init__(self, text, is_true, explanation):
#         self.explanation = explanation
#         self.is_tru = is_true
#         self.text = text


@dataclass
class Question:
    text: str = 'abc'
    is_true: bool = False
    explanation: str = ''


q = Question('text', True, '')
a = Question()
print(q)
print(a)
