#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int hei;
    do
    {
        hei = get_int("Height: ");
    }
    while (hei < 1 || hei > 8);
    for (int a = 1; a <= hei; a++)
    {
        for (int c = 1; c <= hei - a; c++)
        {
            printf(" ");
        }
        for (int b = 1; b <= a; b++)
        {
            printf("#");
        }
        printf("\n");
    }
}