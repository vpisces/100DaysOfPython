## Functions with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    full_name = f_name + " " + l_name
    return full_name.title()


#print(format_name("FAIyaz", "rAZA"))
formatted_name = format_name("faiYaz", "rAzA")
print(formatted_name)

print(format_name(
    input("What is your first name? "),
    input("What is your last name? ")
))