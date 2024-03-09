import pdal


def convert_e57_to_las(input_file, output_file):
    pipeline = {
        "pipeline": [
            {
                "type": "readers.e57",
                "filename": input_file
            },
            {
                "type": "writers.las",
                "filename": output_file
            }
        ]
    }


    try:
        pdal_pipeline = pdal.Pipeline(json.dumps(pipeline))
        pdal_pipeline.execute()
        print("Conversion completed successfully.")
    except pdal.PyPipelineError as e:
        print("Error:", e)


if __name__ == "__main__":
    import sys
    import json


    if len(sys.argv) != 3:
        print("Usage: python convert_e57_to_las.py <input.e57> <output.las>")
        sys.exit(1)


    input_file = sys.argv[1]
    output_file = sys.argv[2]


    convert_e57_to_las(input_file, output_file)
