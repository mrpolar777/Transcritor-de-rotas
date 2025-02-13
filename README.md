# Transcrição de Rotas com Nomes de Ruas

Esta aplicação permite que você faça o upload de um arquivo KML contendo coordenadas geográficas e, em seguida, gera um PDF com os nomes das ruas correspondentes a essas coordenadas. A aplicação utiliza a API do OpenRoute Service para obter os nomes das ruas a partir das coordenadas fornecidas.

## Funcionalidades

- **Upload de arquivo KML**: Faça o upload de um arquivo KML contendo as coordenadas geográficas.
- **Extração de coordenadas**: As coordenadas são extraídas do arquivo KML.
- **Obtenção de nomes de ruas**: As coordenadas são usadas para obter os nomes das ruas correspondentes através da API do OpenRoute Service.
- **Geração de PDF**: Um PDF é gerado contendo os nomes das ruas encontradas.
- **Download do PDF**: O PDF gerado pode ser baixado diretamente da aplicação.

## Como usar

1. **Faça o upload do arquivo KML**:
   - Clique no botão "Faça o upload do arquivo KML" e selecione o arquivo KML que contém as coordenadas geográficas.

2. **Processamento das coordenadas**:
   - A aplicação irá extrair as coordenadas do arquivo KML e, em seguida, obter os nomes das ruas correspondentes usando a API do OpenRoute Service. Uma barra de progresso mostrará o andamento do processamento.

3. **Geração e download do PDF**:
   - Após o processamento, se nomes de ruas forem encontrados, um PDF será gerado e um botão de download será disponibilizado. Clique em "Baixar PDF" para baixar o arquivo.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `streamlit`
  - `requests`
  - `fpdf`
  - `xml.etree.ElementTree`

## Instalação

1. Clone o repositório ou baixe o código-fonte da aplicação.

2. Instale as dependências necessárias:

   ```bash
   pip install streamlit requests fpdf
   ```

3. Execute a aplicação:

   ```bash
   streamlit run nome_do_arquivo.py
   ```

4. A aplicação será aberta no seu navegador padrão.

## Configuração

- **API Key**: A aplicação utiliza a API do OpenRoute Service, que requer uma chave de API. A chave de API está configurada no código como `API_KEY`. Certifique-se de que a chave de API está correta e válida.

## Exemplo de arquivo KML

Um arquivo KML válido deve conter coordenadas geográficas no formato correto. Aqui está um exemplo simples de como um arquivo KML pode ser estruturado:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <Placemark>
      <name>Exemplo de Coordenada</name>
      <Point>
        <coordinates>-46.633308,-23.550520</coordinates>
      </Point>
    </Placemark>
  </Document>
</kml>
```

## Limitações

- A precisão dos nomes das ruas depende da qualidade dos dados fornecidos pela API do OpenRoute Service.
- A aplicação atualmente suporta apenas arquivos KML com coordenadas em pontos (`<Point>`).

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar a aplicação.

---

**Nota**: Certifique-se de que você tem uma conexão com a internet ao usar esta aplicação, pois ela depende da API do OpenRoute Service para obter os nomes das ruas.
