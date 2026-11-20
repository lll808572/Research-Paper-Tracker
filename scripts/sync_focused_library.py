"""Maintain explicit full-note copies without overwriting manually edited copies."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'focused_papers/rca_agent_reliability/catalog.json'


def digest(data):
    # Git may check out CRLF on Windows; line endings alone are not user edits.
    return hashlib.sha256(data.replace(b'\r\n', b'\n')).hexdigest()


def safe_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or path.suffix != '.md':
        raise ValueError(f'Invalid note path: {relative}')
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text(encoding='utf-8'))
    pending, errors, seen_ids, seen_copies = [], [], set(), set()
    for entry in catalog['papers']:
        if entry['paper_id'] in seen_ids:
            errors.append(f'Duplicate paper ID: {entry["paper_id"]}')
        seen_ids.add(entry['paper_id'])
        source = safe_path(entry['canonical'])
        if not source.is_file():
            errors.append(f'Missing canonical note: {source}')
            continue
        data = source.read_bytes()
        current_hash = digest(data)
        for relative in entry['copies']:
            if relative in seen_copies:
                errors.append(f'Duplicate copy target: {relative}')
            seen_copies.add(relative)
            target = safe_path(relative)
            if target == source:
                errors.append(f'Copy equals canonical: {relative}')
                continue
            existing_hash = digest(target.read_bytes()) if target.exists() else None
            if args.check:
                if existing_hash != current_hash:
                    errors.append(f'Missing or stale copy: {relative}')
            elif existing_hash not in (None, entry['synced_sha256'], current_hash):
                errors.append(f'Manually edited copy; preserved: {relative}')
            elif existing_hash != current_hash:
                pending.append((target, data))
        if args.check and entry['synced_sha256'] != current_hash:
            errors.append(f'Stale catalog hash: {entry["paper_id"]}')
        entry['synced_sha256'] = current_hash
    if errors:
        raise SystemExit('\n'.join(errors))
    # Validate every target before any write so a conflict leaves all copies intact.
    if not args.check:
        for target, data in pending:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{"Checked" if args.check else "Synced"}: {len(seen_ids)} papers, {len(seen_copies)} copies; changed {len(pending)} copies.')


if __name__ == '__main__':
    main()
