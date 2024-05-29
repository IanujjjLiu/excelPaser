import pandas as pd
import sys

def parse_excel_to_txt(excel_file, output_txt_file):

    df = pd.read_excel(excel_file)


    with open(output_txt_file, 'w') as file:

        for column in df.columns:
            # Write the column name as the line title
            file.write(f"{column}:\n")
            # Iterate through each element in the column
            for element in df[column]:
                # Write the element followed by a colon
                file.write(f"{element}:\n")
            # Add a newline for separation between columns
            file.write("\n")

def main():
    
    excel_file = sys.argv[1]
    output_txt_file = sys.argv[2]
    
    parse_excel_to_txt(excel_file, output_txt_file)

if __name__ == '__main__':
    main()
