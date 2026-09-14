"""Run the fault-tolerant student result processor."""

from pathlib import Path

from student_result_processor.exceptions import StudentProcessingError
from student_result_processor.logging_config import configure_logging
from student_result_processor.result_calculation import calculate_result
from student_result_processor.student_operations import (
    read_students_from_csv,
    student_from_row,
)


def process_students(records, logger=None):
    """Process every record, logging invalid students without stopping the batch."""
    if logger is None:
        logger = configure_logging()

    successful_results = []

    for row_number, record in enumerate(records, start=2):
        identifier = "unknown student"
        if isinstance(record, dict):
            identifier = record.get("student_id") or record.get("name") or identifier

        try:
            student = student_from_row(record)
            result = calculate_result(student)
            successful_results.append(result)
            logger.info(
                "Processed student %s (%s) successfully.",
                result["student_id"],
                result["name"],
            )
        except (StudentProcessingError, TypeError, ValueError, ArithmeticError) as error:
            logger.error(
                "Skipped CSV row %s for %s: %s: %s",
                row_number,
                identifier,
                type(error).__name__,
                error,
            )
            continue

    return successful_results


def display_results(results):
    """Display successfully calculated student results as a readable table."""
    if not results:
        print("No valid student results were produced.")
        return

    heading = (
        f"{'ID':<10} {'Name':<16} {'Total':>8} "
        f"{'Percentage':>12} {'Grade':>8} {'Status':>8}"
    )
    print(heading)
    print("-" * len(heading))

    for result in results:
        print(
            f"{result['student_id']:<10} "
            f"{result['name']:<16} "
            f"{result['total']:>8.1f} "
            f"{result['percentage']:>11.2f}% "
            f"{result['grade']:>8} "
            f"{result['status']:>8}"
        )


def main():
    """Read the sample CSV, process all students, and display valid results."""
    package_directory = Path(__file__).parent
    input_file = package_directory / "students.csv"
    log_file = package_directory / "student_errors.log"
    logger = configure_logging(log_file)

    try:
        records = read_students_from_csv(input_file)
    except (FileNotFoundError, StudentProcessingError, OSError) as error:
        logger.critical("Unable to read the input file: %s: %s", type(error).__name__, error)
        return

    results = process_students(records, logger)
    display_results(results)
    print(f"\nProcessed {len(records)} record(s): {len(results)} succeeded and "
          f"{len(records) - len(results)} failed.")
    print(f"Log file: {log_file}")


if __name__ == "__main__":
    main()
