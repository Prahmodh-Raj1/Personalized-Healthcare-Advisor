import pandas as pd

# Load the dataset
file_path = "/content/disease_symptoms.csv"  # Replace with your actual CSV file path
df = pd.read_csv(file_path)

# Separate symptoms and prognosis columns
symptom_columns = df.columns[:-1]  # All columns except the last one (which is 'prognosis')
prognosis_column = df.columns[-1]  # The last column (disease name)

# Dictionary to store the new format
disease_symptoms = {}

# Iterate over each row
for _, row in df.iterrows():
    disease = row[prognosis_column]  # Extract disease name
    symptoms = [symptom for symptom in symptom_columns if row[symptom] == 1]  # Get symptoms with '1'

    # Append symptoms to the disease in dictionary
    if disease in disease_symptoms:
        disease_symptoms[disease].update(symptoms)  # Use a set to avoid duplicates
    else:
        disease_symptoms[disease] = set(symptoms)

# Convert dictionary to a DataFrame
formatted_data = pd.DataFrame({"Disease": disease_symptoms.keys(), 
                               "Symptoms": [", ".join(symptoms) for symptoms in disease_symptoms.values()]})

# Save to CSV
output_file = "formatted_disease_symptoms.csv"
formatted_data.to_csv(output_file, index=False)

print(f"Transformed data saved to {output_file}")
