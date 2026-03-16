import streamlit as st
import pandas as pd
from io import BytesIO
import re
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Confronto Fatture ed Estratto Conto",
    page_icon="📊",
    layout="wide",
    menu_items=None
)

# Hide Streamlit branding with custom CSS + JavaScript - ULTIMATE aggressive
st.markdown("""
<style>
    /* Hide ALL elements at bottom of page - footer area */
    [data-testid="stBottom"] {display: none !important; visibility: hidden !important; height: 0 !important;}
    .stBottom {display: none !important; visibility: hidden !important; height: 0 !important;}
    
    /* Hide footer by all possible selectors */
    footer {display: none !important; visibility: hidden !important; height: 0 !important;}
    [data-testid="stFooter"] {display: none !important; visibility: hidden !important; height: 0 !important;}
    [data-testid="stFooterContainer"] {display: none !important; visibility: hidden !important; height: 0 !important;}
    [data-testid="stFooterContent"] {display: none !important; visibility: hidden !important; height: 0 !important;}
    [data-testid="stFooterSection"] {display: none !important; visibility: hidden !important; height: 0 !important;}
    .stFooter {display: none !important; visibility: hidden !important; height: 0 !important;}
    .stFooterContainer {display: none !important; visibility: hidden !important; height: 0 !important;}
    .stFooterContent {display: none !important; visibility: hidden !important; height: 0 !important;}
    
    /* Hide bottom bar */
    [data-testid="stBottomBar"] {display: none !important;}
    .stBottomBar {display: none !important;}
    [data-testid="stBottomSection"] {display: none !important;}
    
    /* Hide Streamlit Cloud specific elements */
    [class*="StreamlitCloud"] {display: none !important;}
    [class*="streamlit-cloud"] {display: none !important;}
    [class*="StyledAppFooter"] {display: none !important;}
    [class*="AppFooter"] {display: none !important;}
    [class*="Footer-"] {display: none !important;}
    [class*="footer-"] {display: none !important;}
    
    /* Hide by aria-label and title */
    [aria-label*="hosted"] {display: none !important;}
    [aria-label*="created"] {display: none !important;}
    [aria-label*="Hosted"] {display: none !important;}
    [aria-label*="Created"] {display: none !important;}
    [title*="hosted"] {display: none !important;}
    [title*="created"] {display: none !important;}
    [title*="Hosted"] {display: none !important;}
    [title*="Created"] {display: none !important;}
    
    /* Hide main menu and three dots */
    #MainMenu {visibility: hidden !important; display: none !important;}
    [data-testid="stMainMenu"] {visibility: hidden !important; display: none !important;}
    button[aria-label="Main menu"] {display: none !important;}
    button[aria-label="main menu"] {display: none !important;}
    [title="Main menu"] {display: none !important;}
    
    /* Hide header toolbar */
    header {visibility: hidden !important; display: none !important;}
    [data-testid="stHeader"] {visibility: hidden !important; display: none !important;}
    [data-testid="stToolbar"] {visibility: hidden !important; display: none !important;}
    
    /* Hide deploy button */
    .stDeployButton {display: none !important;}
    [data-testid="stDeployButton"] {display: none !important;}
    
    /* Hide sidebar */
    [data-testid="stSidebar"] {display: none !important;}
    [data-testid="stSidebarUserContent"] {display: none !important;}
    
    /* Remove padding at bottom */
    [data-testid="stVerticalBlock"] > div:last-child {
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
    }
    [data-testid="stMainBlockContainer"] {
        padding-bottom: 0 !important;
    }
    
    /* Nuclear: hide any div with footer-like class names */
    div[class*="Footer"] {display: none !important;}
    div[class*="footer"] {display: none !important;}
    div[class*="Bottom"] {display: none !important;}
    div[class*="bottom"] {display: none !important;}
    
    /* EXTREME: Hide Streamlit Cloud avatar image */
    [class*="_profileImage"] {display: none !important; visibility: hidden !important;}
    img[alt="App Creator Avatar"] {display: none !important; visibility: hidden !important;}
    img[data-testid="appCreatorAvatar"] {display: none !important; visibility: hidden !important;}
    
    /* Hide Streamlit logo SVG */
    svg[data-testid="streamlitLogo"] {display: none !important; visibility: hidden !important;}
    [class*="StreamlitLogo"] {display: none !important; visibility: hidden !important;}
    
    /* Hide the entire footer container by all known selectors */
    [class*="StyledAppView"] footer {display: none !important;}
    [class*="AppView"] [class*="Footer"] {display: none !important;}
    
    /* Hide by data-testid patterns */
    [data-testid^="st-"] {display: none !important;}
    [data-testid*="footer"] {display: none !important;}
    [data-testid*="bottom"] {display: none !important;}
    
    /* Hide elements with specific class patterns from Streamlit Cloud */
    [class^="_"] [class*="Footer"] {display: none !important;}
    [class^="_"] [class*="footer"] {display: none !important;}
    [class^="_"] [class*="Bottom"] {display: none !important;}
    [class^="_"] [class*="bottom"] {display: none !important;}
    
    /* Hide any SVG in footer area */
    footer svg {display: none !important;}
    [class*="Footer"] svg {display: none !important;}
    [class*="Bottom"] svg {display: none !important;}
    
    /* Hide image elements in footer */
    footer img {display: none !important;}
    [class*="Footer"] img {display: none !important;}
    [class*="Bottom"] img {display: none !important;}
</style>

<script>
(function() {
    function hideBranding() {
        // Get ALL elements
        var allElements = document.querySelectorAll('*');
        
        allElements.forEach(function(el) {
            var text = el.textContent || '';
            var textLower = text.toLowerCase();
            var attrValue = el.getAttribute('aria-label') || '';
            var titleValue = el.getAttribute('title') || '';
            var className = el.className || '';
            
            // Check for branding text
            if (textLower.includes('hosted by') || textLower.includes('created by') || 
                textLower.includes('hosted') || textLower.includes('created') ||
                textLower.includes('streamlit') || textLower.includes('daviderreg')) {
                // Nuke the element and all parents
                var current = el;
                while (current && current !== document.body && current !== document.documentElement) {
                    current.style.display = 'none';
                    current.style.visibility = 'hidden';
                    current.style.opacity = '0';
                    current.style.height = '0';
                    current.style.width = '0';
                    current.style.overflow = 'hidden';
                    current.style.position = 'absolute';
                    current = current.parentElement;
                }
            }
            
            // Check attributes
            if (attrValue.toLowerCase().includes('hosted') || attrValue.toLowerCase().includes('created') ||
                titleValue.toLowerCase().includes('hosted') || titleValue.toLowerCase().includes('created') ||
                className.toLowerCase().includes('footer') || className.toLowerCase().includes('bottom')) {
                el.style.display = 'none';
                el.style.visibility = 'hidden';
                el.style.opacity = '0';
                el.style.height = '0';
                el.style.width = '0';
            }
            
            // Hide menu buttons
            if (el.tagName === 'BUTTON') {
                if (attrValue.toLowerCase().includes('menu') || titleValue.toLowerCase().includes('menu')) {
                    el.style.display = 'none';
                }
            }
        });
        
        // Also hide by specific selectors
        var selectors = [
            '[data-testid="stFooter"]',
            '[data-testid="stFooterContainer"]',
            '[data-testid="stFooterContent"]',
            '[data-testid="stFooterSection"]',
            '[data-testid="stBottom"]',
            '[data-testid="stBottomBar"]',
            '[data-testid="stBottomSection"]',
            '.stFooter',
            '.stFooterContainer',
            '.stFooterContent',
            '.stBottomBar',
            'footer',
            '#MainMenu',
            '[data-testid="stMainMenu"]',
            '[data-testid="stDeployButton"]',
            '[aria-label*="hosted"]',
            '[aria-label*="created"]',
            '[title*="hosted"]',
            '[title*="created"]'
        ];
        
        selectors.forEach(function(sel) {
            try {
                var els = document.querySelectorAll(sel);
                els.forEach(function(e) {
                    e.style.display = 'none';
                    e.style.visibility = 'hidden';
                    e.style.opacity = '0';
                    e.style.height = '0';
                    e.style.width = '0';
                });
            } catch(err) {}
        });
        
        // Hide Streamlit Cloud footer specifically
        var appView = document.querySelector('[class*="StyledAppView"]');
        if (appView) {
            var footerElements = appView.querySelectorAll('footer, [class*="Footer"], [class*="footer"]');
            footerElements.forEach(function(e) {
                e.style.display = 'none';
                e.style.visibility = 'hidden';
            });
        }
    }
    
    // Run immediately
    hideBranding();
    
    // Run frequently
    setInterval(hideBranding, 50);
    
    // Watch for changes
    var observer = new MutationObserver(function(mutations) {
        hideBranding();
    });
    observer.observe(document.body, { 
        childList: true, 
        subtree: true, 
        attributes: true, 
        characterData: true,
        attributeOldValue: true,
        characterDataOldValue: true
    });
    
    // Run on DOMContentLoaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', hideBranding);
    }
})();
</script>
""", unsafe_allow_html=True)

