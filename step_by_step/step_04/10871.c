#include <stdio.h>
#include <stdlib.h>

int	main()
{
	int	n, x;
	int	*arr;

	scanf("%d %d", &n, &x);
	if (!(arr = (int *)malloc(sizeof(int) * n)))
		return (0);
	for (int i = 0; i < n; i++)
		scanf("%d", arr + i);
	for (int i = 0; i < n; i++)
		if (arr[i] < x)
			printf("%d ", arr[i]);
	free(arr);
	return (0);
}