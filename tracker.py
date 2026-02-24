import datetime

class LanguageTracker:
    def __init__(self, filename):
        self.filename = filename

    def add_task(self, language, detail):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"[{now}] {language}: {detail}\n")
        print("Robot: Save_Data")

    def view_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()
                if not content:
                    print("\n--- Robot: Log is empty ---")
                else:
                    print("\n--- History Save ---")
                    print(content)
                    print("----------------------")
        except FileNotFoundError:
            print("Robot: No_Data")

    def delete_all(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            pass
        print("Robot: Log Cleared")
