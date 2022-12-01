class FunctionCache:
    def __init__(self, function):
        self.function = function
        self.cached_calls = {}
    
    def __call__(self, *args):
        if(args in self.cached_calls):
            arg_str = ", ".join(f'{arg}' for arg in args)
            print("Using cached value for arguments " + arg_str)
            return self.cached_calls[args]
        result = self.function(*args)
        self.cached_calls[args] = result
        return result

@FunctionCache
def numbers_with_sum_of_digits_count(sum_of_digits, number_of_digits):
    if number_of_digits == 1:
        if sum_of_digits <=  9:
            return 1
        return 0
    res = 0
    for i in range(10):
        if sum_of_digits-i < 0:
            break
        res+=numbers_with_sum_of_digits_count(sum_of_digits-i, number_of_digits-1)
    return res

def lucky_tickets_count(n):
    res = 0
    for i in range(28):
        res +=  numbers_with_sum_of_digits_count(i, n)*numbers_with_sum_of_digits_count(i, n)
    return res

#numbers_with_sum_of_digits_count=FunctionCache(numbers_with_sum_of_digits_count)
n = int(input("Число цифр в билете (должно быть четным): "))/2
print(f'Число счастливых билетов: {lucky_tickets_count(n)}')