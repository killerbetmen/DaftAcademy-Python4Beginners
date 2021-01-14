"""
Napisz context manager - ContextPatcher,
który zaktualizuje podany słownik o inny podany słownik,
a po wyjściu z bloku with, przywróci oryginalny słownik.
"""

from copy import deepcopy


class ContextPatcher():
    def __init__(self, old_dict, update_dict):
        self._old_dict = old_dict
        self.update_dict = update_dict

    def __enter__(self):
        self.update_dict = deepcopy(self._old_dict)
        return self.update_dict

    def __exit__(self, type, value, traceback):
        return self._old_dict


original_dict = {"k1": "v1", "k2": "v2"}
with ContextPatcher(original_dict, {"k2": "v3"}) as super_dict:
    assert super_dict == {"k1": "v1", "k2": "v3"}


assert original_dict == {"k1": "v1", "k2": "v2"}