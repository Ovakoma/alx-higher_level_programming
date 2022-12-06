import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l_b = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l_b = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l_b = []
lib.print_python_list_info(l)
l_b.append(0)
lib.print_python_list_info(l)
l_b.append(1)
l_b.append(2)
l_b.append(3)
l_b.append(4)
lib.print_python_list_info(l)
l_b.pop()
lib.print_python_list_info(l)
