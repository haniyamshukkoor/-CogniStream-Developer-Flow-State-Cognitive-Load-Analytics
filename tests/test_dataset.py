
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = (
    ROOT / "data" / "processed"
    / "cognistream_developer_activity_cleaned.csv"
)

REQUIRED_COLUMNS = {
    "event_id",
    "developer_id",
    "team",
    "event_timestamp",
    "activity_type",
    "application",
    "project_name",
    "duration_minutes",
    "interruption_flag",
    "flow_state_proxy",
    "context_switch_flag",
    "data_source",
}


class TestCogniStreamDataset(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not DATA_PATH.exists():
            raise FileNotFoundError(
                f"Cleaned dataset not found: {DATA_PATH}"
            )
        cls.df = pd.read_csv(DATA_PATH)

    def test_dataset_is_not_empty(self):
        self.assertGreater(len(self.df), 0)

    def test_required_columns_exist(self):
        self.assertTrue(
            REQUIRED_COLUMNS.issubset(set(self.df.columns)),
            f"Missing columns: {REQUIRED_COLUMNS - set(self.df.columns)}",
        )

    def test_event_ids_are_present_and_unique(self):
        self.assertTrue(self.df["event_id"].notna().all())
        self.assertTrue(self.df["event_id"].is_unique)

    def test_developer_ids_are_present(self):
        self.assertTrue(self.df["developer_id"].notna().all())

    def test_timestamps_are_valid(self):
        timestamps = pd.to_datetime(
            self.df["event_timestamp"], errors="coerce"
        )
        self.assertTrue(timestamps.notna().all())

    def test_durations_are_positive(self):
        durations = pd.to_numeric(
            self.df["duration_minutes"], errors="coerce"
        )
        self.assertTrue(durations.notna().all())
        self.assertTrue((durations > 0).all())

    def test_binary_flags_are_valid(self):
        for column in [
            "interruption_flag",
            "context_switch_flag",
        ]:
            values = pd.to_numeric(
                self.df[column], errors="coerce"
            )
            self.assertTrue(
                values.isin([0, 1]).all(),
                f"{column} must contain only 0 or 1",
            )

    def test_flow_state_proxy_is_binary(self):
        values = pd.to_numeric(
            self.df["flow_state_proxy"], errors="coerce"
        )
        self.assertTrue(
            values.isin([0, 1]).all(),
            "flow_state_proxy must contain only 0 or 1",
        )


if __name__ == "__main__":
    unittest.main()
