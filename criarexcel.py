import pandas as pd


df_user = pd.DataFrame({
    'id': [1, 2],
    'name': ['Guilherme', 'Maria'],
    'email': ['guilherme@email.com', 'maria@email.com']
})

df_estado = pd.DataFrame({
    'uf': ['SP', 'RJ'],
    'nome': ['São Paulo', 'Rio de Janeiro']
})

df_cidade = pd.DataFrame({
    'id': ['100', '101'],
    'nome': ['São Paulo', 'Rio de Janeiro'],
    'uf': ['SP', 'RJ']
})

df_empresa = pd.DataFrame({
    'id': [1, 2],
    'razao_social': ['Assistência Técnica SP Ltda', 'Assistência RJ Serviços'],
    'nome_fantasia': ['AssistSP', 'AssistRJ'],
    'cep': ['01000-000', '20000-000'],
    'bairro': ['Centro', 'Copacabana'],
    'endereco': ['Rua A, 123', 'Avenida B, 456'],
    'ddd': ['11', '21'],
    'telefone': ['1111-1111', '2222-2222'],
    'classificacao': ['Nível A', 'Autorizada'],
    'cidade_id': ['100', '101']
})

with pd.ExcelWriter('dados_para_importacao.xlsx') as writer:
    df_user.to_excel(writer, sheet_name='user', index=False)
    df_estado.to_excel(writer, sheet_name='estado', index=False)
    df_cidade.to_excel(writer, sheet_name='cidade', index=False)
    df_empresa.to_excel(writer, sheet_name='empresa_assistencia_tecnica', index=False)
