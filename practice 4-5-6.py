import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high_performers_count = 0

        for s in self.students:
            try:
                val = float(s['GPA'])
                gpas.append(val)
                if val > 3.5:
                    high_performers_count += 1
            except ValueError:
                print(f"Warning: could not convert value for student {s.get('student_id')} skipping row.")
                continue

        if not gpas:
            return {}

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": high_performers_count
        }
        return self.result

    def run_advanced_processing(self):
        print("\nLambda / Map / Filter")

        high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, self.students))
        print(f"Students with GPA > 3.8: {len(high_gpa)}")

        gpa_values = list(map(lambda s: float(s['GPA']), self.students))
        print(f"GPA values (first 5): {gpa_values[:5]}")

        hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, self.students))
        print(f"Students studying > 4 hrs: {len(hard_workers)}")

    def print_results(self):
        print("\nANALYSIS RESULT")
        print("===============")
        print(f"Analysis: {self.result.get('analysis')}")
        print(f"Total students: {self.result.get('total_students')}")
        print(f"Average GPA: {self.result.get('average_gpa')}")
        print(f"Highest GPA: {self.result.get('max_gpa')}")
        print(f"Lowest GPA: {self.result.get('min_gpa')}")
        print(f"High performers: {self.result.get('high_performers')}")


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w') as f:
                json.dump(self.result, f, indent=4)
            print(f"\nResult saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving results: {e}")


if __name__ == "__main__":
    target_file = 'students.csv'

    fm = FileManager(target_file)
    if not fm.check_file():
        print("Stopping program.")
        exit()

    fm.create_output_folder()

    dl = DataLoader(target_file)
    data = dl.load()

    if data:
        dl.preview()

        analyser = DataAnalyser(data)
        analyser.analyse()
        analyser.run_advanced_processing()
        analyser.print_results()

        saver = ResultSaver(analyser.result, 'output/result.json')
        saver.save_json()