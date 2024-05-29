import pandas as pd
import sys

def parse_excel_to_txt(excel_file, output_txt_file):
    print(f"Reading Excel file: {excel_file}")
    df = pd.read_excel(excel_file)


    with open(output_txt_file, 'w') as file:

        for column in df.columns:
            
            file.write(f"{column}:\n")
            
            for element in df[column]:
          
                file.write(f"{element}:\n")
            
            file.write("\n")

def main():
    print('running')
    excel_file = sys.argv[1]
    output_txt_file = sys.argv[2]
    
    parse_excel_to_txt(excel_file, output_txt_file)

if __name__ == '__main__':
    main()
