def counter_div(n):
    count_prime_number = 0

    for current_number in range(2, n + 1):
        count_div = 0

        for div in range(1, current_number + 1):
            if current_number % div == 0:
                count_div += 1

        if count_div == 2:
            count_prime_number += 1

    return count_prime_number
