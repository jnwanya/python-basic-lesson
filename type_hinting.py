from typing import List, Optional


def list_avg(sequence: Optional[List] = None) -> float:
    my_sequence = sequence or []
    return sum(my_sequence) / len(my_sequence)


