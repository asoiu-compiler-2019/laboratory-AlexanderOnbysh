#include <stdio.h>
#include <math.h>

int a = 20;

int test(int a)
{
    printf("%d\n",a);
    return a;
}
int test3(int a)
{
    printf("%f\n", a);
    return a;
}
void test1(int b)
{
    printf("%d\n",b);
}

int main()
{
    int i = 0;
    for (i = 0; i < 10; i++){
        if (i % 2 == 0){
            test(i);
        }
    }
    test(a);
    test(a);
    test(10);
    test1(55);
    return 0;
}
