# 02_dicionario.md — Dicionário de Dados do Sistema

**Unidade Curricular:** Projeto Aplicado I
**Empresa Parceira:** Schulz S.A.
**Tema 02:** Modelagem e Implementação de Banco de Dados (SQLite)
**Professores:** Prof. MSc. Hugo Menezes Barra | Prof. Rodrigo Losina
**Integrantes:** João Vítor Martins da Silva, Mario Nobre Porto
**Data de Entrega:** 15/10/2026

---

## 1. Mapeamento das Tabelas e Campos

### 1.1. Tabela: `tecnico` (Técnicos / Solicitantes)

| Nome do Campo | Tipo (SQLite) | Restrições / Chaves | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_tecnico` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do técnico. |
| `nome_tecnico` | TEXT | NOT NULL | Nome completo do profissional. |
| `matricula` | TEXT | NOT NULL, UNIQUE | Matrícula funcional. Não pode repetir entre técnicos. |
| `email` | TEXT | NOT NULL | E-mail corporativo para contato e notificação. |
| `setor` | TEXT | NOT NULL | Departamento de atuação (Ex: Metrologia). |

### 1.2. Tabela: `equipamento` (Instrumentos e Máquinas)

| Nome do Campo | Tipo (SQLite) | Restrições / Chaves | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_equipamento` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do equipamento. |
| `codigo_tag` | TEXT | NOT NULL, UNIQUE | Código/Tag gravado no instrumento (Ex: 703.1208). |
| `nome_equipamento` | TEXT | NOT NULL | Descrição do equipamento (Ex: Dispositivo de Controle). |
| `fabricante` | TEXT | NOT NULL | Fabricante (Ex: CDM, Usifer). |
| `modelo` | TEXT | NOT NULL | Modelo do instrumento. |

### 1.3. Tabela: `medicao` (Registro das Calibrações / Ensaios)

| Nome do Campo | Tipo (SQLite) | Restrições / Chaves | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_medicao` | INTEGER | PRIMARY KEY AUTOINCREMENT | Identificador único do ensaio. |
| `id_equipamento` | INTEGER | NOT NULL, FOREIGN KEY (equipamento) | Vínculo com o equipamento avaliado. |
| `id_tecnico` | INTEGER | NOT NULL, FOREIGN KEY (tecnico) | Vínculo com o técnico responsável. |
| `parametro_medido` | TEXT | NOT NULL | Variável aferida (Ex: Diâmetro, Planicidade, Posição). |
| `valor_nominal` | REAL | NOT NULL | Valor de referência padrão esperado. |
| `tolerancia_min` | REAL | NOT NULL | Limite inferior aceitável, obtido por Nominal menos o módulo da tolerância negativa. |
| `tolerancia_max` | REAL | NOT NULL | Limite superior aceitável, obtido por Nominal mais o módulo da tolerância positiva. |
| `valor_obtido` | REAL | NOT NULL | Leitura real coletada no ensaio. |
| `status_resultado` | TEXT | NOT NULL, CHECK ('APROVADO', 'REPROVADO') | Parecer técnico automático. É APROVADO quando o valor obtido está entre o limite mínimo e o limite máximo. |
| `data_medicao` | TEXT / DATETIME | DEFAULT CURRENT_TIMESTAMP | Data e hora automática da calibração. |

