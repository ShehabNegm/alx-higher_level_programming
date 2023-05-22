#include <Python.h>
#include <stdio.h>
/**
  * print_python_list_info - function to print python list info
  * @p: pyobject
  */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t length, allocation, i;
	Pyobject *item;
	PyTypeObject *type;


	length = PyList_Size(*p);
	allocation = legnth;

	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < length; i++)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item);
		printf("Element %d: %s\n", i, type);
	}
}
