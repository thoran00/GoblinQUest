#new pet project: make a z/t stastistic calculator using python
#this will also let me experiment with using functions inside of functions!

#just gets the parameters for the one-sample tests
def parameters_two_sample():
    s1 = input("What is the first sample standard deviation?")
    s2 = input("What is the second sample standard deviation?")
    difference_of_population_mean = input("What is the claimed difference in population means? (probably zero)")
    x_bar_one = input("What is the mean of the first sample?")
    x_bar_two = input("What is the mean of the second sample?")

    return s1, s2, difference_of_population_mean, x_bar_one, x_bar_two

def converter_for_two(s1, s2, difference_of_population_mean, x_bar_one, x_bar_two):
    try:
        s1 = float(s1)
        s2 = float(s2)
        difference_of_population_mean = float(difference_of_population_mean)
        x_bar_one = float(x_bar_one)
        x_bar_two = float(x_bar_two)

    except ValueError:
        print("Error, the values have to be numbers")
        evaluator = True
        return evaluator, s1, s2, difference_of_population_mean, x_bar_one, x_bar_two

    if s1 < 0 or s2 < 0 or x_bar_one < 0 or x_bar_two < 0:
        print("""
        Error, neither of the sample standard deviations or means can be negative. Please re-enter these values
        """)
        evaluator = True
    else:
        evaluator = False

    return evaluator, s1, s2, difference_of_population_mean, x_bar_one, x_bar_two


def parameters():
    s = input('What is your sample standard deviation?')
    u = input('What is the claimed mean?')
    x_bar = input('What is the sample mean? ')

    return s, u, x_bar

#runs by some filters for the parameters in case the user enters in a string or a negative number
def converter(s, u, x_bar):
    try:
        s = float(s)
        u = float(u)
        x_bar = float(x_bar)

    except ValueError:
        print('Error: The values have to be numbers')
        evaluator = True
        #this was necessary in order for this filter to catch the error and return the loop back
        #to parameters
        return evaluator, s, u, x_bar

    if s < 0 or u < 0 or x_bar < 0:
        print("these numbers cannot be negative")
        evaluator = True
    else:
        evaluator = False

    #evaluator will allow the loop in the respective test function to restart if one of the filters fail
    #ie if evaluator = True
    return evaluator, s, u, x_bar

def t_test(n):
    print('Your sample size is', n)

    while True:
        s, u, x_bar = parameters()
        evaluator, s, u, x_bar = converter(s, u, x_bar)

        if evaluator == False:
            statistic = (x_bar - u) / (s/(n)**(1/2))
            break
        else:
            continue

    return statistic

def z_test(n):
    print("Your sample size is", n)

    while True:
        sigma, u, x_bar = parameters()
        evaluator, sigma, u, x_bar = converter(sigma, u, x_bar)

        if evaluator == False:
            statistic = (x_bar - u) / (sigma/(n)**(1/2))
            break
        else:
            continue

    return statistic

def two_sample_z(n1, n2):
    print(f"Your two sample sizes are {n1} and {n2}")

    while True:
        sigma1, sigma2, difference_of_population_mean, x_bar_one, x_bar_two = parameters_two_sample()
        evaluator, sigma1, sigma2, difference_of_population_mean, x_bar_one, x_bar_two = converter_for_two(sigma1, sigma2, difference_of_population_mean, x_bar_one, x_bar_two)

        if evaluator == False:
            statistic = ( (x_bar_one - x_bar_two) - (difference_of_population_mean) ) / ( ((sigma1**2) / n1) + ((sigma2**2) / n2) )**(1/2)
            break
        else:
            continue

    return statistic

def two_sample_t_pooled(n1, n2):
    print(f"Your two sample sizes are {n1} and {n2}")

    while True:
        s1, s2, difference_of_population_mean, x_bar_one, x_bar_two = parameters_two_sample()
        evaluator, s1, s2, difference_of_population_mean, x_bar_one, x_bar_two = converter_for_two(s1, s2, difference_of_population_mean, x_bar_one, x_bar_two)

        if evaluator == False:
            sp = (((n1-1)*(s1**2)+((n2-1)*(s2**2)))/((n1 + n2)-2))**(1/2)
            statistic = ((x_bar_one - x_bar_two) - difference_of_population_mean) / (sp * ((1/n1)+(1/n2))**(1/2))
            break
        else:
            continue

    return statistic
def two_sample_t_unpooled(n1, n2):
    print(f"Your two sample sizes are {n1} and {n2}")

    while True:
        s1, s2, difference_of_population_mean, x_bar_one, x_bar_two = parameters_two_sample()
        evaluator, s1, s2, difference_of_population_mean, x_bar_one, x_bar_two = converter_for_two(s1, s2, difference_of_population_mean, x_bar_one, x_bar_two)

        if evaluator == False:
            statistic = ( (x_bar_one - x_bar_two) - (difference_of_population_mean) ) / ( ((s1**2) / n1) + ((s2**2) / n2) )**(1/2)
            break
        else:
            continue

    return statistic
#The main program is run through this function. It simply assesses based on sample size and
#if the user wants to use a one or two-sample test which statistical test to use.
def z_t():
    print("Hello! Welcome to z/t test calculator for statistics!\n ")
    while True:
        one_or_two = input("Type '1' if you're doing a one-sample test, type '2' if you're doing a two-sample: ")
        if one_or_two == '1':
            print("\nConducting a one-sample test... ")
            while True:
                n = input('What is your sample size? ')
                try:
                    n = int(n)
                except ValueError:
                    print('Error, n must be a positive whole number ')
                    continue

                #catches the error if the user enters in a negative sample size
                if n < 0:
                    print("n cannot be negative")
                    continue
                # t-tests are used when the sample size is small (ie below 30)
                elif n < 30:
                    print("sample size is less than 30, one-sample t-test")
                    statistic = t_test(n)
                    break

                # z-tests are used when the sample size is at least 30 (which would just be all other
                #circumstances in this case)
                else:
                    print("sample size is at least 30, one-sample z-test")
                    statistic = z_test(n)
                    break
                break
            break




        elif one_or_two == '2':
            #I will write some code to do 2-sample z and t-tests soon
            print("Conducting a two-sample test...\n")
            while True:
                n1 = input("What is the sample size of the first sample?")
                n2 = input("What is the sample size of the second sample?")
                try:
                    n1 = int(n1)
                    n2 = int(n2)
                except ValueError:
                    print("Error, the sample sizes must be positive whole numbers.")
                    continue

                if n1 < 0 or n2 < 0:
                    print("Error, both sample sizes must be positive numbers")
                    continue
                elif n1 < 30 or n2 < 30:
                    print("Since one of the sample sizes is less than 30, will conduct a two-sample t-test")

                    while True:
                        pooled_or_not = input("""
'1' for unpooled (assuming unequal variances), '2' for pooled (assuming equal variances)
""")

                        if pooled_or_not == '1':
                            statistic = two_sample_t_unpooled(n1, n2)
                            break
                        elif pooled_or_not == '2':
                            statistic = two_sample_t_pooled(n1, n2)
                            break

                        else:
                            print("Error, press either 1 for unpooeld or 2 for pooled")
                            continue

                else:
                    print("Since both sample sizes are greater than 30, will use a two-sample z-test")
                    statistic = two_sample_z(n1, n2)
                    break
                break
            break

        else:
            #In case the user enters in something that isn't one or two
            print("Error, either '1' or '2': ")
            continue

    return "\nYour test statistic is {}".format(statistic)


print(z_t())
