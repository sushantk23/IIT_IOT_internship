
def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def ft_to_inch(ft):
    return ft * 12

def inch_to_cm(inch):
    return inch * 2.54

def distance_converter(distance, conversion_type, conversion_function):
    result = conversion_function(distance)
    print(f"{distance} {conversion_type} = {result}")

if __name__ == "__main__":
    
    distance = float(input("Enter a distance value: "))

    distance_converter(distance, "km to m", km_to_m)
    distance_converter(distance, "m to cm", m_to_cm)
    distance_converter(distance, "cm to mm", cm_to_mm)
    distance_converter(distance, "ft to inch", ft_to_inch)
    distance_converter(distance, "inch to cm", inch_to_cm)