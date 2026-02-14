/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: namaloma <namaloma@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 12:16:34 by namaloma          #+#    #+#             */
/*   Updated: 2026/01/08 15:31:46 by namaloma         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*reader(int fd, char *residue, int *bytes)
{
	char	*buffer;
	char	*temp;

	if (!residue)
		residue = ft_calloc(1, sizeof(char));
	if (!residue)
		return (NULL);
	buffer = ft_calloc(BUFFER_SIZE + 1, sizeof(char));
	if (!buffer)
		return (free(residue), NULL);
	*bytes = 1;
	while (!ft_strchr(residue, '\n') && *bytes != 0)
	{
		*bytes = read(fd, buffer, BUFFER_SIZE);
		if (*bytes == -1)
			return (free(buffer), free(residue), NULL);
		buffer[*bytes] = '\0';
		temp = residue;
		residue = ft_strjoin(temp, buffer);
		free (temp);
		if (!residue)
			return (free(buffer), NULL);
	}
	return (free(buffer), residue);
}

static char	*net_line(char *residue)
{
	int		i;
	char	*net;

	i = 0;
	if (!residue[i])
		return (NULL);
	while (residue[i] && residue[i] != '\n')
		i++;
	net = ft_calloc(i + 2, sizeof(char));
	if (!net)
		return (NULL);
	i = 0;
	while (residue[i] && residue[i] != '\n')
	{
		net[i] = residue[i];
		i++;
	}
	if (residue[i] == '\n')
		net[i] = '\n';
	else
		net[i] = '\0';
	return (net);
}

static char	*rm_leftover(char *residue)
{
	char	*nl;
	char	*new;

	nl = ft_strchr(residue, '\n');
	if (!nl)
	{
		free (residue);
		return (NULL);
	}
	new = ft_strdup(nl + 1);
	if (!new)
		return (free(residue), NULL);
	free(residue);
	return (new);
}

char	*get_next_line(int fd)
{
	int			bytes;
	char		*next_line;
	static char	*residue;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	residue = reader(fd, residue, &bytes);
	if (!residue)
	{
		residue = NULL;
		return (NULL);
	}
	next_line = net_line(residue);
	residue = rm_leftover(residue);
	return (next_line);
}
