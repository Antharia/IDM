#include "Idm.h"

bool Idm::setup()
{
    bool success = true;
    if (SDL_Init (SDL_INIT_VIDEO) < 0)
    {
        SDL_Log ("Can't initialize SDL2. Error : %s", SDL_GetError());
        success = false;
    }

    window = SDL_CreateWindow(
            "IDM",
            SDL_WINDOWPOS_UNDEFINED,
            SDL_WINDOWPOS_UNDEFINED,
            800,
            600,
            SDL_WINDOW_OPENGL
            );

    if (window == NULL)
    {
        printf ("Could not create window : %s\n", SDL_GetError());
    }

    return success;
}

bool Idm::run()
{
    bool success = true;
    SDL_Delay(3000);
    return success;
}

bool Idm::close()
{
    bool success;
    SDL_DestroyWindow(window);
    SDL_Quit();
    return success;
}
