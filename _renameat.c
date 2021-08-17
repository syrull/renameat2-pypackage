// refs:
// https://gist.github.com/eatnumber1/f97ac7dad7b1f5a9721f#file-renameat2-c-L11
// https://github.com/asottile/rename-exchange/blob/master/main.c

#include <Python.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <sys/syscall.h>

#ifndef RENAME_EXCHANGE
#define RENAME_EXCHANGE 2
#endif

static PyObject *_rename_exchange(PyObject *self, PyObject *args) {
    char *path1 = NULL;
    char *path2 = NULL;

    if(!PyArg_ParseTuple(args, "ss", &path1, &path2)) {
        return NULL;
    }

    if (syscall(SYS_renameat2, AT_FDCWD, path1, AT_FDCWD, path2, RENAME_EXCHANGE)) {
        PyErr_SetFromErrno(PyExc_OSError);
        return NULL;
    } else {
        return Py_BuildValue("");
    }
}

static struct PyMethodDef methods[] = {
    {"rename_exchange", (PyCFunction)_rename_exchange, METH_VARARGS, "Python Interface for renameat2 function"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef rename_exchange_module = {
    PyModuleDef_HEAD_INIT,
    "_renameat",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit__renameat (void) {
    return PyModule_Create(&rename_exchange_module);
}