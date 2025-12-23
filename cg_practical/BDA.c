#include <stdio.h>
#include <stdlib.h>
#include <graphics.h>
#include <conio.h>

void bresenham_line(int x0, int y0, int x1, int y1, int color)
{
	int dx = abs(x1 - x0);
	int dy = abs(y1 - y0);
	int sx = (x0 < x1) ? 1 : -1;
	int sy = (y0 < y1) ? 1 : -1;
	int err = dx - dy;

	while (1) {
		putpixel(x0, y0, color);
		if (x0 == x1 && y0 == y1)
			break;
		int e2 = 2 * err;
		if (e2 > -dy) {
			err -= dy;
			x0 += sx;
		}
		if (e2 < dx) {
			err += dx;
			y0 += sy;
		}
	}
}

int main(void)
{
	int gd = DETECT, gm;
	int x0, y0, x1, y1;

	printf("Enter x0 y0 x1 y1 (integer pixel coordinates) separated by spaces:\n");
	scanf("%d %d %d %d", &x0, &y0, &x1, &y1);

	initgraph(&gd, &gm, "c:\\Turboc3\\BGI"); 
	int maxx = getmaxx();
	int maxy = getmaxy();
	int midx = maxx / 2;
	int midy = maxy / 2;
	setcolor(LIGHTGRAY);
	for (int x = 0; x <= maxx; x += 8) putpixel(x, midy, LIGHTGRAY);
	for (int y = 0; y <= maxy; y += 8) putpixel(midx, y, LIGHTGRAY);

	setcolor(WHITE);
	bresenham_line(x0, y0, x1, y1, WHITE);

	putpixel(x0, y0, RED);
	putpixel(x1, y1, GREEN);

	printf("Line drawn. Press any key in the graphics window to exit...\n");
	getch();

	closegraph();
	return 0;
}
