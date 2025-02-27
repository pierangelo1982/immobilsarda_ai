CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE immobili (
    id SERIAL PRIMARY KEY,
    tipo_immobile VARCHAR(255),
    codice_dam VARCHAR(50),
    localita VARCHAR(255),
    nome_immobile VARCHAR(255),
    comune VARCHAR(255),
    indirizzo TEXT,
    descrizione TEXT,
    categoria VARCHAR(255),
    prezzo_vendita DECIMAL(12,2),
    prezzo_affitto DECIMAL(12,2),
    mq_commerciali INT,
    mq_interni INT,
    num_van_locali INT,
    num_van_catastali INT,
    num_camere INT,
    num_bagni INT,
    num_corpi INT,
    num_posti_auto INT,
    num_box INT,
    have_piscina BOOLEAN,
    have_giardino BOOLEAN,
    mq_giardino INT,
    have_terrazze BOOLEAN,
    have_posto_auto BOOLEAN,
    mq_terreno INT,
    is_complesso BOOLEAN,
    codice_crm VARCHAR(255),
    nome_fittizio VARCHAR(255),
    note TEXT,
    embeddings vector(1536)  -- Store embeddings as a vector (adjust the dimension as needed)
);
