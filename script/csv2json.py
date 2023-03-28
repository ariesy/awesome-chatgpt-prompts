import argparse
import csv
import json
import os.path
import unittest


def csv_to_json(csv_file_path):
    # Read CSV file into a list of dictionaries
    with open(csv_file_path, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]

    # Write JSON output file
    basename = os.path.splitext(csv_file_path)[0]
    output_file_path = f"{basename}.json"
    with open(output_file_path, "w") as outfile:
        json.dump(rows, outfile, indent=2)

    return output_file_path


class TestCsvToJson(unittest.TestCase):

    def test_csv_to_json(self):
        csv_file_path = "test.csv"
        expected_output = [
            {"act": "act1", "prompt": "I want you to act as a some act. promt1"},
            {"act": "act2", "prompt": "I want you to act as an some act, promt2"}
        ]
        actual_output = None

        try:
            with open(csv_to_json(csv_file_path), "r") as infile:
                actual_output = json.load(infile)
        except Exception as e:
            self.fail(f"csv_to_json() raised an exception: {str(e)}")

        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV file to JSON")
    parser.add_argument("csv_file_path", help="Path to input CSV file")
    args = parser.parse_args()
    csv_to_json(args.csv_file_path)