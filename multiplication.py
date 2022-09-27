def product_of_numbers( *args ):
    # args is a list of all arguments
    print('from function: ', some_global_variable) # Avoid this, function should be isolated
    result = 1 # in local scope
    for num in args:
        result *= num # result = result * num
    
    return result


product_of_numbers(1,897,5)