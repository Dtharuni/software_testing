import datetime

def my_brand(hw_name):
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    screen_brand = f"=*=*=*= Tharuni D =*=*=*=\n\n" \
                  f"=*=*=*= Course 2023S-SSW567-WS =*=*=*=\n\n" \
                  f"=*=*=*= {hw_name} =*=*=*=\n\n" \
                  f"=*=*=*= {current_datetime} =*=*=*=\n"
    
    print(screen_brand)

my_brand("HW 00")

print("Hello World")