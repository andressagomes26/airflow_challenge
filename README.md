# Tutorial Airflow | Desafio Módulo 5

Neste repositório está sendo desenvolvido o desafio módulo 5 referente ao conteúdo "Orquestração ocm Airflow". 

## Instruções

Para utilizar este projeto deve-se clonar o repositório do github e executar os comando dentro da pasta do projeto. 

Ativar o ambiente virtual
```bash
source venv/bin/activate
```

Instalar as dependências
```bash
pip install -r requiremenst.txt
```

Configurar o ambiente de acordo com o local dos arquivos de config do airflow
```bash
export AIRFLOW_HOME=./airflow-data
```

Resetar o db do airflow 
```bash
airflow db reset
```

Start airflow
```bash
airflow standalone
```

## Arquivos
- Dags: *./airflow-data/dags/example_desafio.py*
- Banco de dados: *./airlow-data/data/Northwind_small.sqlite*
- Arquivo final: *./airlow-data/data/output_orders.csv*
- Arquivo gerado automaticamente pela task (final_output): *final_output.txt*
