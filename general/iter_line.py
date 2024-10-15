class Reader:
    def __init__(self, file_path):
        self.file = open(file_path, "r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line.rstrip("\n")
        else:
            self.file.close()
            raise StopIteration


if __name__ == "__main__":
    file_path = "sample_data/doubutsu.txt"
    reader = Reader(file_path)
    for line in reader:
        print(line)
