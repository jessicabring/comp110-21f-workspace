"""Practice writing functions."""


def main() -> None:
    print(dict_transform({2: [1, 2], 5: [3, 4]}))
    print(average_grades({"Bill": [75, 94, 97], "Annie": [88, 93, 99]}))


def dict_transform(a: dict[int, list[int]]) -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}
    for key in a:
        multiplication_list: list[int] = []
        for value in a[key]:
            multiplication_list.append(key * value)
        result[key] = multiplication_list
    return result


def average_grades(a: dict[str, list[int]]) -> dict[str, float]:
    result: dict[str, float] = {}
    for key in a:
        average: float = 0
        counter: int = 0
        for value in a[key]:
            average += float(value)
            counter += 1
        result[key] = average / counter
    return result


if __name__ == "__main__":
    main()