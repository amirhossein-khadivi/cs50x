#include <math.h>
#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int red;
    int green;
    int blue;
    float gray;
    for (int a= 0; a < height; a++)
    {
        for (int b = 0; b < width; b++)
        {
            red = image[a][b].rgbtRed;
            blue = image[a][b].rgbtBlue;
            green = image[a][b].rgbtGreen;
            gray = round((red + blue + green) / 3.0);

            image[a][b].rgbtRed = gray;
            image[a][b].rgbtBlue = gray;
            image[a][b].rgbtGreen = gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int red, blue, green;
    int red2, blue2, green2;
    for (int a = 0; a < height; a++)
    {
        for (int b = 0; b < width; b++)
        {
            red = image[a][b].rgbtRed;
            blue = image[a][b].rgbtBlue;
            green = image[a][b].rgbtGreen;
            red2 = round(.393 * red + .769 * green + .189 * blue);
            green2 = round(.349 * red + .686 * green + .168 * blue);
            blue2 = round(.272 * red + .534 * green + .131 * blue);

            if (red2 > 255)
            {
                red2 = 255;
            }
            if (green2 > 255)
            {
                green2 = 255;
            }
            if (blue2 > 255)
            {
                blue2 = 255;
            }

            image[a][b].rgbtRed = red2;
            image[a][b].rgbtBlue = blue2;
            image[a][b].rgbtGreen = green2;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE rplace[width];
    for (int a = 0; a < height; a++)
    {
        for (int b = 0; b < width; b++)
        {
            rplace[b] = image[a][b];
        }
        for (int c = 0; c < width; c++)
        {
            image[a][c].rgbtRed = rplace[width - c - 1].rgbtRed;
            image[a][c].rgbtBlue = rplace[width - c - 1].rgbtBlue;
            image[a][c].rgbtGreen = rplace[width - c - 1].rgbtGreen;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            copy[h][w] = image[h][w];
        }
    }

    for (int a = 0; a < height; a++)
    {
        for (int b = 0; b < width; b++)
        {
            int count = 0;
            float rsum = 0;
            float gsum = 0;
            float bsum = 0;
            for (int c = -1; c < 2; c++)
            {
                for (int d = -1; d < 2; d++)
                {
                    if (!((a + c) < 0 || (a + c) >= height || (b + d) < 0 || (b + d) >= width))
                    {
                        rsum += copy[a + c][b + d].rgbtRed;
                        bsum += copy[a + c][b + d].rgbtBlue;
                        gsum += copy[a + c][b + d].rgbtGreen;
                        count++;
                    }
                    else
                    {
                        continue;
                    }
                }
            }
            image[a][b].rgbtBlue = (int) round(bsum / count);
            image[a][b].rgbtRed = (int) round(rsum / count);
            image[a][b].rgbtGreen = (int) round(gsum / count);
        }
    }
    return;
}
