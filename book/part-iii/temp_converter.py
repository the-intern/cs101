def to_fahrenheit():
    # °F = (°C × 9/5) + 32
    userinput = input("Please enter the temperature you want to convert: ")
    userinput_to_int = int(userinput)
    celsius_temp = userinput_to_int * 9 / 5 + 32
    print(
        f"The temperature in celsius of {userinput_to_int} degrees is equivalent to {celsius_temp} degrees in fahrenheit."
    )
