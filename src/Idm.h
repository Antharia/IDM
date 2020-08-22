// Idm class
#pragma once
#include <SDL2/SDL.h>

class Idm
{
    public:
        SDL_Window* window;
        SDL_Renderer* renderer;

        bool setup();
        bool run();
        bool close();
};
