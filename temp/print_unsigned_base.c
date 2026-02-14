/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_unsigned_base.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: namaloma <namaloma@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/24 14:33:32 by namaloma          #+#    #+#             */
/*   Updated: 2025/12/24 14:33:35 by namaloma         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	print_unsigned_base(unsigned long num, char *base)
{
	int		count;
	size_t	base_len;

	count = 0;
	base_len = 0;
	while (base[base_len])
		base_len++;
	if (num >= base_len)
		count += print_unsigned_base(num / base_len, base);
	count += write (1, &base[num % base_len], 1);
	return (count);
}
