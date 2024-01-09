#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
   if (argc < 2)
   {
        printf("Usage: ./recover IMAGE\n");
        return 1;
   }

   FILE *d = fopen(argv[1], "r");
   unsigned char *t = malloc(1024);

   char *fn = malloc(4 * sizeof(int));
   int image = 0;

   if (t == NULL)
   {
        return 1;
   }
   if (fn == NULL )
   {
        return 1;
   }

   FILE *imgf = NULL;
   while (fread(t, sizeof(unsigned char), 512, d))
   {
        if (t[0] == 0xff && t[1] == 0xd8 && t[2] == 0xff && (t[3] & 0xf0) == 0xe0)
        {
            if (image != 0)
            {
                fclose(imgf);
            }
            sprintf(fn, "%03i.jpg", image);
            imgf = fopen(fn, "w");
            image += 1;
        }
        if (image != 0)
        {
            fwrite(t, 1, 512, imgf);
        }
   }
   if (image != 0)
   {
        fclose(imgf);
   }
   fclose(d);
   free(fn);
   free(t);

}
