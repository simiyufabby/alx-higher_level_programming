#include <Python.h>

/**
 * print_python_string - Print information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	/* Make sure p is a string object */
	if (!PyUnicode_Check(p))
	{
	printf("[ERROR] Invalid String Object\n");
	return;
	}
	/* Get the length of the string and print it */
	length = PyUnicode_GET_LENGTH(p);
	printf("  length: %ld\n", length);

	/* Check the kind of string representation */
	if (PyUnicode_IS_COMPACT_ASCII(p))
	printf("  type: compact ascii\n");
	else
	printf("  type: compact unicode object\n");
	/* Print the string as a Python Unicode object and as a C string */
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
