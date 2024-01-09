#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    float L = 100 * ((float) count_letters(text) / (float) count_words(text));
    float S = 100 * ((float) count_sentences(text) / (float) count_words(text));
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    float length = strlen(text);
    int letter = 0;
    for (int a = 0; a < length; a++)
    {
        if ((text[a] >= 97 && text[a] <= 122) || (text[a] >= 65 && text[a] <= 90))
        {
            letter += 1;
        }
    }
    return letter;
}

int count_words(string text)
{
    float length = strlen(text);
    int word = 1;
    for (int b = 0; b < length; b++)
    {
        if (text[b] == 32)
        {
            word += 1;
        }
    }
    return word;
}

int count_sentences(string text)
{
    float length = strlen(text);
    int sentence = 0;
    for (int c = 0; c < length; c++)
    {
        if (text[c] == 63 || text[c] == 33 || text[c] == 46)
        {
            sentence += 1;
        }
    }
    return sentence;
}