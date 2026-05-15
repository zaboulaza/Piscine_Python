import os
from time import sleep


def ft_tqdm(lst : range) -> None :
    range_ = len(lst)
    length_term = os.get_terminal_size().columns
    for i in lst :
        percent = i / range_ * 100
        bar_size = length_term - len(str(percent)) - len(str(i)) - len(str(range_)) - 7
        nb_egal = int(bar_size * percent / 100)
        load = "=" * nb_egal + ">"
        load = load.ljust(bar_size)
        print(f"{percent:.0f}%|[{load}]| {i}/{range_}".ljust(length_term), end="\r", flush=True)
        yield i    
    print(f"{percent:.0f}%|[{load}]| {range_}/{range_}".ljust(length_term))
