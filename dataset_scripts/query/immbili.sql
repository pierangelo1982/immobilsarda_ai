CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS immobili (
    id SERIAL PRIMARY KEY,
    tipo_immobile TEXT,
    codice_dam TEXT,
    localita TEXT,
    nome_immobile TEXT,
    descrizione TEXT,
    categoria TEXT,
    prezzo_vendita NUMERIC,
    prezzo_affitto NUMERIC,
    mq_commerciali NUMERIC,
    mq_interni NUMERIC,
    num_van_locali INTEGER,
    num_camere INTEGER,
    num_bagni INTEGER,
    num_corpi INTEGER,
    num_posti_auto INTEGER,
    num_box INTEGER,
    mq_giardino NUMERIC,
    mq_terreno NUMERIC,
    is_complesso BOOLEAN,
    codice_crm TEXT,
    note TEXT,
    embedding vector(384)  -- adjust dimension to match your SentenceTransformer model
);

