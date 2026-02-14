*This activity has been created as part of the 42 curriculum by namaloma.*

# libft_printf

## Description

**libft_printf** is a reimplementation of the standard C library function `printf`.
The goal of this project is to gain a deeper understanding of formatted output,
variadic functions, and low-level I/O in C.

This implementation reproduces the behavior of the original `printf` for the
mandatory format specifiers required by the 42 subject:
`%c`, `%s`, `%p`, `%d`, `%i`, `%u`, `%x`, `%X`, and `%%`.
The function prints formatted output to the standard output and returns the
number of characters written.

---


## Instructions

### Compilation

To compile the library, run:

```bash
make
```
This will generate the static library:
```bash
libftprintf.a
```
---
#### Usage:
Include the header file in your source code:
```c
    #include "ft_printf.h"
```
Compile your program with the library:
```c
    cc -Iincludes your_program.c libftprintf.a
```
## Algorithm and Design Choices
The format string is parsed character by character. When a '%' is encountered,
the following character is treated as a format specifier and dispatched to a
dedicated printing function.  
Variadic arguments are handled using va_list, va_start, and va_arg. Each
specifier is implemented in a separate function to keep the code modular and
readable.  
Numbers are printed using base conversion, and all output is written directly
using the write system call, without implementing buffer management, as required
by the subject.
The %p conversion prints pointer addresses in hexadecimal with a "0x" prefix,
and prints "(nil)" for a NULL pointer to match the behavior of the system printf.

## Resources
- Linux manual pages: man printf, man stdarg
- C reference documentation: https://en.cppreference.com
- Variadic functions tutorial: https://youtu.be/oDC208zvsdg?si=qnwdKKmhSKwqtXyY

## AI Usage
AI tools were used to clarify concepts related to variadic functions, analyze
edge cases of printf, review implementation choices.

