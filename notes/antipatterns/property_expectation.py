"""
A property is expected to return a direct or simply computed value without a
state change. Property should not be used for expensive queries or change state.
"""

from time import sleep


class Customer:
    @property
    def salary_report(self) -> str:
        """BAD - Long running expensive query as property"""
        salary = "..."  # download salary excel
        sleep(2)
        calculation = "..."  # calculate salary
        sleep(2)
        report = "..."  # generate report
        sleep(2)
        return report

    def get_salary_report(self) -> str:
        """GOOD - Long running expensive query as function"""
        salary = "..."  # download salary excel
        sleep(2)
        calculation = "..."  # calculate salary
        sleep(2)
        report = "..."  # generate report
        sleep(2)
        return report
