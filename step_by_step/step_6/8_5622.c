#include <stdio.h>

int	main()
{
	int	time = 0;
	char	str[16];

	scanf("%s", str);
	for (int i = 0; str[i]; i++)
		if (str[i] <= 'C')
			time += 3;
		else if (str[i] <= 'F')
			time += 4;
		else if (str[i] <= 'I')
			time += 5;
		else if (str[i] <= 'L')
			time += 6;
		else if (str[i] <= 'O')
			time += 7;
		else if (str[i] <= 'S')
			time += 8;
		else if (str[i] <= 'V')
			time += 9;
		else
			time += 10;
	printf("%d", time);
	return (0);
}