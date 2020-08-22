CC=g++
OUTPUT=idm
FLAGS=-lSDL2
SRC=src/*.cpp 
SRC_H=src/*.h

$(OUTPUT): $(SRC) $(SRC_H)
	$(CC) $(FLAGS) $(SRC) -o ./build/$(OUTPUT)

