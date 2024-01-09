#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startsize;
    do
    {
        startsize = get_int("start size: ");
    }
    while (startsize < 9);

    // TODO: Prompt for end size
    int endsize;
    do
    {
        endsize = get_int("end size: ");
    }
    while (endsize < startsize);

    // TODO: Calculate number of years until we reach threshold
    int year = 0;
    while (startsize < endsize)
    {
        if (startsize == endsize)
        {
            printf("Years: 0\n");
            break;
        }
        startsize = startsize + (startsize / 3) - (startsize / 4);
        year += 1;
    }

    // TODO: Print number of years
    printf("Years: %i\n", year);
}
