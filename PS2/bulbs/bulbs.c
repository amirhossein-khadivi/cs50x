#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string word = get_string("Message: ");
    int length = strlen(word);
    int a = 0;
    while (a < length)
    {
        int binary[] = {0, 0, 0, 0, 0, 0, 0, 0};
        int decimal = word[a];

        int b = 0;
        while (decimal > 0)
        {
            binary[b] = decimal % 2;
            decimal = decimal / 2;
            b += 1;
        }
        for (int c = BITS_IN_BYTE - 1; c >= 0; c--)
        {
            print_bulb(binary[c]);
        }
        printf("\n");
        a += 1;
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}