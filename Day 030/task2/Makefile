CC=gcc
FLAGS=-Wall

mtliani : exercise.c
	$(CC) $(FLAGS) -o exercise exercise.c

debug: exercise.c
	$(CC) $(FLAGS) -g -o debug_exercise exercise.c
	gdb -tui debug_exercise

obieqturi : exercise.o
	$(CC) $(FLAGS) -o exercise exercise.o

exercise.o : exercise.c
	$(CC) $(FLAGS) -c -o exercise.o exercise.c
