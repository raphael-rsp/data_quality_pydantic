#!/usr/bin/env python3
import re
import sys
from pathlib import Path

DAG_ID_PATTERN = re.compile(r"dag_id\s*=\s*['\"]([^'\"]+)['\"]")


def extract_dag_ids(path: Path) -> list[str]:
    """
    Lê o ficheiro e extrai todos os valores de 'dag_id' usando regex.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"[ERRO DE LEITURA] {path}: {e}", file=sys.stderr)
        return []
    return list(set(DAG_ID_PATTERN.findall(text)))


def find_all_dag_files(base_dir: Path) -> list[Path]:
    """
    Retorna uma lista de todos os arquivos Python dentro da pasta 'dags' (recursivo).
    """
    return [f for f in base_dir.rglob("*.py") if "dags" in str(f)]


def main(argv=None):
    """
    Itera sobre todos os ficheiros e verifica duplicatas de dag_id,
    incluindo subpastas dentro de 'dags/'.
    """
    base_dir = Path.cwd() / "dags"
    found_dag_ids: dict[str, list[Path]] = {}

    # Se o pre-commit passar arquivos específicos, usa-os.
    # Caso contrário, busca todos os .py dentro de dags/
    if len(sys.argv) > 1:
        files_to_check = [Path(f) for f in sys.argv[1:] if f.endswith(".py")]
    else:
        files_to_check = find_all_dag_files(base_dir)

    for path in files_to_check:
        if path.exists() and path.suffix == ".py":
            ids_in_file = extract_dag_ids(path)
            for dag_id in ids_in_file:
                found_dag_ids.setdefault(dag_id, []).append(path)

    has_duplicates = False

    for dag_id, paths in found_dag_ids.items():
        if len(paths) > 1:
            print("--------------------------------------------------")
            print(f"[ERRO FATAL] DAG ID DUPLICADO DETETADO: '{dag_id}'")
            print("Encontrado nos seguintes ficheiros:")
            for p in paths:
                print(f"  -> {p}")
            print("--------------------------------------------------")
            has_duplicates = True

    return 1 if has_duplicates else 0


if __name__ == "__main__":
    sys.exit(main())
