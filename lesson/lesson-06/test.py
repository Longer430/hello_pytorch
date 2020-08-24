import os
BASE= os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE)
print(BASE_DIR)
print(BASE_DIR1)