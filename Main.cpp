#include <SDL2/SDL.h>
#include <stdio.h>

// HEADERS

bool setup();
void run();
void close();

// CLASSES

class Idm
{
    public:
        SDL_Window* window;
        SDL_Renderer* renderer;

        void createWindow()
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

        void close()
        {
            SDL_DestroyWindow(window);
        }
        
};

class Renderer
{

}

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
