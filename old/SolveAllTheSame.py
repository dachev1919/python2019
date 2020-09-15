from collections import Counter
from typing import List, Any
def all_the_same(elements: List[Any]) -> bool:
    try: 
        text = sorted(elements)
        count = Counter(text).most_common(len(elements))
        if len(count) > 1:
            return False
        else:
            return True
    except TypeError:
        return False

if __name__ == '__main__':
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True