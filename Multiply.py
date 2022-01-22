def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(div1, div2):
    unit = div1 / div2
    return unit

def modulo(mod1, mod2):
    turkey = mod1 % mod2
    return turkey

def count_upto(arg):
    start = 0
    while start < arg:
        print(start)
        start += 1

def is_value_divisible_by_two_and_three(x):
    if x % 2 == 0 or x % 3 == 0:
        print('success')

def fun_with_for_loop():
    lst = [2, 4, 5, 8]
    for item in lst:
        if not item % 2 == 0:
            print(item)

def reverse(road):
    print(road)

if __name__ == "__main__":
    # item = 2
    # item2 = 3
    # result = multiply(item, item2)
    # result2 = divide(item, item2)
    # mod_result = modulo(8, 3)
    # is_value_divisible_by_two_and_three(8)
    # count_upto(10)
    # print(mod_result)
    # print(result2)
    # print(result)
    #fun_with_for_loop()
