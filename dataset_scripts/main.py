from config.database_postgresql import db
from utils.db_utils import test_postgres_connection

from utils.excell_data import read_excell_immobili

from sentence_transformers import SentenceTransformer

test_postgres_connection()

df = read_excell_immobili()
print(df)
head_list = df.columns.values.tolist()
print(head_list)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # Lightweight model

for index, row in df.iterrows():
    id = row['id']
    tipo_immobile = row['tipo_immobile']
    codice_dam = row['codice_dam']
    localita = row['localita']
    nome_immobile = row['nome_immobile']
    comune = row['comune']
    indirizzo = row['indirizzo']
    descrizione = row['descrizione']
    categoria = row['categoria']
    prezzo_vendita = row['prezzo_vendita']
    prezzo_affitto = row['prezzo_affitto']
    mq_commerciali = row['mq_commerciali']
    mq_interni = row['mq_interni']
    num_van_locali = row['num_van_locali']
    num_van_catastali = row['num_van_catastali']
    num_camere = row['num_camere']
    num_bagni = row['num_bagni']
    num_corpi = row['num_corpi']
    num_posti_auto = row['num_posti_auto']
    num_box = row['num_box']
    have_piscina = row['have_piscina']
    have_giardino = row['have_giardino']
    mq_giardino = row['mq_giardino']
    have_terrazze = row['have_terrazze']
    have_posto_auto = row['have_posto_auto']
    mq_terreno = row['mq_terreno']
    is_complesso = row['is_complesso']
    codice_crm = row['codice_crm']
    nome_fittizio = row['nome_fittizio']
    note = row['note']
    
    text_to_embed = f"{id} {tipo_immobile} {codice_dam} {localita} {nome_immobile} {comune} {indirizzo} {descrizione} {categoria} {prezzo_vendita} {prezzo_affitto} {mq_commerciali} {mq_interni} {num_van_locali} {num_van_catastali} {num_camere} {num_bagni} {num_corpi} {num_posti_auto} {num_box} {have_piscina} {have_giardino} {mq_giardino} {have_terrazze} {have_posto_auto} {mq_terreno} {is_complesso} {codice_crm} {nome_fittizio} {note}"
    embedding = embedding_model.encode(text_to_embed).tolist()  # Convert to list
    print(embedding)
        
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO immobili (id, tipo_immobile, codice_dam, localita, nome_immobile, comune, indirizzo, descrizione, categoria, prezzo_vendita, prezzo_affitto, mq_commerciali, mq_interni, num_van_locali, num_van_catastali, num_camere, num_bagni, num_corpi, num_posti_auto, num_box, have_piscina, have_giardino, mq_giardino, have_terrazze, have_posto_auto, mq_terreno, is_complesso, codice_crm, nome_fittizio, note, embedding)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, 
        (id, tipo_immobile, codice_dam, localita, nome_immobile, comune, indirizzo, descrizione, categoria, prezzo_vendita, prezzo_affitto, mq_commerciali, mq_interni, num_van_locali, num_van_catastali, num_camere, num_bagni, num_corpi, num_posti_auto, num_box, have_piscina, have_giardino, mq_giardino, have_terrazze, have_posto_auto, mq_terreno, is_complesso, codice_crm, nome_fittizio, note, embedding)
    )
    db.commit()
    
    

