# 📊 Audit Contabile Professionale - Confronto Fatture ed Estratto Conto

## Descrizione del Tool

Applicazione web professionale per l'**audit contabile** che permette di confrontare automaticamente le **Fatture Fornitori** con l'**Estratto Conto** bancario, identificando discrepanze con precisione al centesimo di euro.

### 🔍 Funzionalità Principali

- **Caricamento Excel**: Importa file Excel (.xlsx, .xls) per Fatture e Estratto Conto
- **Selezione Dinamica Colonne**: Interfaccia intuitiva per mappare le colonne di Importo e Data
- **Pulizia Dati Avanzata**:
  - Gestione formati numerici italiani (1.200,50 → 1200.50)
  - Rimozione automatica simbolo € e spazi
  - Supporto per date in qualsiasi formato (DD/MM/YYYY, ISO, europeo, testuale)
  - Filtro righe vuote o incomplete
- **Algoritmo di Confronto**:
  - Matching temporale entro ±7 giorni
  - Rilevamento differenze importi > 0,02€
  - Classificazione: "Record Mancante", "Differenza Importo", "Arrotondamento"
- **Export Report**: Download Excel con dettaglio discrepanze e foglio riepilogo

---

## 🛡️ Privacy & GDPR Compliance

Questo tool è progettato nel pieno rispetto del **Regolamento GDPR (UE) 2016/679**:

- ✅ **Elaborazione Locale**: Tutti i dati vengono processati esclusivamente nel browser dell'utente
- ✅ **Nessun Salvataggio**: I file caricati non vengono memorizzati su server esterni
- ✅ **Sessione Ephemeral**: I dati esistono solo per la durata della sessione browser
- ✅ **Trasparenza**: Informativa privacy visibile in homepage

---

## 📋 Requisiti di Sistema

### Dipendenze Python
```
streamlit
pandas
openpyxl
xlsxwriter
```

### Pacchetti di Sistema (Linux/Debian)
```
libcap-dev
build-essential
```

---

## 🚀 Installazione e Avvio

### 1. Clonare il Repository
```bash
git clone https://github.com/TUO_USERNAME/audit-commercialisti-salerno.git
cd audit-commercialisti-salerno
```

### 2. Creare Ambiente Virtuale (opzionale ma consigliato)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Installare Dipendenze
```bash
pip install -r requirements.txt
```

### 4. Avviare l'Applicazione
```bash
streamlit run app.py
```

L'interfaccia sarà accessibile a: **http://localhost:8501**

---

## 📁 Struttura File

| File | Descrizione |
|------|-------------|
| `app.py` | Applicazione principale Streamlit |
| `requirements.txt` | Dipendenze Python |
| `packages.txt` | Pacchetti di sistema per deployment |
| `README.md` | Documentazione |

---

## 💼 Casi d'Uso

- **Studi Commercialisti**: Riconciliazione automatica fatture/estratti per clienti
- **Departimenti Finance**: Audit interno su pagamenti fornitori
- **Revisione Contabile**: Verifica integrità dati contabili
- **PMI**: Controllo periodico corrispondenza bancaria

---

## 🎯 Precisione Contabile

Il sistema garantisce:
- **Tolleranza 0,02€** per differenze di arrotondamento
- **Window ±7 giorni** per matching temporale
- **Tracciabilità completa** di ogni discrepanza rilevata

---

## 📞 Supporto

Per informazioni o personalizzazioni, contattare lo sviluppatore.

---

*Tool sviluppato per professionisti dell'audit contabile - Salerno, Italia*