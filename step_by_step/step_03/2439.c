#include <stdio.h>

int main()
{
	int	n;
	int	k;

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		k = 0;
		while (++k < n - i)
			printf(" ");
		while (k++ - 1 < n)
			printf("*");
		printf("\n");
	}
	return (0);
}