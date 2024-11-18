#Write a program that asks for the current temperature. If the temperature is 30 degrees or higher, print "It’s hot!" If it’s between 15 and 29, print "It’s warm." Otherwise, print "It’s cold."

def temp_check(temp):
    if temp > 30:
        return "It's hot!"
    elif temp >15 < 29:
        return "It's warm"
    else:
        return "It's Cold"
    
# Typeshii - X
temp = float(input("Enete the temperature: "))

print(f"The temperature is {temp}. {temp_check(temp)}")