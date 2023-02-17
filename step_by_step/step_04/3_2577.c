#include <stdio.h>

int	main()
{
	int	tmp, sum;
	int	i;
	int	arr[10] = {0,};

	i = 0;
	sum = 1;
	while(i++ < 3)
	{
		scanf("%d", &tmp);
		sum *= tmp;
	}
	while (sum)
	{
		arr[sum % 10]++;
		sum /= 10;
	}
	i = 0;
	while (i < 10)
		printf("%d\n", arr[i++]);
	return (0);
}