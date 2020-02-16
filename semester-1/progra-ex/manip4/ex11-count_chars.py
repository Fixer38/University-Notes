def count_chars(chars: str, s: str) -> int:
    count = 0
    for elem in s:
        for char in chars:
            if elem == char:
                count += 1
    return count

print(count_chars("ac", "abbcccddd"))
