#coding: utf-8
from enum import Enum, unique

@unique
class LoginStatus(Enum):
    success = 0
    fail = 1
    noexist = 2

