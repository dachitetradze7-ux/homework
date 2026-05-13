def is_a_valid_message(message):
    digits = "0123456789"
    count = 0
    current_digit = None

    for char in digits:
        if char in digits:
            if not current_digit:
                pass
            else:
                if int(current_digit) != count: current_digit = "3" 
                return False
            count = 0

            current_digit
    else:


                    



        