# Python Library Import
# DO NOT REMOVE
import statistics
import numpy


# Welcome Text
print('Welcome to ZeLu Calculator'.center(35, '*'))
# User Category for Input
print('  Category for Inputs  '.center(30, '='))
print('_______________________________')
print('| four       -- \t4 Inputs  |')
print('| five       -- \t5 Inputs  |')
print('| six        -- \t6 Inputs  |')
print('| seven      -- \t7 Inputs  |')
print('| eight      -- \t8 Inputs  |')
print('| nine       -- \t9 Inputs  |')
print('| ten        -- \t10 Inputs |')
print('| eleven     -- \t11 Inputs |')
print('| twelve     -- \t12 Inputs |')
print('| thirteen   -- \t13 Inputs |')
print('| fourteen   -- \t14 Inputs |')
print('| fifteen    -- \t15 Inputs |')
print('| sixteen    -- \t16 Inputs |')
print('_______________________________')

# User Choice
choice = input('\nEnter number of choice: ')

# Calculation for Mean, Median and Mode
if choice == 'four':
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('4 Inputs'.center(30, '-'))
    first_num = float(input('Enter number: '))
    second_num = float(input('Enter number: '))
    third_num = float(input('Enter number: '))
    fourth_num = float(input('Enter number: '))

    # Array
    four_inputs = [first_num, second_num, third_num, fourth_num]

    # Statistics Calculation
    print('\n\n')
    print(' Result of Calculation '.center(35, '-'))
    numbers_mean = statistics.mean(four_inputs)
    print("Mean: ", numbers_mean)

    numbers_median = statistics.median(four_inputs)
    print('Median: ', numbers_median)

    numbers_std = numpy.std(four_inputs)
    print('Standard Deviation: ', round(numbers_std, 3))

    cons_skewness: float = (3)
    result_memo = numbers_mean - numbers_median
    result_skewm = cons_skewness * result_memo
    numbers_Skewness = round(result_skewm / numbers_std, 3)
    print('Skewness: ', numbers_Skewness)
    if numbers_Skewness < 0:
        print('Skewness is negatively skewed or skewed to the left')

    else:
        print('Skewness is positively skewed or skewed to the right')

elif choice == 'five':
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('5 Inputs'.center(30, '-'))
    first_num = float(input('Enter number: '))
    second_num = float(input('Enter number: '))
    third_num = float(input('Enter number: '))
    fourth_num = float(input('Enter number: '))
    fifth_num = float(input('Enter number: '))

    # Array
    five_inputs = [first_num, second_num, third_num, fourth_num, fifth_num]

    # Statistics Calculation
    numbers_mean = statistics.mean(five_inputs)
    print('Mean is: ', numbers_mean)

    numbers_median = statistics.median(five_inputs)
    print('Median is: ', numbers_median)

    numbers_std = numpy.std(five_inputs)
    print('Standard Deviation is: ', round(numbers_std, 3))

    cons_skewness: float = (3)
    result_memo = numbers_mean - numbers_median
    result_skewm = cons_skewness * result_memo
    numbers_Skewness = round(result_skewm / numbers_std, 3)
    print('Skewness: ', numbers_Skewness)
    if numbers_Skewness < 0:
        print('Skewness is negatively skewed or skewed to the left')

    else:
        print('Skewness is positively skewed or skewed to the right')

elif choice == 'six':
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('6 Inputs'.center(30, '-'))
    first_num = float(input('Enter number: '))
    second_num = float(input('Enter number: '))
    third_num = float(input('Enter number: '))
    fourth_num = float(input('Enter number: '))
    fifth_num = float(input('Enter number: '))
    sixth_num = float(input('Enter number: '))

    # Array
    six_inputs = [first_num, second_num, third_num, fourth_num, fifth_num, sixth_num]

    # Statistics Calculation
    numbers_mean = statistics.mean(six_inputs)
    print('Mean is: ', numbers_mean)

    numbers_median = statistics.median(six_inputs)
    print('Median is: ', numbers_median)

    numbers_std = numpy.std(six_inputs)
    print('Standard Deviation is: ', round(numbers_std, 3))

    cons_skewness: float = (3)
    result_memo = numbers_mean - numbers_median
    result_skewm = cons_skewness * result_memo
    numbers_Skewness = round(result_skewm / numbers_std, 3)
    print('Skewness: ', numbers_Skewness)
    if numbers_Skewness < 0:
        print('Skewness is negatively skewed or skewed to the left')

    else:
        print('Skewness is positively skewed or skewed to the right')

