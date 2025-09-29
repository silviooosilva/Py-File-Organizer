# Py File Organizer

Organize automaticamente arquivos em pastas baseadas na extensao, mantendo seus diretórios sempre limpos.

## Visao geral
- Detecta a extensao de cada arquivo e move para a pasta correspondente definida em `py_file_organizer/extensions.py`.
- Interface em modo texto usando `console-menu` para facilitar o uso.
- Tratamento de erros basico para diretórios inexistentes ou ja organizados.

## Pre-requisitos
- Python 3.8 ou superior.
- `pip` configurado no PATH.
- Ambiente virtual (opcional, mas recomendado).

## Como configurar o ambiente
```bash
# clone o repositorio
git clone https://github.com/silviooosilva/Py-File-Organizer.git
cd Py-File-Organizer

# (opcional) crie e ative um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# dependencias do aplicativo
pip install -r requirements.txt

# dependencias para desenvolvimento e testes
pip install -r requirements_dev.txt
```

## Como executar o organizador
```bash
python3 -m py_file_organizer.main
```
O programa abre um menu interativo. Escolha `Start App`, cole o caminho absoluto do diretorio que deseja organizar e confirme. As pastas sao criadas conforme o mapeamento definido em `py_file_organizer/extensions.py`.

## Testes e manutencao de qualidade
### Testes unitarios
```bash
python3 -m pytest tests/ -v
```
Ou utilize o atalho com relatorio de cobertura:
```bash
make tests
```

### Testes comportamentais (BDD)
```bash
python3 -m pytest bdd/ -v
```
Ou ainda:
```bash
make bdd
```

### Lint
```bash
flake8 .
```
(O comando `make lint` executa os testes com cobertura e, em seguida, roda o lint.)

## Estrutura do projeto
```
py_file_organizer/
├── main.py            # Interface interativa baseada em console-menu
├── functions.py       # Regras de organizacao de arquivos
├── extensions.py      # Mapeamento de extensoes para pastas
└── __init__.py
```
Os testes unitarios vivem em `tests/` e os cenarios comportamento em `bdd/`. Imagens de demonstracao estao em `demo/`.

## Contribuindo
Sinta-se a vontade para abrir issues ou pull requests. Antes de enviar mudancas, execute os testes (`make tests`) e o lint (`flake8 .`) para garantir que tudo continua funcionando.

## Licenca
Distribuido sob a licenca MIT. Consulte `LICENSE` para mais detalhes.

## Autor
Projeto criado por Silvio Silva.
