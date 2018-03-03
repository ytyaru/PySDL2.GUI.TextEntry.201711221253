import sys
import sdl2
import sdl2.ext

GREY = sdl2.ext.Color(200, 200, 200)
RED = sdl2.ext.Color(255, 0, 0)
GREEN = sdl2.ext.Color(0, 255, 0)

def run():
    sdl2.ext.init()
#    window = sdl2.ext.Window("PySDL2でTextEntryを作る", size=(800, 600))
#    window.show()

    #http://sdl2referencejp.osdn.jp/TextInput.html
#    sdl2.InitVideo()
#    sdl2.ext.InitVideo()
#    import sdl2.video
#    sdl2.video.SDL_VideoInit()
    sdl2.SDL_StartTextInput()

    window = sdl2.ext.Window("PySDL2でTextEntryを作る", size=(800, 600))
    window.show()

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_TEXTINPUT:
                print(event.text.text)
                print(event.text.text.decode('utf-8'))
            if event.type == sdl2.SDL_TEXTEDITING:
                print(event.edit.text)
                print(event.edit.start)
                print(event.edit.length)
                #https://qiita.com/dario_okazaki/items/8c6953166b336e83e417
                print(event.edit.text.decode('utf-8'))
            

if __name__ == "__main__":
    sys.exit(run())
