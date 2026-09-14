# DocSnap

Automated receipt and invoice data extraction. Upload a photo of a receipt and the app pulls out the line items and prices, then exports them to CSV.

## How it works

1. **Image to text**: a DONUT vision model (`AdamCodd/donut-receipts-extract`) reads the receipt image through HuggingFace `transformers`
2. **Parse**: a regex extracts the item name and price pairs from the model tagged output
3. **Export**: results are written to CSV and displayed in a table

The interface is a Gradio app.

## Stack

- Python 3.11
- HuggingFace `transformers` with a DONUT image-to-text model
- PyTorch
- Gradio
- Docker

## Run it

### With Docker

```bash
docker build -t docsnap .
docker run -p 7860:7860 docsnap
```

### Locally

```bash
pip install -r requirements.txt
python main.py
```

## Status

MVP, 2024. Built as a foundation for further development.
