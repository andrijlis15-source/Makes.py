def count_pairs(filename, pairs):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # створюємо словник лічильників одразу
                pairs_count = {pair: 0 for pair in pairs}

                words = line.lower().split()

                for word in words:
                    for i in range(len(word) - 1):
                        pair = word[i:i+2]
                        if pair in pairs_count:
                            pairs_count[pair] += 1

                yield pairs_count

    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")


def main():
    FILE = "laba9/text.txt"
    PAIRS = ['su', 'on', 'ps']
    result = count_pairs(FILE, PAIRS)

    for i, res in enumerate(result, start=1):
        print(f"Рядок №{i}: {res}")


if __name__ == "__main__":
    main()
