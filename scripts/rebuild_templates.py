#!/usr/bin/env python3
"""Rebuild the original self-contained HTML templates from GitHub-friendly chunks.

The chunks are plain UTF-8 slices of the uploaded original files. No artwork
is re-encoded or altered: we concatenate the fragments, verify SHA-256,
then write the original complete HTML files.
"""
from hashlib import sha256
from pathlib import Path

TEMPLATES = {
    "Cream_Slide_Cards_Starter_UPDATED.html": (
        "cream",
        "76fc4c6bbf5685613cad3eb5aee300c888c11206a0fb6bdd0179e776f2c3a13c",
    ),
    "Illustrated_Textbook_Starter_UPDATED.html": (
        "textbook",
        "2fa3128ab4c4f043a38f21fd0e773ba92974db8b2669ef53d7b7e77fd34416fd",
    ),
}

for destination, (prefix, expected_sha) in TEMPLATES.items():
    pieces = sorted(Path("fragments").glob(f"{prefix}-*.txt"))
    if len(pieces) != 12:
        raise RuntimeError(f"Expected 12 fragments for {prefix}, found {len(pieces)}")
    data = b"".join(piece.read_bytes() for piece in pieces)
    actual = sha256(data).hexdigest()
    if actual != expected_sha:
        raise RuntimeError(f"SHA-256 mismatch for {destination}: {actual}")
    Path(destination).write_bytes(data)
    print(f"Verified and restored {destination} ({len(data):,} bytes)")
