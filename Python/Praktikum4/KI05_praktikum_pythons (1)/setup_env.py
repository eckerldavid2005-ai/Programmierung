#!/usr/bin/env python3
"""
setup_env.py - Reproduzierbares Setup der Kurs-Umgebung (KI).

Legt eine virtuelle Python-Umgebung an, installiert die benoetigten Pakete,
registriert den Jupyter-Kernel "KI kernel" und konfiguriert VS Code.

Laeuft auf Windows, macOS und Linux. Getestet mit Python 3.9+.

Aufruf:
    python setup_env.py                 # venv-Verzeichnis wird automatisch
                                        # erkannt (U:\\KI.venv im CIP-Pool,
                                        # sonst .venv neben diesem Skript)
    python setup_env.py --venv-dir D:\\KI.venv     # explizites Verzeichnis
    Umgebungsvariable KI_VENV_DIR geht vor dem Default.

Das Skript prueft zusaetzlich, ob der aufrufende Interpreter brauchbar ist
(kein Microsoft-Store-Stub, lauffaehig, Python >= 3.9).

Windows: einfach setup_env.bat doppelklicken.
macOS/Linux: sh setup_env.sh
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

PAKETE = ["matplotlib", "pandas", "scikit-learn", "ipykernel", "pytest"]
KERNEL_NAME = "ki_kernel"
KERNEL_DISPLAY = "KI kernel"


def is_windows() -> bool:
    return os.name == "nt"


def pruefe_interpreter() -> None:
    """Prueft, ob der laufende Interpreter wirklich brauchbar ist.

    Faengt zwei haeufige Windows-Faelle ab:
    1. Den Microsoft-Store-Stub (WindowsApps\\python.exe), der kein echtes
       Python ist, sondern nur den Store oeffnet.
    2. Kaputte/halb installierte Interpreter, die sich nicht mehr selbst
       ausfuehren lassen.
    """
    exe = Path(sys.executable)
    if is_windows() and "WindowsApps" in str(exe):
        raise RuntimeError(
            "Der aufgerufene Python-Interpreter ist nur der "
            "Microsoft-Store-Stub ({}) und kein echtes Python.\n"
            "Bitte Python von https://www.python.org/downloads/ installieren "
            "(Haken bei 'Add python.exe to PATH' setzen)\n"
            "oder das Setup mit 'py -3 setup_env.py' starten.".format(exe)
        )
    try:
        r = subprocess.run(
            [str(exe), "-c", "import sys, venv, pip; "
             "assert sys.version_info >= (3, 9)"],
            capture_output=True,
        )
    except OSError as e:
        raise RuntimeError(
            "Python-Interpreter liess sich nicht ausfuehren "
            "({}): {}".format(exe, e)
        )
    if r.returncode != 0:
        raise RuntimeError(
            "Der Python-Interpreter ist nicht benutzbar oder aelter als "
            "3.9: {}\nMeldung: {}".format(exe, r.stderr.decode(errors="replace"))
        )


def default_venv_dir(project: Path) -> Path:
    """Waehlt automatisch ein sinnvolles venv-Verzeichnis.

    Prioritaet:
    1. Umgebungsvariable KI_VENV_DIR (falls gesetzt)
    2. Laufwerk U: vorhanden (CIP-Pool) und Projekt liegt nicht auf U:
       -> U:\\KI.venv   (Home-Quota wird geschont)
    3. sonst: .venv direkt im Projektordner
    """
    env_dir = os.environ.get("KI_VENV_DIR")
    if env_dir:
        return Path(env_dir)
    if is_windows():
        u_drive = Path("U:\\")
        if u_drive.exists() and project.drive.upper() != "U:":
            return u_drive / "KI.venv"
    return project / ".venv"


def venv_python(venv_dir: Path) -> Path:
    """Pfad des Python-Interpreters im venv (plattformabhaengig)."""
    if is_windows():
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def run(cmd, **kwargs):
    """Fuehrt ein Kommando aus und bricht bei Fehler mit klarer Meldung ab."""
    print("  $ " + " ".join(str(c) for c in cmd))
    result = subprocess.run(
        [str(c) for c in cmd],
        check=False,
        **kwargs,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "Befehl fehlgeschlagen (Exit-Code {}): {}".format(
                result.returncode, " ".join(str(c) for c in cmd)
            )
        )
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Kurs-Umgebung einrichten")
    parser.add_argument(
        "--venv-dir",
        default=None,
        help="Verzeichnis der virtuellen Umgebung. "
        "Standard: automatisch erkannt (U:\\KI.venv im CIP-Pool, "
        "sonst .venv neben diesem Skript). Kann auch per "
        "Umgebungsvariable KI_VENV_DIR gesetzt werden.",
    )
    args = parser.parse_args()

    # Interpreter pruefen BEVOR irgendetwas installiert wird
    pruefe_interpreter()

    project = Path(__file__).resolve().parent
    venv_dir = Path(args.venv_dir) if args.venv_dir else default_venv_dir(project)
    venv_py = venv_python(venv_dir)
    base_python = sys.executable
    vscode_dir = project / ".vscode"

    print("Projekt : {}".format(project))
    print("Python  : {}".format(base_python))
    print("venv    : {}".format(venv_dir))
    if venv_dir == Path("U:\\KI.venv"):
        print("          (Laufwerk U: erkannt - venv liegt im CIP-Pool, "
              "Home-Quota wird geschont)")
    print()

    # [1/5] Virtuelle Umgebung anlegen
    print("[1/5] Erstelle virtuelle Umgebung ...")
    if venv_py.exists():
        print("  Existiert bereits - ueberspringe Erstellung.")
    else:
        venv_dir.parent.mkdir(parents=True, exist_ok=True)
        run([base_python, "-m", "venv", str(venv_dir)])

    # [2/5] Pakete installieren
    print("[2/5] Installiere Pakete (pip + {}) ...".format(", ".join(PAKETE)))
#    run([venv_py, "-m", "pip", "install", "--upgrade", "pip"])
    run([venv_py, "-m", "pip", "install"] + PAKETE)

    # [3/5] Jupyter-Kernel registrieren
    print('[3/5] Registriere Jupyter-Kernel "{}" ...'.format(KERNEL_DISPLAY))
    run([venv_py, "-m", "ipykernel", "install", "--user",
         "--name", KERNEL_NAME, "--display-name", KERNEL_DISPLAY])

    # [4/5] VS Code konfigurieren
    print("[4/5] Konfiguriere VS Code ...")
    vscode_dir.mkdir(parents=True, exist_ok=True)

    settings = {
        "python.defaultInterpreterPath": str(venv_py),
        "python.terminal.activateEnvironment": True,
        "jupyter.notebookFileRoot": "${workspaceFolder}",
        # pytest-Tests direkt im VS Code Test-Explorer sichtbar machen
        "python.testing.pytestEnabled": True,
        "python.testing.pytestArgs": ["tests"],
        "python.testing.unittestEnabled": False,
    }
    with open(vscode_dir / "settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4, ensure_ascii=True)
        f.write("\n")

    extensions = {
        "recommendations": ["ms-python.python", "ms-toolsai.jupyter"],
    }
    with open(vscode_dir / "extensions.json", "w", encoding="utf-8") as f:
        json.dump(extensions, f, indent=4, ensure_ascii=True)
        f.write("\n")

    # pytest konfigurieren: Tests liegen im Unterordner tests/
    tests_dir = project / "tests"
    tests_dir.mkdir(exist_ok=True)
    pytest_ini = project / "pytest.ini"
    if not pytest_ini.exists():
        pytest_ini.write_text(
            "[pytest]\n"
            "testpaths = tests\n"
            "\n",
            encoding="utf-8",
        )

    # [5/5] Installation pruefen
    print("[5/5] Ueberpruefe Installation ...")
    run([venv_py, "-c",
         "import matplotlib, pandas, sklearn, ipykernel, pytest; "
         "print('    Alle Pakete erfolgreich installiert.')"])

    print()
    print("Umgebung erfolgreich eingerichtet!")
    print("  Projekt : {}".format(project))
    print("  Python  : {}".format(venv_py))
    print("  Kernel  : {}".format(KERNEL_DISPLAY))
    print("  Tests   : {} (VS Code Testing-Ansicht)".format(project / "tests"))
    print()
    print("Naechste Schritte:")
    print("  1. VS Code oeffnen und den Projektordner auswaehlen")
    print("  2. Falls gefragt: empfohlene Erweiterungen installieren")
    print("  3. Python-Interpreter auf das venv setzen "
          "(unten rechts in VS Code)")

    code_exe = shutil.which("code")
    if code_exe:
        print()
        print("VS Code wird geoeffnet ...")
        subprocess.run([code_exe, str(project)])
    else:
        print()
        print("Hinweis: VS Code bitte manuell oeffnen: {}".format(project))

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (RuntimeError, OSError) as e:
        print()
        print("FEHLER: {}".format(e))
        print("Hinweis: Liegt Python 3.9 oder neuer installiert vor? "
              "Fehlermeldungen oben pruefen (z. B. keine Netzwerkverbindung).")
        sys.exit(1)
