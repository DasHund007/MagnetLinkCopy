import pyperclip, time
from colorama import Fore, init

init(autoreset=True)
output_file = 'magnet_links.txt'

def check_clipboard():
    previous_clipboard, link_count = "", 0
    with open(output_file, 'w'): pass
    while True:
        try:
            current_clipboard = pyperclip.paste()
            if current_clipboard.startswith('magnet:?') and current_clipboard != previous_clipboard:
                with open(output_file, 'a') as f: f.write(current_clipboard + '\n')
                link_count += 1
                print(f"{Fore.GREEN}Link saved: {Fore.RED}{current_clipboard} {Fore.BLUE}x{link_count}")
            previous_clipboard = current_clipboard
            time.sleep(0.5)
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nClipboard monitoring stopped.")
            try:
                with open(output_file, 'r') as f:
                    all_links = f.read().strip()
                pyperclip.copy(all_links)
                print(Fore.CYAN + "All links copied to clipboard.")
            except Exception as e:
                print(Fore.RED + f"Error copying to clipboard: {e}")
            break

if __name__ == "__main__":
    print(Fore.YELLOW + "Clipboard monitoring started. Press Ctrl+C to stop.")
    check_clipboard()
