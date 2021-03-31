import os
import platform

if __name__ == '__main__':
    print(f'System: {platform.system()}')
    print(f'Wydanie: {platform.release()}')
    print(f'Wersja: {platform.version()}')
    print(f'Pełne informacje o platformie: {platform.platform()}')
    print(f'Procesor: {platform.processor()}')
    print(f'Liczba rdzeni: {os.cpu_count()}')
    print(f'Architektura: {platform.architecture()[0]}')
    print(f'Linkable Format: {platform.architecture()[1]}')
    print(f'Nazwa hosta: {platform.node()}')
