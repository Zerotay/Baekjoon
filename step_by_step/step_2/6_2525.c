#include <stdio.h>

int	main()
{
	int	h, m, t;
	int	time;

	scanf("%d %d %d", &h, &m, &t);
	time = h * 60 + m + t;
	printf("%d %d", (time / 60) % 24, time % 60);
	return (0);
}