elif choice == 'seven':
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('7 Inputs'.center(30, '-'))
    first_num = float(input('Enter number: '))
    second_num = float(input('Enter number: '))
    third_num = float(input('Enter number: '))
    fourth_num = float(input('Enter number: '))
    fifth_num = float(input('Enter number: '))
    sixth_num = float(input('Enter number: '))
    seventh_num = float(input('Enter number: '))

    # Array
    seven_inputs = [first_num, second_num, third_num, fourth_num, fifth_num, sixth_num, seventh_num]

    # Statistics Calculation
    numbers_mean = statistics.mean(seven_inputs)
    print('Mean is: ', numbers_mean)

    numbers_median = statistics.median(seven_inputs)
    print('Median is: ', numbers_median)

    numbers_std = numpy.std(seven_inputs)
    print('Standard Deviation is: ', round(numbers_std, 3))

    cons_skewness: float = (3)
    result_memo = numbers_mean - numbers_median
    result_skewm = cons_skewness * result_memo
    numbers_Skewness = round(result_skewm / numbers_std, 3)
    print('Skewness: ', numbers_Skewness)
    if numbers_Skewness < 0:
        print('Skewness is negatively skewed or skewed to the left')

    else:
        print('Skewness is positively skewed or skewed to the right')

elif choice == 'eight':
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('8 Inputs'.center(30, '-'))
    first_num = float(input('Enter number: '))
    second_num = float(input('Enter number: '))
    third_num = float(input('Enter number: '))
    fourth_num = float(input('Enter number: '))
    fifth_num = float(input('Enter number: '))
    sixth_num = float(input('Enter number: '))
    seventh_num = float(input('Enter number: '))
    eighth_num = float(input('Enter number: '))

    # Array
    eight_inputs = [first_num, second_num, third_num, fourth_num, fifth_num, sixth_num, seventh_num, eighth_num]

    # Statistics Calculation
    numbers_mean = statistics.mean(eight_inputs)
    print('Mean is: ', numbers_mean)

    numbers_median = statistics.median(eight_inputs)
    print('Median is: ', numbers_median)

    numbers_std = numpy.std(eight_inputs)
    print('Standard Deviation is: ', round(numbers_std, 3))

    cons_skewness: float = (3)
    result_memo = numbers_mean - numbers_median
    result_skewm = cons_skewness * result_memo
    numbers_Skewness = round(result_skewm / numbers_std, 3)
    print('Skewness: ', numbers_Skewness)
    if numbers_Skewness < 0:
        print('Skewness is negatively skewed or skewed to the left')

    else:
        print('Skewness is positively skewed or skewed to the right')

elif choice == 'nine':
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('9 Inputs'.center(30, '-'))
    first_num = float(input('Enter number: '))
    second_num = float(input('Enter number: '))
    third_num = float(input('Enter number: '))
    fourth_num = float(input('Enter number: '))
    fifth_num = float(input('Enter number: '))
    sixth_num = float(input('Enter number: '))
    seventh_num = float(input('Enter number: '))
    eighth_num = float(input('Enter number: '))
    ninth_num = float(input('Enter number: '))

    nine_inputs = [first_num, second_num, third_num, fourth_num, fifth_num, sixth_num, seventh_num, eighth_num,
                   ninth_num]

    # Statistics Calculation
    numbers_mean = statistics.mean(nine_inputs)
    print('Mean is: ', numbers_mean)

    numbers_median = statistics.median(nine_inputs)
    print('Median is: ', numbers_median)

    numbers_std = numpy.std(nine_inputs)
    print('Standard Deviation is: ', round(numbers_std, 3))

    cons_skewness: float = (3)
    result_memo = numbers_mean - numbers_median
    result_skewm = cons_skewness * result_memo
    numbers_Skewness = round(result_skewm / numbers_std, 3)
    print('Skewness: ', numbers_Skewness)
    if numbers_Skewness < 0:
        print('Skewness is negatively skewed or skewed to the left')

    else:
        print('Skewness is positively skewed or skewed to the right')

elif choice == 'ten':
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n')
    print('10 Inputs'.center(30, '-'))
    first_num = float(input('Enter number: '))
    second_num = float(input('Enter number: '))
    third_num = float(input('Enter number: '))
    fourth_num = float(input('Enter number: '))
    fifth_num = float(input('Enter number: '))
    sixth_num = float(input('Enter number: '))
    seventh_num = float(input('Enter number: '))
    eighth_num = float(input('Enter number: '))
    ninth_num = float(input('Enter number: '))
    tenth_num = float(input('Enter number: '))

    ten_inputs = [first_num, second_num, third_num, fourth_num, fifth_num, sixth_num, seventh_num, eighth_num,
                   ninth_num, tenth_num]

    # Statistics Calculation
    print('\n\n')
    print('Result of Calculation')
    numbers_mean = statistics.mean(ten_inputs)
    print("Mean: ", numbers_mean)

    numbers_median = statistics.median(ten_inputs)
    print('Median: ', numbers_median)

    numbers_std = numpy.std(ten_inputs)
    print('Standard Deviation: ', round(numbers_std, 3))

    cons_skewness: float = (3)
    result_memo = numbers_mean - numbers_median
    result_skewm = cons_skewness * result_memo
    numbers_Skewness = round(result_skewm / numbers_std, 3)
    print('Skewness: ', numbers_Skewness)
    if numbers_Skewness < 0:
        print('Skewness is negatively skewed or skewed to the left')

    else:
        print('Skewness is positively skewed or skewed to the right')