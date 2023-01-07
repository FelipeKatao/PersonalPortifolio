SELECT * FROM usuarios JOIN Cargos ON Cargos.Modulo = usuarios.Modulo WHERE usuarios.Modulo = 'VENDAS' ORDER BY Acessos
SELECT * FROM usuarios JOIN Cargos ON Cargos.Modulo = usuarios.Modulo WHERE usuarios.Modulo = 'TODOS' ORDER BY Acessos
SELECT * FROM usuarios JOIN Cargos ON Cargos.Modulo = usuarios.Modulo WHERE usuarios.Modulo = 'ADM' ORDER BY Acessos
SELECT * FROM usuarios JOIN Cargos ON Cargos.Modulo = usuarios.Modulo WHERE usuarios.Modulo = 'PAGAMENTO' ORDER BY Acessos
UPDATE usuarios SET Acessos = 2 WHERE Cargos = 'VENDAS'