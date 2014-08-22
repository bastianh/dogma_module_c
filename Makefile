
CXX=gcc
CXXFLAGS=-I/usr/include/python3.4m -fPIC -I/usr/local/Cellar/python3/3.4.0_1/Frameworks/Python.framework/Versions/3.4/include/python3.4m

.PHONY: all test clean install

all: clean _dogma.so test 

_dogma.so: dogma_wrap.o dogma_module.o
	$(CXX) -shared dogma_wrap.o dogma_module.o -ldogma -o _dogma.so  -lpython3.4m -L/usr/local/lib -L/usr/local/Cellar/python3/3.4.0_1/Frameworks/Python.framework/Versions/3.4/lib/

dogma_wrap.o: dogma_wrap.c
	$(CXX) -c dogma_wrap.c $(CXXFLAGS)

dogma_module.o: dogma_module.c
	$(CXX) -c dogma_module.c $(CXXFLAGS)

dogma_wrap.c: dogma.i
	swig -python dogma.i

clean:
	rm -rf *.o *.so dogma_wrap.c dogmy.py

test:
	python3 dogma_test.py

