def modules_of_python():
    def mod_time():
        # Import datetime from datetime below:
        from datetime import datetime
        current_time = datetime.now()
        print(current_time)
    
    def mod_random():
        # Import random below:
        import random
        #This variable creates a random list of numbers up to 99 since randint isn't inclusive
        random_list = [random.randint(1,100) for i in range(101)]
        # This variable is selecting a single number from the list
        randomer_number = random.choice(random_list)
        print(randomer_number)
        
    def mod_plot():
        # range of numbers from 1 - 12, inclusive
        numbers_a = range(1, 13)
        # range of 12 numbers between 1 - 1000, exclusive
        numbers_b = random.sample(range(1000), 12)
        
    def mod_decimal():
        # Import Decimal below:
        #Decimal deals w/transaction numbers
        from decimal import Decimal

        # Fix the floating point math below:
        two_decimal_points = Decimal('0.2') + Decimal('0.69')
        #The floating points are fixed by calling Decimal and treating the numbers as strings
        print(two_decimal_points)

        #The floating points are fixed by calling Decimal and treating the numbers as strings
        four_decimal_points = Decimal('0.53') * Decimal('0.65')
        print(four_decimal_points)
    
    def mod_scope():
        def mod_script():
            # Import library below:
            # from mod_library import always_three
            
            # Call your function below:
            # always_three()
        # def mod_library():
            def always_three():
                return 3
    mod_scope()
modules_of_python()