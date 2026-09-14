# DocSnap

Receipt and invoice data extraction prototype. The codebase can read a receipt photo with a vision model and export line items to CSV.

## How it works

`main.py` implements three stages:

1. **Image to text**: `img2text()` runs a DONUT vision model (`AdamCodd/donut-receipts-extract`) through HuggingFace `transformers`
2. **Parse**: `parse_items()` uses a regex to pull item name and price pairs from the tagged model output
3. **Export**: `save_to_csv()` writes those pairs to CSV

**Current state:** the Gradio interface is wired to `process_image()` only, which validates the input and returns its file path. The three stages above are implemented as functions but are **not yet connected to the interface**, so the running app does not yet produce a CSV. This README describes the code as written, not a completed pipeline.

## Stack

- Python 3.11
- HuggingFace `transformers` with a DONUT image-to-text model
- PyTorch
- Gradio
- Docker

## Run it

With Docker:

```bash
docker build -t docsnap .
docker run -p 7860:7860 docsnap
```

Locally:

```bash
pip install -r requirements.txt
python main.py
```

## Status

MVP, 2024. Extraction functions implemented; wiring them into the interface is the next step. See `NOTES.org` for the original project notes.
