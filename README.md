# <h1 align="center"><font color = #119fbf>Tutorial Airflow | Desafio Módulo 5</font></h1>
Neste repositório está sendo desenvolvido o desafio módulo 5 referente ao conteúdo "Orquestração com Airflow". 

<div align="center"><img src='https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png' style='width: 50%;'></div>

## Instruções

Para utilizar este projeto deve-se clonar o repositório do github e executar os comando dentro da pasta do projeto. 

Criar o ambiente virtual
```bash
pip install virtualenv
```

```bash
virtualenv venv -p python3
```

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

Se necessário realizar a instalação do airflow
```bash
AIRFLOW_VERSION=2.6.0
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
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
- Arquivo contagem da quantidade vendida: *count.txt*
- Arquivo gerado automaticamente pela task (final_output): *final_output.txt*
