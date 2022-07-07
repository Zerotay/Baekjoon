#include <stdio.h>
#include <stdlib.h>

int	main()
{
	int	num, l;
	int	*arr;
	int	a, b;

	scanf("%d", &num);
	l = num;
	if(!(arr = (int *)malloc(sizeof(int) * num)))
		return (0);
	while (num--)
	{
		scanf("%d %d", &a, &b);
		arr[num] = a + b;
	}
	for (int i = l - 1; i >= 0; i--)
		printf("%d\n", arr[i]);
	free(arr);
	return (0);
}