class LogAnalyzer:
    def __init__(self):
        self.total = 0
        self.info = 0
        self.warning = 0
        self.error = 0

    def process_line(self, line):
        self.total += 1

        if line.startswith("INFO"):
            self.info += 1
        elif line.startswith("WARNING"):
            self.warning += 1
        elif line.startswith("ERROR"):
            self.error += 1

    def analyze(self, lines):
        for line in lines:
            self.process_line(line.strip())

    def get_report(self):
        return (
            f"Total lines: {self.total}\n"
            f"INFO: {self.info}\n"
            f"WARNING: {self.warning}\n"
            f"ERROR: {self.error}\n"
        )