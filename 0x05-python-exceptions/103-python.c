#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: PyObject list pointer
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (Py_ssize_t i = 0; i < size; i++)
		{
			PyObject *item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: PyObject bytes pointer
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		char *s;
		Py_ssize_t size;
		PyBytes_AsStringAndSize(p, &s, &size);
		printf("[*] Size of the Python Bytes = %ld\n", size);
		printf("[*] Trying string: %s\n", s);
		printf("[*] First 10 bytes:");
		for (Py_ssize_t i = 0; i < size && i < 10; i++)
		{
			printf(" %02hhx", s[i]);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - Prints basic info about Python floats.
 * @p: PyObject float pointer
 */
void print_python_float(PyObject *p)
{
	if (PyFloat_Check(p))
	{
		double value = PyFloat_AsDouble(p);
		printf("[*] Python float\n");
		printf("  value: %lf\n", value);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
}

