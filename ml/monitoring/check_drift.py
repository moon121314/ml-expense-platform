"""Check for data drift using Evidently."""

import pandas as pd

from evidently import Report
from evidently.presets import DataDriftPreset


REFERENCE_PATH = "/Users/moon/Downloads/Python/Day13/ml-expense-platform/ml/data/raw/sample_expenses.csv"
CURRENT_PATH = "/Users/moon/Downloads/Python/Day13/ml-expense-platform/ml/data/raw/current_expense.csv"


def main() -> None:
    reference = pd.read_csv(REFERENCE_PATH)
    current = pd.read_csv(CURRENT_PATH)

    report = Report(
        metrics=[
            DataDriftPreset(),
        ]
    )

    result = report.run(
        reference_data=reference,
        current_data=current,
    )

    result.save_html("drift_report.html")

    print("Drift report saved to drift_report.html")


if __name__ == "__main__":
    main()