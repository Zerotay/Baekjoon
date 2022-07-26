#include <stdio.h>
#include <stdlib.h>

void	swap(int **arr, int i, int j)
{
	int	tmp;

	tmp = (*arr)[i];
	(*arr)[i] = (*arr)[j];
	(*arr)[j] = tmp;
}

int	*sort(int *arr, int i, int j)
{
	int	pivot, k, l;

	if (j - i < 0)
		return (arr);
	if (j - i == 1)
	{
		if (arr[i] > arr[j])
			swap(&arr, i , j);
		return (arr);
	}
	pivot = i;
	k = i + 1;
	l = j;
	while (1)
	{
		while (arr[pivot] > arr[k])
			k++;
		while (arr[pivot] < arr[l])
			l--;
		if (k < l)
			swap(&arr, k, l);
		else
		{
			swap(&arr, pivot, l);
			break ;
		}
	}
	arr = sort(arr, i, l - 1);
	arr = sort(arr, l + 1, j);
	return (arr);
}

int	main()
{
	int	n;
	int	*arr;

	scanf("%d", &n);
	if (!(arr = (int *)malloc(sizeof(int) * n)))
		return (0);
	for(int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	arr = sort(arr, 0, n - 1);
	for(int i = 0; i < n; i++)
		printf("%d\n", arr[i]);
	free(arr);
	return (0);
}