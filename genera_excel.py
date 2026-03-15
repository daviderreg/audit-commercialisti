import pandas as pd
from datetime import datetime, timedelta

# Create fatture.xlsx with columns: 'ID', 'Fornitore', 'Data', 'Importo'
fatture_data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Fornitore': ['Fornitore A', 'Fornitore B', 'Fornitore C', 'Fornitore A', 'Fornitore D',
                  'Fornitore B', 'Fornitore E', 'Fornitore C', 'Fornitore A', 'Fornitore F'],
    'Data': [
        '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19',
        '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24'
    ],
    'Importo': [100.50, 250.00, 175.30, 320.00, 89.90, 450.00, 125.75, 200.00, 550.00, 180.25]
}

df_fatture = pd.DataFrame(fatture_data)
df_fatture.to_excel('fatture.xlsx', index=False)

# Create estratto_conto.xlsx with columns: 'Data Operazione', 'Causale', 'Importo'
# Note: Row 3 (ID=3) has a different amount (175.00 instead of 175.30)
#       Row 9 (ID=9) is missing entirely
estratto_data = {
    'Data Operazione': [
        '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19',
        '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-24'
    ],
    'Causale': ['Fattura 1', 'Fattura 2', 'Fattura 3', 'Fattura 4', 'Fattura 5',
                'Fattura 6', 'Fattura 7', 'Fattura 8', 'Fattura 10'],
    'Importo': [100.00, 250.00, 175.00, 320.00, 89.90, 450.00, 125.75, 200.00, 180.25]
}

df_estratto = pd.DataFrame(estratto_data)
df_estratto.to_excel('estratto_conto.xlsx', index=False)

print("File Excel generati con successo!")
print("- fatture.xlsx: 10 righe")
print("- estratto_conto.xlsx: 9 righe (manca la riga ID=9)")
print("\nDiscrepanze inserite:")
print("1. Riga ID=1: Importo 100.50 (fatture) vs 100.00 (estratto)")
print("2. Riga ID=3: Importo 175.30 (fatture) vs 175.00 (estratto)")
print("3. Riga ID=9: Presente in fatture ma manca in estratto_conto")