# GDPR Header
st.markdown("""
<div style='background-color: #e8f4f8; padding: 15px; border-radius: 10px; margin-bottom: 20px; border-left: 4px solid #1f77b4;'>
    <h4 style='margin: 0; color: #1f77b4;'>🔒 Privacy & Sicurezza Dati</h4>
    <p style='margin: 5px 0 0 0; color: #555;'>I dati caricati vengono elaborati localmente e <strong>non vengono salvati</strong> su nessun server. Tutte le operazioni sono eseguite nel browser.</p>
</div>
""", unsafe_allow_html=True)

# Main title
st.title("📊 Confronto Fatture Fornitori - Estratto Conto")
st.markdown("""
<div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
    <strong>📋 Istruzioni:</strong>
    <ol style='margin: 5px 0;'>
        <li>Carica i due file Excel (Fatture Fornitori e Estratto Conto)</li>
        <li>Seleziona le colonne contenenti Importo e Data per ciascun file</li>
        <li>Clicca su "Analizza Discrepanze" per confrontare i dati</li>
        <li>Scarica il report degli errori in formato Excel</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'discrepanze' not in st.session_state:
    st.session_state.discrepanze = None
if 'analisi_completata' not in st.session_state:
    st.session_state.analisi_completata = False


def parse_amount(value):
    """
    Converte un valore in formato numerico pulito.
    Gestisce: virgole decimali (1.200,50), simbolo €, spazi, valori vuoti.
    """
    if value is None or pd.isna(value):
        return 0.0
    
    # Convert to string if not already
    str_val = str(value).strip()
    
    # Remove euro symbol and spaces
    str_val = str_val.replace('€', '').replace(' ', '').replace('\xa0', '')
    
    # Handle empty string
    if not str_val:
        return 0.0
    
    # Handle Italian number format (1.200,50 -> 1200.50)
    if ',' in str_val:
        str_val = str_val.replace('.', '')  # Remove thousands separator
        str_val = str_val.replace(',', '.')  # Convert decimal comma to dot
    
    try:
        return float(str_val)
    except ValueError:
        return 0.0


def parse_date(value):
    """
    Converte qualsiasi formato data in standard ISO (YYYY-MM-DD).
    """
    if value is None or pd.isna(value):
        return None
    
    if isinstance(value, (datetime, pd.Timestamp)):
        return pd.Timestamp(value)
    
    str_val = str(value).strip()
    
    if not str_val:
        return None
    
    date_formats = [
        '%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y', '%m/%d/%Y', '%m-%d-%Y',
        '%Y/%m/%d', '%d.%m.%Y', '%Y%m%d', '%d %b %Y', '%d %B %Y',
        '%b %d, %Y', '%B %d, %Y',
    ]
    
    for fmt in date_formats:
        try:
            return pd.Timestamp(datetime.strptime(str_val, fmt))
        except ValueError:
            continue
    
    try:
        return pd.to_datetime(str_val, errors='coerce')
    except:
        return None


def load_excel_robust(file_obj):
    """
    Carica file Excel in modo robusto:
    - Salta righe vuote all'inizio
    - Legge il primo foglio utile con dati
    """
    try:
        excel_file = pd.ExcelFile(file_obj, engine='openpyxl')
        sheet_name = excel_file.sheet_names[0]
        df = pd.read_excel(file_obj, sheet_name=sheet_name, engine='openpyxl')
        
        # Remove completely empty rows and columns
        df = df.dropna(how='all')
        df = df.dropna(axis=1, how='all')
        
        return df
    
    except Exception as e:
        st.error(f"Errore nella lettura del file Excel: {str(e)}")
        return None


# File upload section
col1, col2 = st.columns(2)

with col1:
    st.subheader("📁 Fatture Fornitori")
    fatture_file = st.file_uploader(
        "Carica file Excel",
        type=["xlsx", "xls"],
        key="fatture",
        help="Seleziona il file Excel contenente le fatture dei fornitori"
    )

with col2:
    st.subheader("📁 Estratto Conto")
    estratto_file = st.file_uploader(
        "Carica file Excel",
        type=["xlsx", "xls"],
        key="estratto",
        help="Seleziona il file Excel contenente l'estratto conto"
    )

# Process files when both are uploaded
if fatture_file and estratto_file:
    df_fatture = load_excel_robust(fatture_file)
    df_estratto = load_excel_robust(estratto_file)
    
    if df_fatture is not None and df_estratto is not None:
        st.success(f"✅ File caricati: {len(df_fatture)} righe (Fatture), {len(df_estratto)} righe (Estratto)")
        
        # Preview data
        with st.expander("👁️ Anteprima dati"):
            col_p1, col_p2 = st.columns(2)
            with col_p1:
                st.write("**Fatture Fornitori**")
                st.dataframe(df_fatture.head(5))
            with col_p2:
                st.write("**Estratto Conto**")
                st.dataframe(df_estratto.head(5))
        
        # Column selection section
        st.subheader("⚙️ Configurazione Colonne")
        
        col_sel1, col_sel2 = st.columns(2)
        
        with col_sel1:
            st.markdown("**Fatture Fornitori**")
            # Auto-detect columns
            all_columns = df_fatture.columns.tolist()
            
            # Try to auto-detect importo column
            importo_candidates = [c for c in all_columns if 'importo' in str(c).lower() or 'amount' in str(c).lower() or 'totale' in str(c).lower() or 'valore' in str(c).lower()]
            data_candidates = [c for c in all_columns if 'data' in str(c).lower() or 'date' in str(c).lower() or 'tempo' in str(c).lower()]
            
            ff_importo = st.selectbox(
                "Colonna Importo",
                all_columns,
                index=0 if not importo_candidates else (all_columns.index(importo_candidates[0]) if importo_candidates[0] in all_columns else 0),
                key="ff_importo"
            )
            ff_data = st.selectbox(
                "Colonna Data",
                all_columns,
                index=0 if not data_candidates else (all_columns.index(data_candidates[0]) if data_candidates[0] in all_columns else 0),
                key="ff_data"
            )
        
        with col_sel2:
            st.markdown("**Estratto Conto**")
            all_columns_ec = df_estratto.columns.tolist()
            
            importo_candidates_ec = [c for c in all_columns_ec if 'importo' in str(c).lower() or 'amount' in str(c).lower() or 'totale' in str(c).lower() or 'valore' in str(c).lower()]
            data_candidates_ec = [c for c in all_columns_ec if 'data' in str(c).lower() or 'date' in str(c).lower() or 'tempo' in str(c).lower() or 'operazione' in str(c).lower()]
            
            ec_importo = st.selectbox(
                "Colonna Importo",
                all_columns_ec,
                index=0 if not importo_candidates_ec else (all_columns_ec.index(importo_candidates_ec[0]) if importo_candidates_ec[0] in all_columns_ec else 0),
                key="ec_importo"
            )
            ec_data = st.selectbox(
                "Colonna Data",
                all_columns_ec,
                index=0 if not data_candidates_ec else (all_columns_ec.index(data_candidates_ec[0]) if data_candidates_ec[0] in all_columns_ec else 0),
                key="ec_data"
            )
        
        # Analysis button
        if st.button("🔍 Analizza Discrepanze", type="primary", use_container_width=True):
            with st.spinner("Analisi in corso..."):
                # Prepare cleaned data
                discrepanze_list = []
                
                # Process Fatture data
                fatture_processed = []
                for idx, row in df_fatture.iterrows():
                    importo = parse_amount(row[ff_importo])
                    data_val = parse_date(row[ff_data])
                    if data_val is not None or importo != 0:
                        fatture_processed.append({
                            'importo': importo,
                            'data': data_val,
                            'row_idx': idx,
                            'original_data': row.to_dict()
                        })
                
                # Process Estratto data
                estratto_processed = []
                for idx, row in df_estratto.iterrows():
                    importo = parse_amount(row[ec_importo])
                    data_val = parse_date(row[ec_data])
                    if data_val is not None or importo != 0:
                        estratto_processed.append({
                            'importo': importo,
                            'data': data_val,
                            'row_idx': idx,
                            'original_data': row.to_dict()
                        })
                
                # Find discrepancies
                matched_estratto_indices = set()
                
                for fatt in fatture_processed:
                    if fatt['data'] is None:
                        continue
                    
                    # Find matching records in estratto (within 7 days)
                    best_match = None
                    best_diff = float('inf')
                    
                    for i, est in enumerate(estratto_processed):
                        if i in matched_estratto_indices:
                            continue
                        if est['data'] is None:
                            continue
                        
                        date_diff = abs((fatt['data'] - est['data']).days)
                        if date_diff <= 7:
                            amount_diff = abs(fatt['importo'] - est['importo'])
                            if amount_diff < best_diff:
                                best_diff = amount_diff
                                best_match = (i, est)
                    
                    if best_match is None:
                        # No matching record found
                        discrepanze_list.append({
                            'Tipo Discrepanza': 'Record Mancante',
                            'File Origine': 'Fatture Fornitori',
                            'Importo': fatt['importo'],
                            'Data': fatt['data'].strftime('%Y-%m-%d') if fatt['data'] else 'N/A',
                            'Note': 'Nessun corrispettivo trovato in Estratto Conto'
                        })
                    else:
                        matched_idx, est_match = best_match
                        amount_difference = abs(fatt['importo'] - est_match['importo'])
                        
                        if amount_difference > 0.02:
                            discrepanze_list.append({
                                'Tipo Discrepanza': 'Differenza Importo',
                                'File Origine': 'Fatture vs Estratto',
                                'Importo Fatture': fatt['importo'],
                                'Importo Estratto': est_match['importo'],
                                'Data Fatture': fatt['data'].strftime('%Y-%m-%d') if fatt['data'] else 'N/A',
                                'Data Estratto': est_match['data'].strftime('%Y-%m-%d') if est_match['data'] else 'N/A',
                                'Differenza': round(amount_difference, 2),
                                'Note': 'Importi non corrispondenti'
                            })
                        elif amount_difference > 0:
                            discrepanze_list.append({
                                'Tipo Discrepanza': 'Arrotondamento',
                                'File Origine': 'Fatture vs Estratto',
                                'Importo Fatture': fatt['importo'],
                                'Importo Estratto': est_match['importo'],
                                'Data Fatture': fatt['data'].strftime('%Y-%m-%d') if fatt['data'] else 'N/A',
                                'Data Estratto': est_match['data'].strftime('%Y-%m-%d') if est_match['data'] else 'N/A',
                                'Differenza': round(amount_difference, 4),
                                'Note': 'Differenza minima (< 0.02€) - probabile arrotondamento'
                            })
                        
                        matched_estratto_indices.add(matched_idx)
                
                # Check for unmatched estratto records (missing in fatture)
                for i, est in enumerate(estratto_processed):
                    if i not in matched_estratto_indices and est['data'] is not None:
                        discrepanze_list.append({
                            'Tipo Discrepanza': 'Record Mancante',
                            'File Origine': 'Estratto Conto',
                            'Importo': est['importo'],
                            'Data': est['data'].strftime('%Y-%m-%d') if est['data'] else 'N/A',
                            'Note': 'Presente in Estratto ma non in Fatture'
                        })
                
                # Store results
                if discrepanze_list:
                    st.session_state.discrepanze = pd.DataFrame(discrepanze_list)
                else:
                    st.session_state.discrepanze = pd.DataFrame()
                
                st.session_state.analisi_completata = True
        
        # Display results
        if st.session_state.analisi_completata:
            if st.session_state.discrepanze is not None and len(st.session_state.discrepanze) > 0:
                st.success("✅ Analisi completata!")
                st.subheader(f"📊 Discrepanze trovate: {len(st.session_state.discrepanze)}")
                
                # Color code by type
                def color_discrepanza(val):
                    if val == 'Record Mancante':
                        return 'background-color: #ffcccc'
                    elif val == 'Differenza Importo':
                        return 'background-color: #ffeb3b'
                    elif val == 'Arrotondamento':
                        return 'background-color: #c8e6c9'
                    return ''
                
                styled_df = st.session_state.discrepanze.style.applymap(color_discrepanza, subset=['Tipo Discrepanza'])
                st.dataframe(styled_df, use_container_width=True)
                
                # Summary stats
                col_sum1, col_sum2, col_sum3 = st.columns(3)
                with col_sum1:
                    n_mancanti = len(st.session_state.discrepanze[st.session_state.discrepanze['Tipo Discrepanza'] == 'Record Mancante'])
                    st.metric("Record Mancanti", n_mancanti)
                with col_sum2:
                    n_differenze = len(st.session_state.discrepanze[st.session_state.discrepanze['Tipo Discrepanza'] == 'Differenza Importo'])
                    st.metric("Differenze Importo", n_differenze)
                with col_sum3:
                    n_arrotond = len(st.session_state.discrepanze[st.session_state.discrepanze['Tipo Discrepanza'] == 'Arrotondamento'])
                    st.metric("Arrotondamenti", n_arrotond)
                
                # Download button
                output = BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    st.session_state.discrepanze.to_excel(writer, index=False, sheet_name='Discrepanze')
                    # Add summary sheet
                    summary_df = pd.DataFrame({
                        'Metrica': ['Totale Discrepanze', 'Record Mancanti', 'Differenze Importo', 'Arrotondamenti'],
                        'Valore': [
                            len(st.session_state.discrepanze),
                            n_mancanti,
                            n_differenze,
                            n_arrotond
                        ]
                    })
                    summary_df.to_excel(writer, index=False, sheet_name='Riepilogo')
                
                st.download_button(
                    label="📥 Scarica Report Errori (Excel)",
                    data=output.getvalue(),
                    file_name="report_discrepanze.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    type="primary",
                    use_container_width=True
                )
            else:
                st.success("🎉 Nessuna discrepanza trovata! I dati corrispondono.")