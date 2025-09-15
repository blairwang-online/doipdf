import pandas as pd

# Adapted from https://stackoverflow.com/questions/9161439/parse-key-value-pairs-in-a-text-file
secrets = {}
with open("secrets_csvmode.txt") as myfile:
    for line in myfile:
        key, value = line.split("=")
        secrets[key.strip()] = value.strip()

def get_pdf_from_doi(given_doi):
  given_doi = given_doi.lower()
  df_mappingfile = pd.read_csv(secrets["doipdf_mappingfile_csv"])
  
  # Use str.lower() on each element individually
  df_lookup_doi = df_mappingfile[df_mappingfile['doi'].str.lower() == given_doi]
  
  if not df_lookup_doi.empty:
    df_lookup_doi_path_to_file = df_lookup_doi[['path_to_file']]
    df_lookup_doi_filename = df_lookup_doi[['filename']]
    my_filepath = df_lookup_doi_path_to_file.iloc[0, 0] + df_lookup_doi_filename.iloc[0, 0]
    
    prepared_output = {"folder": secrets["doipdf_pdfs_folder"], "filepath": my_filepath}
    
    return prepared_output
  else:
    # Handle the case when no matching DOI is found
    raise ValueError(f"No match found for DOI: {given_doi}")
