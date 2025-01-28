def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if (number>10 ):
         return "Greater"
    if (number<10):
        return "lesser"
    else :
        return "equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum  =0
    for i in range (1 , n+1 ):
        sum += i
    return(sum )

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    Total_Sum= sum(numbers) 
    Total_max= max(numbers)
    Total_min= min (numbers)
    
    return(Total_Sum,Total_max,Total_min)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    above_80 = [] #initalizing value 0
    for key, value in students_dict.items():
        if value > 80 :
          above_80.append(key)

    return (above_80)

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_element =  set ( set(list1)&set(list2))
    
    return("common_element")
    

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    sum = float(a+b)
    diff = float (a-b)
    mult = float(a*b)
    try:
      div = float (a/b)
    except ZeroDivisionError :
        div =0 
        print (" Error ! : cannot divide by zero ")
    
    return (sum , diff ,mult ,div)


def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """ 
    dict_log = {"And": x and y , "OR": x or y , "xor": x or y }
    return(dict_log)

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    dit_bit = {"And": a & b , "OR": a | b  , "xor": a^b }
    return (dit_bit)