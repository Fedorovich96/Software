def analyze_text(filename):
    letters = 0
    words = 0
    lines_count = 0

    with open(filename, 'r') as file:
        for line in file:
            lines_count += 1
            words += len(line.split())
            letters += sum(1 for char in line if char.isalpha())

    print(f"Input file contains:")
    print(f"{letters} letters")
    print(f"{words} words")
    print(f"{lines_count} lines")

if __name__ == "__main__":
    analyze_text('input.txt')
