from airflow.utils.edgemodifier import Label
from datetime import datetime, timedelta
from textwrap import dedent
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.models import Variable
import sqlite3
import pandas as pd

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


## Do not change the code below this line ---------------------!!#
def export_final_answer():
    import base64

    # Import count
    with open('count.txt') as f:
        count = f.readlines()[0]

    my_email = Variable.get("my_email")
    message = my_email+count
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    with open("final_output.txt","w") as f:
        f.write(base64_message)
    return None
## Do not change the code above this line-----------------------##

def reads_data_table_order():
    conn = sqlite3.connect("/home/andressa/andressa/lh/airflow_challenge/data/Northwind_small.sqlite")
    select_sql = "SELECT * FROM 'Order';"
    df = pd.read_sql_query(select_sql, conn)
    df.to_csv('/home/andressa/andressa/lh/airflow_challenge/data/output_orders.csv', index=False)
    conn.close

def reads_data_table_orderDetail():
    conn = sqlite3.connect("/home/andressa/andressa/lh/airflow_challenge/data/Northwind_small.sqlite")
    select_sql = "SELECT * FROM 'OrderDetail';"

    df_Order = pd.read_csv('/home/andressa/andressa/lh/airflow_challenge/data/output_orders.csv', sep=',')
    df_OrderDetail = pd.read_sql_query(select_sql, conn)
    
    result = df_Order.merge(df_OrderDetail, left_on='Id', right_on='OrderId', how='left')
    df1 = result.loc[result['ShipCity'] == 'Rio de Janeiro']

    soma = str(df1['Quantity'].sum())

    with open("count.txt","w") as arq:
        arq.write(soma)

    conn.close

with DAG(
    'DesafioAirflow',
    default_args=default_args,
    description='Desafio de Airflow da Indicium',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:
    dag.doc_md = """
        Esse é o desafio de Airflow da Indicium.
    """
   
    export_final_output = PythonOperator(
        task_id='export_final_output',
        python_callable=export_final_answer,
        provide_context=True
    )

    export_table_order = PythonOperator(
        task_id='export_table_order',
        python_callable=reads_data_table_order,
        provide_context=True
    )

    export_table_order_detail = PythonOperator(
        task_id='export_table_order_detail',
        python_callable=reads_data_table_orderDetail,
        provide_context=True
    )

    export_table_order >> export_table_order_detail >> export_final_output