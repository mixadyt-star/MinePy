import colorama
import sys

colorama.init()

verbosity_level = 1

def set_verbosity_level(level: int):
    global verbosity_level

    verbosity_level = level

def log(message: str, level: int = 1, **kwargs):
    global verbosity_level

    if (verbosity_level >= level):
        print(colorama.Fore.GREEN + f"[{sys._getframe(1).f_globals['__name__'].replace('__', '')} INFO] {message}" + colorama.Fore.RESET, **kwargs)

def warn(message: str, level: int = 1, **kwargs):
    global verbosity_level

    if (verbosity_level >= level):
        print(colorama.Fore.YELLOW + f"[{sys._getframe(1).f_globals['__name__'].replace('__', '')} WARNING] {message}" + colorama.Fore.RESET, **kwargs)

def err(message: str, level: int = 1, **kwargs):
    global verbosity_level

    if (verbosity_level >= level):
        print(colorama.Fore.RED + f"[{sys._getframe(1).f_globals['__name__'].replace('__', '')} ERROR] {message}" + colorama.Fore.RESET, **kwargs)

def show_self(cls: object, level: int = 1):
    global verbosity_level

    if (verbosity_level >= level):
        print(colorama.Fore.GREEN + f"[{sys._getframe(1).f_globals['__name__'].replace('__', '')} INFO] Content of class {cls.__class__.__name__}:" + colorama.Fore.RESET)

        for key, value in vars(cls).items():
            print(colorama.Fore.GREEN + f"\t{key}: {value}" + colorama.Fore.RESET, flush=True)
        