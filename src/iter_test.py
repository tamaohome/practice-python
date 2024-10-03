class AnimalReader:
    """クラスの持つ配列 animals をイテレータとして使う"""

    def __init__(self):
        self.animals = ["cat", "dog", "elephant", "monkey", "giraffe", "lion"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.animals):
            animal = self.animals[self.index]
            self.index += 1
            return animal
        else:
            raise StopIteration


class AnimalFileReader1:
    """インスタンス生成時にファイルを全て読み込み、配列 animals に格納する"""

    def __init__(self, file_path):
        self.animals = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                self.animals.append(line.rstrip("\n"))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.animals):
            animal = self.animals[self.index]
            self.index += 1
            return animal
        else:
            raise StopIteration


class AnimalFileReader2:
    """yield文を使って1行ずつ読み込む イテレーションの状態も保存する"""

    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, "r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self):
        if self.file.closed:
            raise StopIteration
        line = self.file.readline()
        if line:
            return line.rstrip("\n")
        else:
            self.file.close()
            raise StopIteration


if __name__ == "__main__":

    input_file = "sample_data/doubutsu.txt"

    readers = [
        AnimalReader(),
        AnimalFileReader1(input_file),
        AnimalFileReader2(input_file)
    ]  # fmt: skip

    for reader in readers:
        print(reader.__class__.__name__ + ":")

        print("1回目のループ: ", end="")
        for i, animal in enumerate(reader):
            print(animal + " ", end="")
            if i == 2:
                print()
                break

        print("2回目のループ: ", end="")
        i = 0
        while True:
            try:
                animal = next(reader)
                print(f"{i}:{animal}" + " ", end="")
            except StopIteration:
                break
            i += 1

        print("\n")
