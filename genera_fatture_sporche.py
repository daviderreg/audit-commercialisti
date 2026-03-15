import pandas as pd
from openpyxl import Workbook

# Create test data with "dirty" formats
data = {
    'Numero Fattura': ['F001', 'F002', 'F003', 'F004', 'F005', 'F006', 'F007', 'F008', '', 'F009'],
    'Fornitore': ['Acme Srl', 'Beta SpA', '', 'Gamma Srl', 'Delta Srl', '', 'Epsilon Srl', 'Zeta Srl', '', 'Eta Srl'],
    'Importo': ['1.200,50', '€ 850,00', '100,50', '€2.500', '', '350,00 €', '1.000', '€ 125,50 ', '', '999,99'],
    'Data': ['15/01/2024', '2024-01-20', '20/01/2024', '25.01.2024', '', '2024/01/28', '30/01/2024', '01-02-2024', '', '10 feb 2024'],
    'Note': ['Regular', 'With euro symbol', 'Italian format', 'Dot separator', 'Empty row', 'Euro after', 'No cents', 'Spaces', 'Empty', 'Text date']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('fatture_sporche.xlsx', index=False, sheet_name='Fatture')

print("✅ File 'fatture_sporche.xlsx' generato con successo!")
print("\nContenuto del file:")
print(df.to_string())
print("\nIl file include:")
print("- Importi con virgola decimale italiana (1.200,50)")
print("- Importi con simbolo € (€ 850,00)")
print("- Importi con € attaccato (€2.500)")
print("- Importi con € dopo il numero (350,00 €)")
print("- Righe completamente vuote")
print("- Date in vari formati (italiano, ISO, europeo con punto, testo)")