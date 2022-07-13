#include <stdio.h>
#include <unistd.h>

int	main()
{
	int	n, r;
	char	s[20];

	scanf("%d", &n);
	while (n--)
	{
		scanf("%d %s", &r, s);
		for (int i = 0; s[i]; i++)
			for (int j = 0; j < r; j++)
				write(1, (s + i), 1);
		write(1, "\n", 1);
	}
	return (0);
}