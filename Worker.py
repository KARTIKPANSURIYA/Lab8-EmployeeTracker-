# Author: Kartik Pansuriya
# Date: November 10, 2024
# Description: This file Describe a Worker class which inherited from employee and stores shift information.

from Employee import Employee

class Worker(Employee):
    def __init__(self, name: str, emp_id: int, pay_rate: float, shift: int):
        """
        Initializing a Worker with a name, ID, pay rate, and shift.
        :param shift: 1 for day shift, 2 for night shift
        """
        super().__init__(name, emp_id, pay_rate)
        self.__shift = shift

    def getShift(self) -> int:
        return self.__shift

    def setShift(self, shift: int):
        self.__shift = shift

    def shiftType(self) -> str:
        return "Day Shift" if self.__shift == 1 else "Night Shift"
