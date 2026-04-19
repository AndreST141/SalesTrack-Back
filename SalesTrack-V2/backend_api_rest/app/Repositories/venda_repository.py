from config.database import get_db_connection

class VendaRepository:

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.*, c.nome as clienteNome, u.nome as vendedorNome
            FROM Venda v
            LEFT JOIN Cliente c ON v.idCliente = c.idCliente
            JOIN Usuario u ON v.idUsuario = u.idUsuario
            ORDER BY v.dataVenda DESC
            LIMIT 100
        """)
        vendas = cursor.fetchall()
        cursor.close()
        conn.close()
        return vendas

    @staticmethod
    def find_with_itens(id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT v.*, c.nome as clienteNome, u.nome as vendedorNome
            FROM Venda v
            LEFT JOIN Cliente c ON v.idCliente = c.idCliente
            JOIN Usuario u ON v.idUsuario = u.idUsuario
            WHERE v.idVenda = %s
        """, (id,))
        venda = cursor.fetchone()

        if not venda:
            cursor.close()
            conn.close()
            return None

        cursor.execute("""
            SELECT iv.*, p.nome as produtoNome
            FROM ItemVenda iv
            JOIN Produto p ON iv.idProduto = p.idProduto
            WHERE iv.idVenda = %s
        """, (id,))
        venda['itens'] = cursor.fetchall()
        cursor.close()
        conn.close()
        return venda

    @staticmethod
    def create(dados, usuario_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO Venda (idCliente, idUsuario, valorTotal, desconto, valorFinal, formaPagamento, observacoes)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                dados.get('idCliente'),
                usuario_id,
                dados['valorTotal'],
                dados.get('desconto', 0),
                dados['valorFinal'],
                dados['formaPagamento'],
                dados.get('observacoes', '')
            ))
            venda_id = cursor.lastrowid

            for item in dados['itens']:
                cursor.execute("""
                    INSERT INTO ItemVenda (idVenda, idProduto, quantidade, precoUnitario, subtotal)
                    VALUES (%s, %s, %s, %s, %s)
                """, (venda_id, item['idProduto'], item['quantidade'], item['precoUnitario'], item['subtotal']))

                cursor.execute("""
                    UPDATE Produto SET estoque = estoque - %s WHERE idProduto = %s
                """, (item['quantidade'], item['idProduto']))

            conn.commit()
            cursor.close()
            conn.close()
            return venda_id
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            raise e
