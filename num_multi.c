#include "num_multi.h"

float mult(int int_numb, float float_numb){
    float result = int_numb * float_numb;
    printf("In num_multi.c, the result of %d * %f is: %f \n",int_numb, float_numb, result);
    return result;
}