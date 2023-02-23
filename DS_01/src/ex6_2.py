def isPalindrome_v2(x: int) -> bool:
    n = x
    rev = 0
    while n:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    return x == rev

# Запуск
n = 45654
print(isPalindrome_v2(n))