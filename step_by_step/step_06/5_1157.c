#include <stdio.h>

int	main()
{
	char	s[1000000];
	int		alpha[26] = {0, };
	int i = -1;
	int max = 0;

	scanf("%s", s);
	while(s[++i])
		alpha[s[i] + (s[i] < 97) * 32 - 97]++;
	i = -1;
	while (++i < 26)
		if (alpha[i] > alpha[max])
			max = i;
	i = max;
	while (++i < 26)
		if (alpha[max] == alpha[i])
			max = -1;
	if (max < 0)
		printf("?");
	else
		printf("%c", max + 65);
	return (0);
}