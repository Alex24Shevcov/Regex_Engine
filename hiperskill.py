def one_simbol_regex(part_one, part_two) -> bool:
    if part_one == part_two or part_one == "." or part_one == "":
        return True
    elif part_one == "" and part_two == "":
        return True

    return False 


def word_regex(part_one, part_two) -> bool:
    if len(part_one) == 0 and len(part_two) != 0:
        return True
    elif len(part_one) != len(part_two):
        return False

    for i in range(len(part_two)):
        if part_one[i] != part_two[i]:
            if part_one[i] == ".":
                continue
            else:
                return False
    
    return True



def my_regex(part_one, part_two) -> bool:
    
    if len(part_one) > len(part_two):
        return False
    elif len(part_one) == 0 and len(part_two) >= 0:
        return True
    
    if part_one == part_two or ("." in part_one and len(part_two) >= 0):
        return True
    elif len(part_one) == len(part_two) and part_one != part_two:
        return False
    
    if part_two.find(part_one) > -1:
        return True
    return False
    


def start_and_end_regex(part_one, part_two) -> bool:
    if "^" in part_one and "$" not in part_one:
        part_one = part_one[1:]
        section_text = part_two[:len(part_one)]

        return True if part_one == section_text else False
    
    elif "^" in part_one and "$" in part_one:
        part_one = part_one[1:-1]

        return True if part_one == part_two else False
    elif "^" not in part_one and "$" in part_one:
        part_one = part_one[:-1]

        part_two = part_two[-len(part_one):]
        
        return True if part_one == part_two else False



def my_count(string, search_simbol, pos) -> int:
    
    counter = 0
    for i in string[pos:]:
        if search_simbol == i:
            counter += 1
        else:
            break
    return counter



def regex_star_plus_question(part_one, part_two) -> tuple:
    lol_bird = False
    lol_dollar = False
    if "^" in part_one:
        part_one = part_one.replace("^", "") 
        lol_bird = True
    if "$" in part_one:
        lol_dollar = True
        part_one = part_one.replace("$", "") 

    if "+" in part_one:
        index_simbol_before_plus = part_one.find("+") - 1

        if part_one[index_simbol_before_plus] == ".":
            part_one = part_one[:part_one.find("+") - 1] + part_two[part_one.find("+") - 1] + part_one[part_one.find("+") - 1:]

        


        if part_two[index_simbol_before_plus] != part_one[index_simbol_before_plus]:
            print(False)
            exit(0)

        count_simbols = my_count(part_two, 
        part_two[index_simbol_before_plus],
         index_simbol_before_plus + 1)
        
        for i in range(count_simbols):
            part_one = part_one[:part_one.find("+") - 1] + part_one[part_one.find("+") - 1] + part_one[part_one.find("+") - 1:]

        
        part_one = part_one[:part_one.find("+")] + part_one[part_one.find("+") + 1:]


    if "*" in part_one:
        index_simbol_before_star = part_one.find("*") - 1

        if part_one[index_simbol_before_star] == ".":
            print(True)
            exit(0)
        


        if part_two[index_simbol_before_star] != part_one[index_simbol_before_star]:
            part_one = part_one[:index_simbol_before_star] + part_one[index_simbol_before_star + 1:]

        count_simbols = my_count(part_two, 
            part_two[index_simbol_before_star],
            index_simbol_before_star + 1)
            
        for i in range(count_simbols):
            part_one = part_one[:part_one.find("*") - 1] + part_one[part_one.find("*") - 1] + part_one[part_one.find("*") - 1:]
        
        part_one = part_one[:part_one.find("*")] + part_one[part_one.find("*") + 1:]
    
    
    if "?" in part_one:
        index_simbol_before_question_mark = part_one.find("?") - 1

        if part_one[index_simbol_before_question_mark] == ".":
            print(True)
            exit(0)


        if part_two[index_simbol_before_question_mark] != part_one[index_simbol_before_question_mark]:
            part_one = part_one[:index_simbol_before_question_mark] + part_one[index_simbol_before_question_mark + 1:]
        
        part_one = part_one[:part_one.find("?")] + part_one[part_one.find("?") + 1:]

    
    if lol_bird:
        part_one = "^" + part_one
    if lol_dollar:
        part_one = part_one + "$" 


    return part_one, part_two


def point_processing(part_one, part_two) -> tuple:

    lol_bird = False
    lol_dollar = False
    if "^" in part_one:
        part_one = part_one.replace("^", "") 
        lol_bird = True
    if "$" in part_one:
        lol_dollar = True
        part_one = part_one.replace("$", "") 


    if "*" in part_one:
        if part_one[-1] != "*":
            index_simbol_after_sign = -part_one.find("*")
        else:
            index_simbol_after_sign = len(part_two)

        part_two = part_two[:part_one.find("*") - 1] + part_two[index_simbol_after_sign:]            
        part_one = part_one.replace("*", "")
        part_one = part_one.replace(".", "")

    elif "+" in part_one:
        if part_one[-1] != "+":
            index_simbol_after_sign = -part_one.find("+")
        else:
            index_simbol_after_sign = len(part_two)
        
        part_two = part_two[:part_one.find("+") - 1] + part_two[index_simbol_after_sign:]
        part_one = part_one.replace("+", "")
        part_one = part_one.replace(".", "")


    elif lol_bird == False and lol_dollar == True:
            part_one = part_one[::-1]
            part_two = part_two[::-1]

            part_one = part_one.replace("$", "")
            for i in range(len(part_one)):
                    if part_one[i] == ".":
                        part_two = part_two[:i] + "."\
                            + part_two[i + 1:]


            part_one = part_one[::-1]
            part_two = part_two[::-1]

    elif lol_bird == True and lol_dollar == True:
        part_one = part_one.replace("$", "")
        part_one = part_one.replace("^", "")

        for i in range(len(part_one)):
                if part_one[i] == ".":
                    part_two = part_two[:i] + "."\
                        + part_two[i + 1:]

    
    if lol_bird:
        part_one = "^" + part_one
    if lol_dollar:
        part_one = part_one + "$" 

    return part_one, part_two



def backslash_regex(part_one, part_two):
    index_backslash = part_one.find("\\")
    part_one = part_one[:index_backslash] + part_one[index_backslash + 1:]

    try:
        if part_one[index_backslash + 1] == "$":
            return part_one, part_two
    except IndexError:
        ...
    try:
        if part_one[index_backslash - 1] == "^":
            return part_one, part_two
    except IndexError:
        ...
    part_one = part_one[:index_backslash] + part_one[index_backslash + 1:]
    part_two = part_two[:index_backslash] + part_two[index_backslash + 1:]

    return part_one, part_two

    





if __name__ == "__main__":
    regex_input = input()
    part_one, part_two = regex_input.split("|")

    if "\\" in part_one:
        part_one, part_two = backslash_regex(part_one, part_two)

    if "." in part_one:
        part_one, part_two = point_processing(part_one, part_two)

    if "+" in part_one or "*" in part_one or "?" in part_one:
        part_one, part_two = regex_star_plus_question(part_one, part_two)


    if len(part_one) <= 1 and len(part_two) == 1:
        print(one_simbol_regex(part_one, part_two))
    
    elif "^" in part_one or "$" in part_one:
        print(start_and_end_regex(part_one, part_two))

    else:
        print(my_regex(part_one, part_two))
