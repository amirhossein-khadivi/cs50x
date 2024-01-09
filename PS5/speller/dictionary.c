// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 12345;

// Hash table
node *table[N];
int dictionarysize = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hash_value = hash(word);
    for (node *n = table[hash_value]; n != NULL; n = n->next)
    {
        if (strcasecmp(word, n->word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    long sumation = 0;
    int b = 0;
    while (b < strlen(word))
    {
        sumation = sumation + tolower(word[b]);
        b++;
    }
    return sumation % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict_pointer = fopen (dictionary, "r");
    if (dictionary == NULL)
    {
        printf("unable to open file %s\n", dictionary);
        return false;
    }
    char next_word[LENGTH + 1];
    while (fscanf(dict_pointer, "%s", next_word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, next_word);
        int hash_value = hash(next_word);
        n->next = table[hash_value];
        table[hash_value] = n;
        dictionarysize += 1;
    }
    fclose (dict_pointer);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return dictionarysize;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int a = 0;
    while (a < N)
    {
        node *n = table[a];
        while (n != NULL)
        {
            node *temp = n;
            n = n->next;
            free(temp);
        }
        if (n == NULL && a == N - 1)
        {
            return true;
        }
        a++;
    }
    return false;
}
