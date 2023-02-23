def isPalindrome(x: int) -> bool:
    num = str(x)
    num1 = ''.join(reversed(str(x)))
    return num == num1

# Запуск
x = 34543
print(isPalindrome(x))