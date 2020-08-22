#include "Idm.h"

void Idm::createWindow()
{
    window = SDL_CreateWindow(
            "IDM",
            SDL_WINDOWPOS_UNDEFINED,
            SDL_WINDOWPOS_UNDEFINED,
            800,
            600,
            SDL_WINDOW_RESIZABLE
            );
    if (window == NULL)
    {
        printf ("Could not create window : %s\n", SDL_GetError());
    }
}

void Idm::close()
{
    SDL_DestroyWindow(window);
}
