#include <SDL2/SDL.h>
#include <stdio.h>
#include "Idm.h"

// HEADERS

bool setup();
void run();
void close();

// FUNCTIONS

bool setup()
{
    bool success = true;
    if (SDL_Init (SDL_INIT_VIDEO) < 0)
    {
        SDL_Log ("Can't initialize SDL2. Error : %s", SDL_GetError());
        success = false;
    }
    return success;
}

void run()
{
    SDL_Delay(3000);
}
void close()
{
    SDL_Quit();
}

// MAIN

int main (int argc, char* argv[])
{

    setup();

    Idm idm;
    idm.createWindow();

    run();

    idm.close();
    close();

    return 0;
}
