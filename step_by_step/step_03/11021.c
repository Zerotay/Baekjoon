#include <stdio.h>
#include <stdlib.h>

int	main()
{
	int	t, n;
	int	a, b;
	int	*arr;

	scanf("%d", &t);
	n = t;
	if (!(arr = (int *)malloc(sizeof(int) * t)))
		return (0);
	while (t--)
	{
		scanf("%d %d", &a, &b);
		arr[t] = a + b;
	}
	for (int i = n - 1; i >= 0; i--)
		printf("Case #%d: %d\n", n - i, arr[i]);
	free(arr);
	return (0);
}