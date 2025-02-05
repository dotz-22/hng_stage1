import requests

# number classifier

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
   
    num_str = str(abs(n))  # Convert number to string to extract digits
    num_digits = len(num_str)  # Count the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)  # Sum of each digit raised to power of num_digits
    
    return sum_of_powers == n  # Returns 

def is_perfect(n):
   
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def classify_number(n):
  
    is_arm =  is_armstrong(n) 
    parity = "odd" if n % 2 else "even"

    if is_arm  :
        properties = ["armstrong", parity]
    else:
        properties = [parity]

    return {
        "is_prime": is_prime(abs(n)),
        "is_perfect": is_perfect(abs(n)),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(n))),
    }


# number fun fact from numbersapi.com

def get_fun_fact(n):
    
    url = f"http://numbersapi.com/{n}/math"
    try:
        response = requests.get(url, timeout=10)  
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return "No fun fact available."


