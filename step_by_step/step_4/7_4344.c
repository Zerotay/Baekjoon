#include <stdio.h>

int	main()
{
	int		n, num, grade, count, i;
	int		arr[1000];
	float	sum;


	scanf("%d", &n);
	while (n--)
	{
		scanf("%d", &num);
		sum = 0;
		i = 0;
		while(i < num)
		{
			scanf("%d", &grade);
			arr[i++] = grade;
			sum += (float)grade;
		}
		arr[num] = 0;
		sum /= num;
		count = 0;
		i = 0;
		while (i < num)
			if ((float)arr[i++] > sum)
				count++;
		printf("%.3f%%\n", (float)count / num * 100);
	}
	return (0);
}