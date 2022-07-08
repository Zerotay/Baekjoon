#include <stdio.h>

int	main()
{
	int	arr[42] = {0, };
	int	tmp;

	for(int i = 0; i < 10; i++)
	{
		scanf("%d", &tmp);
		arr[tmp % 42]++;
	}
	tmp = 0;
	for (int i = 0; i < 42; i++)
		if (arr[i])
			tmp++;
	printf("%d", tmp);
	return (0);
}