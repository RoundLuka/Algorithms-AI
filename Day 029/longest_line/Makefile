CC=gcc
FLAGS=-Wall

mtliani : longest_line.c
#.PHONY: mtliani
	@echo
	$(CC) $(FLAGS) -o lon_lin longest_line.c
	@echo


debug: longest_line.c
#.PHONY: debug
	$(CC) $(FLAGS) -g -o glon_lin longest_line.c
	gdb -tui glon_lin

obieqturi : lon_lin.o
	$(CC) $(FLAGS) -o lon_lin lon_lin.o

lon_lin.o : longest_line.c
	$(CC) $(FLAGS) -c -o lon_lin.o longest_line.c

didi : main.c longest.h copy.c get_line.c
	$(CC) $(FLAGS) -o udidesi main.c longest.h copy.c get_line.c


swori : copy.o main.o get_line.o
.PHONY: swori
	$(CC) $(FLAGS) -o maqsimaluri main.o copy.o get_line.o longest.h

copy.o : copy.c
	$(CC) $(FLAGS) -c -o copy.o copy.c

main.o : main.c
	$(CC) $(FLAGS) -c -o main.o main.c

get_line.o : get_line.c
	$(CC) $(FLAGS) -c -o getline.o get_line.c
