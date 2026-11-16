
# https://thetech.academy/courses/301e7614-d433-4805-9861-cc50b3e58c7d/step/183

import app

def print_app2():
    name = (__name__)
    return name



# from within this file, __name__ will be "__main__" if run directly
if __name__ == "__main__":
    print(f"I am running code from {print_app2()}")


# imported app.py
    print(f"I am running code from {app.print_app()}")