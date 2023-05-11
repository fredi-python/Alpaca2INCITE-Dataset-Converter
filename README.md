# Alpaca2INCITE-Dataset-Converter
This Python script converts datasets in the Alpaca-data format to the jsonl format needed to fine-tune the RedPajama-INCITE language model. The RedPajama-INCITE model is a commercially-usable language model developed by Together Computer, with a 3B and a 7B parameter pretrained language model.
## Usage:
```
$ python3 convert.py -h
usage: convert.py [-h] --input_file INPUT_FILE --output_file OUTPUT_FILE [--source SOURCE]

Alpaca2INCITE-Dataset-Converter

options:
  -h, --help            show this help message and exit
  --input_file INPUT_FILE
                        the input JSON file
  --output_file OUTPUT_FILE
                        the output JSONL file
  --source SOURCE       the optional source metadata for the JSONL entries
  
```
