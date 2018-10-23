#include <Python.h>
long long
_fib(long long n) {

    int i, t1 = 0, t2 = 1, nextTerm;
    for (i = 1; i <= n; ++i)
    {
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
    return t2;
}
static PyObject *
fib(PyObject *self, PyObject *args) {
    long long n;
    if (!PyArg_ParseTuple(args, "L", &n))
        return NULL;
    return Py_BuildValue("L", _fib(n));
}
static PyMethodDef fib_methods[] = {
        {
                "fib_fast", fib,  METH_VARARGS, "Calcs fib."
        },
        {       NULL,       NULL, 0,            NULL}
};
static struct PyModuleDef fib_def =
        {
                PyModuleDef_HEAD_INIT,
                "alg.fib",
                "",
                -1,
                fib_methods
        };
PyMODINIT_FUNC PyInit_fib(void) {
    Py_Initialize();
    return PyModule_Create(&fib_def);
}
