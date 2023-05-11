import json
import argparse

parser = argparse.ArgumentParser(description='Alpaca2INCITE-Dataset-Converter')
parser.add_argument('--input_file', type=str, help='the input JSON file', required=True)
parser.add_argument('--output_file', type=str, help='the output JSONL file', required=True)
parser.add_argument('--source', type=str, help='the optional source metadata for the JSONL entries', required=False)
args = parser.parse_args()

with open(args.input_file) as f:
    data = json.load(f)

with open(args.output_file, 'w') as f:
    for item in data:
        text = f"<human>: {item['instruction']}\n<bot>: {item['output']}"
        output = {"text": text}
        if args.source:
            output["metadata"] = {"source": args.source}
        f.write(json.dumps(output) + '\n')
