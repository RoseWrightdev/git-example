import time

def main(path):
    init = scanfile(path)
    while True:
        print("Hello world!")
        cur = scanfile(path)
        for i, (line_init, line_cur) in enumerate(zip(init, cur)):
            if line_init != line_cur:
                print(f"Change detected in {path} at line {i + 1}")
                print(f"Old line: {line_init.strip()}")
                print(f"New line: {line_cur.strip()}")
        if len(cur) != len(init):
            print(f"Change detected in {path}: number of lines changed from {len(init)} to {len(cur)}.")
        init = cur
        time.sleep(.5)

def scanfile(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()

if __name__ == "__main__":
    main("./data/example.txt")
