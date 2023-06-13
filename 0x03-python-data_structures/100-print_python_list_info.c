#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - a funct that prints some basic info about pytohn list
* @p: python object
**/

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int m;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (m = 0; m < size; m++)
		printf("Element %m: %s\n", m, Py_TYPE(obj->ob_item[m])->tp_name);
}
