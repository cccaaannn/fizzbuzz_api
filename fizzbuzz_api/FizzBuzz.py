# Write a program that prints the numbers from 1 to 100. 
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
#  For numbers which are multiples of both three and five print “FizzBuzz”.

class FizzBuzz:
    def __init__(self):
        self.custom_fizzbuzz_array = {
            "custom_fizzbuzz":[
                {"word":"fizz", "divisors":[3]},
                {"word":"buzz", "divisors":[5]},
                {"word":"fizzbuzz", "divisors":[3,5]}
            ]
        }

    def __is_divisor(self, num, divisors):
        # returns true if a number is divisible to all of the numbers in a list
        for divisor in divisors:
            if(num % divisor != 0):
                return False
        return True

    def __get_fizzbuzz_result(self, num, custom_fizzbuzz_array):
        # checks all requested divisor lists and returns correspounding word if exists if not returns number itself
        for custom_fizzbuzz in custom_fizzbuzz_array:
            if(self.__is_divisor(num, custom_fizzbuzz["divisors"])):
                return custom_fizzbuzz["word"]
        return str(num)

    def fizzbuzz_custom(self, custom_fizzbuzz_array, start=1, stop=100, to_list=False):
        """generates custom fizzbuzz

        Args:
            custom_fizzbuzz_dict ([type]):
            simple structure
            {
                "custom_fizzbuzz":[
                    {"word":"fizz", "divisors":[3]},
                    {"word":"buzz", "divisors":[5]},
                    {"word":"fizzbuzz", "divisors":[3,5]},
                ]
            }
            start (int, optional): start point. Defaults to 1.
            stop (int, optional): end point. Defaults to 100.
            to_list (bool, optional): convert to list. Defaults to False.
        """
        
        # sort the custom_fizzbuzz_array according to the length of the divisors lists. (longer list with more numbers will be tested first)
        sorted_custom_fizzbuzz_array = sorted(custom_fizzbuzz_array["custom_fizzbuzz"], key=(lambda x: len(x["divisors"])), reverse=True)

        ans = ""
        for num in range(start, stop + 1):
            ans += self.__get_fizzbuzz_result(num, sorted_custom_fizzbuzz_array)
            if(num != stop):
                ans += "\n"

        if(to_list):
            return ans.split("\n")
        else:
            return ans


    def fizzbuzz(self, **kwargs):
        # regular fizzbuzz
        return self.fizzbuzz_custom(self.custom_fizzbuzz_array, **kwargs)

