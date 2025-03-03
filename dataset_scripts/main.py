from config.database_postgresql import db
from utils.db_utils import test_postgres_connection
from utils.excell_data import read_excell_immobili
from sentence_transformers import SentenceTransformer

# Import the pgvector adapter and register it with our database connection.
from pgvector.psycopg2 import register_vector
register_vector(db)

# Test the connection to Postgres.
test_postgres_connection()

# Read Excel data.
df = read_excell_immobili()
print(df)
head_list = df.columns.values.tolist()
print(head_list)

# Load the embedding model.
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # Lightweight model

# Iterate over rows in the dataframe.
for index, row in df.iterrows():
    id_val = row['id']
    tipo_immobile = row['tipo_immobile']
    codice_dam = str(row['codice_dam'])
    localita = row['localita']
    nome_immobile = row['nome_immobile']
    descrizione = row['descrizione']
    categoria = row['categoria']
    prezzo_vendita = row['prezzo_vendita']
    prezzo_affitto = row['prezzo_affitto']
    mq_commerciali = row['mq_commerciali']
    mq_interni = row['mq_interni']
    num_van_locali = int(row['num_vani_locali'])
    num_camere = row['num_camere']
    num_bagni = row['num_bagni']
    num_corpi = row['num_corpi']
    num_posti_auto = row['num_posti_auto']
    num_box = row['num_box']
    mq_giardino = row['mq_giardino']
    mq_terreno = row['mq_terreno']
    # Directly cast the value to a Python boolean.
    is_complesso = bool(row['is_complesso'])
    # If there's a separate field for codice_crm, adjust accordingly.
    codice_crm = row.get('codice_crm', row['codice_dam'])
    note = row['descrizione']
    
    # Create the text to embed from your row data.
    text_to_embed = (
        f"{id_val} {tipo_immobile} {codice_dam} {localita} {nome_immobile} "
        f"{descrizione} {categoria} {prezzo_vendita} {prezzo_affitto} {mq_commerciali} "
        f"{mq_interni} {num_van_locali} {num_camere} {num_bagni} {num_corpi} "
        f"{num_posti_auto} {num_box} {mq_giardino} {mq_terreno} {is_complesso} {codice_crm} {note}"
    )
    
    # Generate the embedding.
    embedding = embedding_model.encode(text_to_embed).tolist()  # Convert to list
    print(embedding)
    
    # Insert the data into the immobili table, including the embedding vector.
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO immobili (
            tipo_immobile, codice_dam, localita, nome_immobile,
            descrizione, categoria, prezzo_vendita, prezzo_affitto,
            mq_commerciali, mq_interni, num_van_locali, num_camere,
            num_bagni, num_corpi, num_posti_auto, num_box, mq_giardino,
            mq_terreno, is_complesso, codice_crm, note, embedding
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (tipo_immobile, codice_dam, localita, nome_immobile, descrizione,
         categoria, prezzo_vendita, prezzo_affitto, mq_commerciali, mq_interni,
         num_van_locali, num_camere, num_bagni, num_corpi, num_posti_auto,
         num_box, mq_giardino, mq_terreno, is_complesso, codice_crm, note,
         embedding)
    )
    db.commit()
    cursor.close()

    
    

