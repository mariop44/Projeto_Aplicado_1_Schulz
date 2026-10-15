# ==============================================================================
# UNIDADE CURRICULAR: PROJETO APLICADO I
# EMPRESA PARCEIRA: SCHULZ S.A.
# SCRIPT DE GERAÇÃO AUTOMÁTICA DA DOCUMENTAÇÃO EM MARKDOWN (01_estrutura.md)
# ==============================================================================

conteudo_markdown = """# PROJETO APLICADO I - SCHULZ S.A.
## Entrega 02: Modelagem e Estruturação de Banco de Dados Relacional

**Integrantes:** João Vítor Martins da Silva, Mario Nobre Porto
**Data de Entrega:** 15/10/2026
**Orientadores:** Prof. MSc. Hugo Menezes Barra | Prof. Rodrigo Losina

---

### 1. Contexto e Problematização (Transição de Planilhas para BD)

Na Entrega 01 identificamos que a emissão dos certificados de calibração da **Schulz S.A.**
depende hoje de planilhas Excel manuais e descentralizadas. O técnico exporta o relatório da
máquina de medir por coordenadas, cola os valores em uma planilha de registro, confere a
aprovação linha por linha e só então gera o certificado. Esse modelo apresenta riscos
operacionais que foram comprovados nos próprios arquivos entregues pela empresa:

- **Risco de perda de histórico:** cada calibração vive em um arquivo solto, sem vínculo com as
anteriores do mesmo instrumento, o que impede acompanhar a evolução das medições.
- **Inconsistência e duplicação:** o mesmo técnico, o mesmo padrão e o mesmo setor são digitados
de novo a cada certificado, e nem sempre do mesmo jeito.
- **Falha na segurança e integridade:** a planilha aceita digitação por cima da fórmula, sem
registro de quem alterou o quê.

A migração para um **Banco de Dados Relacional (SQLite)** garante a centralização dos dados, a
integridade referencial e a recuperação rápida das informações exigidas em auditoria.

---

### 2. Divisão do Banco de Dados em Entidades Principais

Para eliminar a redundância e organizar a arquitetura da informação, o banco de dados foi
estruturado nas 3 entidades fundamentais a seguir:

#### 2.1. Entidade 1: TECNICO / SOLICITANTE

- **Função:** armazena os dados cadastrais dos metrologistas e colaboradores responsáveis pelas
medições e calibrações. Nas planilhas da Schulz esse cadastro já existe, com dois metrologistas
registrados na aba de banco de dados.
- **Atributos Previstos:** `id_tecnico` (Chave Primária), `nome_tecnico`, `matricula`, `email`,
`setor`.

#### 2.2. Entidade 2: EQUIPAMENTO

- **Função:** registra os instrumentos e dispositivos submetidos a calibração, identificados
pela tag gravada na peça. É o cadastro que hoje é redigitado a cada certificado emitido.
- **Atributos Previstos:** `id_equipamento` (Chave Primária), `codigo_tag`, `nome_equipamento`,
`fabricante`, `modelo`.

#### 2.3. Entidade 3: MEDICAO / CALIBRACAO

- **Função:** entidade transacional que registra o evento de medição, conectando o técnico ao
equipamento avaliado. Guarda o parâmetro aferido, o valor nominal, os limites de tolerância, o
valor obtido e o parecer automático.
- **Atributos Previstos:** `id_medicao` (Chave Primária), `id_equipamento` (Chave Estrangeira),
`id_tecnico` (Chave Estrangeira), `parametro_medido`, `valor_nominal`, `tolerancia_min`,
`tolerancia_max`, `valor_obtido`, `status_resultado`, `data_medicao`.

---

### 3. Justificativa da Eliminação de Dados Duplicados

A normalização do banco de dados em entidades separadas resolve os principais problemas mapeados
na Fase 01, e cada um deles tem evidência nos arquivos da Schulz:

1. **Atendimento às normas de qualidade:** cada calibração fica permanentemente associada ao
histórico do equipamento e ao técnico responsável, o que hoje não acontece porque o vínculo
existe apenas dentro do arquivo daquele certificado.
2. **Otimização do armazenamento:** técnicos e equipamentos são cadastrados uma única vez, em vez
de repetidos a cada medição registrada.
3. **Integridade referencial:** o banco impede o registro de medições para equipamentos
inexistentes ou por técnicos não cadastrados. Nas planilhas atuais não existe essa trava, e o
resultado aparece nos dados: o certificado emitido traz o solicitante "Usinagem I", um setor que
não existe no cadastro, onde constam "Usinagem" e "Usinagem II". O mesmo ocorre com o padrão,
registrado como 500008 no relatório da máquina e como 500.011 no certificado.

---

### 4. Próximos Passos (Implementação DDL no SQLite)

A partir dessa estrutura conceitual definida, a próxima etapa consiste na criação do script SQL
(`CREATE TABLE`) para materializar o banco de dados `schulz_calibracao.db` via Python, com as
chaves primárias, as chaves estrangeiras e a ativação da integridade referencial.
"""

# Execução da gravação do arquivo .md
nome_arquivo = "01_estrutura.md"

try:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_markdown)

    print("=" * 60)
    print(f"SUCESSO: O arquivo '{nome_arquivo}' foi gerado com sucesso!")
    print("Abra o VS Code, selecione o arquivo e pressione 'Ctrl + Shift + V'")
    print("para visualizar a documentacao formatada.")
    print("=" * 60)

except Exception as e:
    print(f"ERRO ao gerar o arquivo: {e}")
