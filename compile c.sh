gcc -c -fPIC -o num_multi.o num_multi.c
gcc -shared -o num_multi.so num_multi.o
