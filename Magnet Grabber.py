import pyperclip
import time
from colorama import Fore, init

init(autoreset=True)

output_file = 'magnet_links.txt'

def check_clipboard():
    previous_clipboard = ""
    link_count = 0

    with open(output_file, 'w') as f:
        f.truncate(0)

    while True:
        try:
            current_clipboard = pyperclip.paste()
            
            if current_clipboard.startswith('magnet:?') and current_clipboard != previous_clipboard:
                with open(output_file, 'a') as f:
                    f.write(current_clipboard + '\n')
                
                link_count += 1
                print(Fore.GREEN + "Link saved:")
                print(Fore.RED + current_clipboard)
                print(Fore.BLUE + "Magnet link copied to clipboard.")
                
                if link_count % 2 == 0:
                    print(Fore.YELLOW + "\n")

            previous_clipboard = current_clipboard
            time.sleep(0.5)

        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nClipboard monitoring stopped.")
            break

if __name__ == "__main__":
    print(Fore.YELLOW + "Clipboard monitoring started. Press Ctrl+C to stop.")
    check_clipboard()
