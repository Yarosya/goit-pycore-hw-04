import sys
from pathlib import Path
from colorama import init, Fore

init()

def display_directory_structure(path: Path,level = 0):
    if path.is_dir():
        print(Fore.BLUE + "   " * level + f"📂{path.name}/")
        try:
            for child in path.iterdir():
                display_directory_structure(child,level+1)
        except PermissionError:
            print(Fore.RED + "  " * (level + 1) + "📜Доступ заборонено")

    else:
        print(Fore.GREEN + "  " * (level + 1) + f'📜{path.name}')

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: Введіть шлях до директорії.")
        sys.exit(1)
    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + 'Помилка: такої директорії не існує')
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + 'Помилка: Вказаний шлях не веде до директорії.')
        sys.exit(1)

    display_directory_structure(dir_path)

if __name__ == "__main__":
    main()




