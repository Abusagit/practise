def even_fibbonaci(limit=10):
    previous_last = 0
    previous_first = 1
    even_sum = 0
    while True:
        new = previous_last + previous_first
        if new >= limit:
            break
        even_sum += new if new % 2 == 0 else 0
        previous_last, previous_first = previous_first, new
    return even_sum


if __name__ == '__main__':
    print(even_fibbonaci())
    print(even_fibbonaci(4000000))
    print(even_fibbonaci(50))