from app.config.database import get_connection

def save_to_db(df):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        for index, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO person (
                    data, qual_o_seu_nome, qual_o_seu_numero, 
                    podemos_confirmar_sua_presenca, mulheres, homens, presente
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    row['data'], row['qual_o_seu_nome'], row['qual_o_seu_numero'],
                    row['podemos_confirmar_sua_presenca'], row['mulheres'], row['homens'],
                    row['presente']
                )
            )
        connection.commit()
        cursor.close()
        connection.close()
        print("Dados inseridos com sucesso no banco de dados.")
    except Exception as e:
        print(f"Erro ao inserir dados no banco de dados: {e}")