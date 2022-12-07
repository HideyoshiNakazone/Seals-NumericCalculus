WORK=./yoshi_seals
PROCESS=$(WORK)/process
SHARED=$(WORK)/shared

SETUP_CYTHON=setup_cython.py

OBJS= $(PROCESS)/process.pyx $(SHARED)/array.pyx $(SETUP_CYTHON)

PYTHON?=python
PARALLEL?=$(shell ${PYTHON} -c 'import sys; print("-j5" if sys.version_info >= (3,5) else "")' || true)

all: $(OBJS)
	python3 $(SETUP_CYTHON) build_ext --inplace $(PARALLEL) && \
		rm -r build

clean:

	rm $(WORK)/**/*.cpython-310-x86_64-linux-gnu.so
	rm $(WORK)/**/*.c

