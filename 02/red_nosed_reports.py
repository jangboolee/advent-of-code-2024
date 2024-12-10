from pathlib import Path


def read_input(subfolder: str) -> tuple[list[int]]:

    file_path = Path(".") / subfolder / "input.txt"
    with open(file_path, "r") as f:
        f_content = [line.rstrip().split(" ") for line in f.readlines()]
        return [[int(i) for i in line] for line in f_content]


def calc_safe_reports(data: list[list[int]]) -> int:
    """Function to find the total count of safe reports

    Args:
        data (list[list[int]]): List containing all reports, with one report
            represented as a second-level list

    Returns:
        int: Total count of safe reports
    """

    def check_report(report: list[int]) -> bool:
        """Helper to check if a single report is safe or not

        Args:
            report (list[int]): A single report

        Returns:
            bool: True if the report is safe, False if not
        """

        def check_deltas(report: list[int]) -> bool:
            """Helper to check if any two adjacent levels differ by at least
            1 and at most 3

            Args:
                report (list[int]): A single report

            Returns:
                bool: True if deltas are within accepted levels, False if not
            """

            return all(
                [
                    (
                        0 < abs(report[i] - report[i + 1])
                        and abs(report[i] - report[i + 1]) <= 3
                    )
                    for i in range(len(report) - 1)
                ]
            )

        increasing = False

        # Check increase/decrease for first two elements
        if report[0] < report[1]:
            increasing = True

        if increasing:
            # Check if the levels are all increasing
            all_increase = all(
                [report[i] < report[i + 1] for i in range(len(report) - 1)]
            )
            if all_increase:
                return check_deltas(report)
            else:
                return False
        else:
            # Check if the levels are all decreasing
            all_decrease = all(
                [report[i] > report[i + 1] for i in range(len(report) - 1)]
            )
            if all_decrease:
                return check_deltas(report)
            else:
                return False

    safe_reports = 0
    for report in data:
        safe_reports += check_report(report)

    return safe_reports


def calc_safe_report_dampener(data: list[list[int]]) -> int:

    def is_monotonic(report: list[int]) -> bool:
        """Helper to check if the report increases or decreases monotonically

        Args:
            report (list[int]): A single report

        Returns:
            bool: True if the report increases or decreases monotonically,
                False if not
        """

        increasing = all(
            report[i] < report[i + 1] for i in range(len(report) - 1)
        )
        decreasing = all(
            report[i] > report[i + 1] for i in range(len(report) - 1)
        )
        return increasing or decreasing

    def check_deltas(report: list[int]) -> bool:
        """Helper to check if any two adjacent levels differ by at least
            1 and at most 3

        Args:
            report (list[int]): A single report

        Returns:
            bool: True if deltas are within accepted levels, False if not
        """
        return all(
            1 <= abs(report[i] - report[i + 1]) <= 3
            for i in range(len(report) - 1)
        )

    def check_single_removal(report: list[int]) -> bool:
        """Check if a report can be fixed by removing one element

        Args:
            report (list[int]): A single report

        Returns:
            bool: True if the report can be fixed by removing an element, False
                if not
        """
        for i in range(len(report)):
            removed_list = report[:i] + report[i + 1 :]
            if is_monotonic(removed_list) and check_deltas(removed_list):
                return True
        return False

    safe_reports = 0
    for report in data:
        if is_monotonic(report) and check_deltas(report):
            safe_reports += 1
        else:
            if check_single_removal(report):
                safe_reports += 1

    return safe_reports


if __name__ == "__main__":

    data = read_input("02")
    safe_reports = calc_safe_reports(data)
    safe_reports_dampener = calc_safe_report_dampener(data)
