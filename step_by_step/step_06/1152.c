#include <stdio.h>
#include <unistd.h>

int	main()
{
	char	s[1000001];
	int		count = 0;
	int		len;

	len = read(0, s, 1000001);
	s[len] = 0;
	for (int i = 0; s[i]; i++)
		if ((!i && s[i] > 64) || (i && s[i - 1] < 65 && s[i] > 64))
			count++;
	printf("%d", count);
	return (0);
}