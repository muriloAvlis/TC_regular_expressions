import re
def first_mid_last_name(input:str) -> bool:
    expression = r"(?!^.*[A-Z]{2,}.*$)^[A-Za-z]*$"
    pattern = re.compile(expression)
    print(pattern.match(input))
        

    
test1 = "Murilo Cruz Silva"
# test2 = "Murilo Silva"

first_mid_last_name(test1)
# first_mid_last_name(test2)