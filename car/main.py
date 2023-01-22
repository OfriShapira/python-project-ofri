from car.car_ex import Car

if __name__ == "__main__":
    try:
        car = Car()
        car.show_options()
    except Exception as e:
        print(e)
