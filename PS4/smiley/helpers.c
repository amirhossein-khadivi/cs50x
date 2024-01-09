#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    int i = 0;
    int j = 0;
    while (i < width)
    {
        while (j < height)
        {
            if (image[j][i].rgbtBlue == 0 && image[j][i].rgbtGreen == 0 && image[j][i].rgbtRed == 0)
            {
                image[j][i].rgbtBlue = 200;
                image[j][i].rgbtGreen = 150;
                image[j][i].rgbtRed = 170;
            }
            j++;
        }
        i++;
    }
}
