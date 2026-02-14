/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: namaloma <namaloma@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 12:18:09 by namaloma          #+#    #+#             */
/*   Updated: 2026/01/08 14:18:42 by namaloma         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char		*cdest;
	const unsigned char	*csrc;

	if (!dest && !src)
		return (NULL);
	cdest = (unsigned char *)dest;
	csrc = (const unsigned char *)src;
	while (n--)
		*cdest++ = *csrc++;
	return (dest);
}

char	*ft_strchr(const char *s, int c)
{
	size_t	i;

	i = 0;
	while (s[i])
	{
		if (s[i] == c)
			return ((char *)s + i);
		i++;
	}
	if ((char)c == '\0')
		return ((char *)s + i);
	return (NULL);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*join;
	size_t	l1;
	size_t	l2;

	if (!s1 ||!s2)
		return (NULL);
	l1 = 0;
	while (s1[l1])
		l1++;
	l2 = 0;
	while (s2[l2])
		l2++;
	join = (char *)malloc(l1 + l2 + 1);
	if (!join)
		return (NULL);
	ft_memcpy(join, s1, l1);
	ft_memcpy(join + l1, s2, l2);
	join[l1 + l2] = '\0';
	return (join);
}

char	*ft_strdup(const char *s)
{
	char	*ds;
	size_t	i;
	size_t	len;

	len = 0;
	while (s[len])
	{
		len ++;
	}
	ds = (char *)malloc(sizeof (char) * (len + 1));
	if (!ds)
		return (NULL);
	i = 0;
	while (i < len)
	{
		ds[i] = s[i];
		i++;
	}
	ds [i] = '\0';
	return (ds);
}

void	*ft_calloc(size_t nmemb, size_t size)
{
	size_t	i;
	void	*res;
	size_t	total;

	if (nmemb != 0 && (nmemb * size) / nmemb != size)
		return (NULL);
	total = nmemb * size;
	if (total == 0)
		total = 1;
	res = malloc(total);
	if (! res)
		return (NULL);
	i = 0;
	while (i < total)
	{
		((unsigned char *)res)[i] = 0;
		i++;
	}
	return (res);
}
