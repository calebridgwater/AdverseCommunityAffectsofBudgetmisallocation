import pandas as pd
# Imports pandas library for reading excel data files.

def read_excel_file(file_path): 
    # Read the Excel file
    return pd.read_excel(file_path)
# Will read the excel file- in this case the excel data file of the 2021 census for state and local government budget line items. 

def main():
    
    budget_data_path = input("Enter the path to the budget data file: ")
    # Prompts user for path to data file for budgets at script execution, ensuring data paths are not stored on github and adds flexibility to the script for use of others. 
    # This will be used specifically for the '21slsstab' excel file.
    
    health_data_path = input("Enter the path to the health data file: ")
    # Prompts user for path to data file for budgets at script execution, ensuring data paths are not stored on github and adds flexibility to the script for use of others. 
    # This will be used specifically for the 'PLACES__Local_Data_for_Better_Health__Census_Tract_Data_2023_release_20231113' excel file.
    
    budget_data = read_excel_file(budget_data_path)
    
    health_data = read_excel_file(health_data_path)

    # Print the first few rows of each DataFrame to check
    print(budget_data.head())
    print(health_data.head())

    # Additional processing can go here

if __name__ == '__main__':
    main()
