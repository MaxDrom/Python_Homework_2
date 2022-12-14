class FunctionCache:
    debug = False
    def __init__(self, function):
        self.function = function
        self.cached_calls = {}
    
    def __call__(self, *args):
        if args not in self.cached_calls:
            self.cached_calls[args] = self.function(*args)
        elif FunctionCache.debug:
            arg_str = ", ".join(f'{arg}' for arg in args)
            print("Using cached value for arguments " + arg_str)

        return self.cached_calls[args]

@FunctionCache
def numbers_with_sum_of_digits_count(sum_of_digits, number_of_digits):
    if number_of_digits == 1:
        if sum_of_digits <=  9:
            return 1
        return 0
    res = 0
    for i in range(min(sum_of_digits,9)+1):
        res+=numbers_with_sum_of_digits_count(sum_of_digits-i, number_of_digits-1)
    return res

def lucky_tickets_count(n):
    res = 0
    for i in range(9*n+1):
        res +=  numbers_with_sum_of_digits_count(i, n)**2
    return res


FunctionCache.debug = True
#numbers_with_sum_of_digits_count=FunctionCache(numbers_with_sum_of_digits_count)
n = int(input("Число цифр в билете (должно быть четным): "))//2
print(f'Число счастливых билетов: {lucky_tickets_count(n)}')