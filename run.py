"""
Field Scan — main entry point.

Usage:
    python run.py --images FOLDER --parcelles parcelles.geojson --out results/
"""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Field Scan: banana plantation health analysis")
    p.add_argument("--images", required=True, type=Path, help="Folder of input images (GeoTIFF / orthomosaic)")
    p.add_argument("--parcelles", required=True, type=Path, help="GeoJSON file with parcel polygons")
    p.add_argument("--out", required=True, type=Path, help="Output directory for maps and bulletin")
    p.add_argument("--no-gpu", action="store_true", help="Force CPU inference")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    print(f"[field-scan] images   : {args.images}")
    print(f"[field-scan] parcelles: {args.parcelles}")
    print(f"[field-scan] output   : {args.out}")

    # --- pipeline steps (to be implemented week by week) ---
    # from src.data.loader      import load_images
    # from src.data.indices      import compute_indices
    # from src.inference.counter import count_plants
    # from src.inference.disease import classify_leaves
    # from src.report.bulletin   import generate_bulletin

    print("[field-scan] pipeline not yet implemented — scaffold only.")


if __name__ == "__main__":
    main()
