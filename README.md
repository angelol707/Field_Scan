# Field Scan

AI pipeline that turns aerial images of a banana plantation into a per-parcel health bulletin: plant count, vigour map, water-stress map, and disease alerts.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python run.py --images FOLDER --parcelles parcelles.geojson --out results/
```

| Argument | Description |
|----------|-------------|
| `--images` | Folder of input images (GeoTIFF, orthomosaic, Sentinel-2) |
| `--parcelles` | GeoJSON file with parcel polygons |
| `--out` | Output directory (maps + bulletin) |
| `--no-gpu` | Force CPU-only inference |

## Outputs

| File | Description |
|------|-------------|
| `results/plants.geojson` | Detected plants with geolocation |
| `results/vigour.tif` | NDVI / ExG vigour raster |
| `results/water_stress.tif` | NDMI / NDWI water-stress raster |
| `results/bulletin.html` | Per-parcel health bulletin |

## Project structure

```
src/
  data/       # image loading, tiling, vegetation indices
  models/     # model definitions (detection, classification)
  inference/  # plant counting, disease classification
  report/     # bulletin generation
notebooks/    # exploration and experiments
data/         # local data (gitignored)
weights/      # trained model weights (gitignored)
results/      # pipeline outputs (gitignored)
data_notebook.md  # dataset provenance and licences
```

## Free compute

- Google Colab (T4 GPU) — save checkpoints to Drive
- Kaggle Notebooks — weekly GPU quota
