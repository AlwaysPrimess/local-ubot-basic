# __init__.py
# Memuat semua modul userbot otomatis
# Termasuk modul dengan prefix dinamis

from .help_mod import register as help_register
from .echo import register as echo_register
from .broadcast import register as broadcast_register
from .premium import register as premium_register
from .listuser import register as listuser_register

# Modul 06–10
from .mod_06_prefix import register as prefix_register
from .mod_07_share import register as share_register
from .mod_08_download import register as download_register
from .mod_09_stub import register as mod09_register
from .mod_10_stub import register as mod10_register

# Daftarkan semua modul ke client
def register_all(client):
    # Modul utama
    help_register(client)
    echo_register(client)
    broadcast_register(client)
    premium_register(client)
    listuser_register(client)

    # Modul 06–10
    prefix_register(client)
    share_register(client)
    download_register(client)
    mod09_register(client)
    mod10_register(client)

    # Modul stub 11–50
    for i in range(11, 51):
        mod_name = f"mod_{i:02}_stub"
        try:
            mod = __import__(f"userbot.modules.{mod_name}", fromlist=["register"])
            if hasattr(mod, "register"):
                mod.register(client)
        except Exception as e:
            print(f"Gagal load {mod_name}: {e}")
