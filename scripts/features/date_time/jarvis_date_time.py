# imports
import datetime


# do not remove inp=None the function format should be same, name can be change
# inp is the input from the user (query ask by user)
# you can use this inp inside the function. LOL, because you may need user input
# Function should return something because this is the output we want to show user
def tell_me_date(inp=None):
    # inp (do something if you want to do with inp)
    date = datetime.datetime.now().strftime("%b %d %Y")

    # the return format should be string only
    return date


def tell_me_time(inp=None):
    time = datetime.datetime.now().strftime("%H:%M")
    return time


# you can run and test your script by calling from main
if __name__ == '__main__':
    response = tell_me_date()
    print(response)
    response = tell_me_time()
    print(response)