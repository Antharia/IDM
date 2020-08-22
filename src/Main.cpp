#include <SDL2/SDL.h>
#include <stdio.h>
#include "Idm.h"

int main (int argc, char* argv[])
{
    Idm idm;

    idm.setup();
    idm.run();
    idm.close();

    return 0;
}
