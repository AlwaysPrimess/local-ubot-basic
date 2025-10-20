# __init__.py
# Auto load semua module di folder

import os
import importlib

def register_all(client):
    package_dir = os.path.dirname(__file__)

    for filename in os.listdir(package_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            modulename = filename[:-3]  # hapus ".py"
            try:
                mod = importlib.import_module(f"userbot.modules.{modulename}")
                if hasattr(mod, "register"):
                    mod.register(client)
                    print(f"[MODULE] Loaded: {modulename}")
                else:
                    print(f"[MODULE] Lewati (tidak ada register): {modulename}")
            except Exception as e:
                print(f"[ERROR] Gagal load {modulename}: {e}")
