/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: namaloma <namaloma@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 10:57:40 by namaloma          #+#    #+#             */
/*   Updated: 2025/12/27 12:10:51 by namaloma         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printf(const char *format, ...)
{
	int			bytes;
	va_list		args;

	bytes = 0;
	va_start(args, format);
	while (*format)
	{
		if (*format == '%')
		{
			++format;
			if (*format)
				bytes += printform(*format, &args);
		}
		else
			bytes += write (1, format, 1);
		format ++;
	}
	va_end(args);
	return (bytes);
}
