import json
from constant import *
from pyqldb.driver.pooled_qldb_driver import PooledQldbDriver
from logging import basicConfig, getLogger, INFO
import amazon.ion.simpleion as ion
#from amazon.ion.simpleion import dumps, loads

class QLDBDriver():
    def __init__(self, ledger_name=LEDGER_NAME, region_name=REGION, endpoint_url=None, boto3_session=None,
                 aws_access_key_id=ACCESSID, aws_secret_access_key=ACCESSSECRETKEY):

        self.bd = PooledQldbDriver(ledger_name=ledger_name, region_name=region_name, endpoint_url=endpoint_url,
                                   boto3_session=boto3_session, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        self.logger = getLogger()

        self.logger.info('Instanciando driver')

    def create_qldb_session(self):

        self.logger.info('Creando session')
        qldb_session = self.bd.get_session()
        return qldb_session

    def execute_query(self, executor, query):

        self.logger.info('Ejecutando query {}...'.format(query))
        return executor.execute_statement(query)

    def execute_insert(self, executor, table, data):
        data_json = json.dumps(data).replace("\"", "'").replace("[","").replace("]", "")
        query = "INSERT INTO {} << {} >>".format(table, data_json)
        self.logger.info('Ejecutando Insert {}...'.format(query))
        return executor.execute_statement(query)

    def create_insert(self, table, data):
        try:
            with self.create_qldb_session() as session:
                query_lambda = lambda executor: self.execute_insert(executor, table, data)
                query_retry = lambda retry_attempt: self.logger.info('Existen conflictos con este insert, intento: {}'.format(retry_attempt))
                return session.execute_lambda(query_lambda, query_retry)
        except Exception:
            self.logger.exception('Error en query, tabla: {}'.format(table))
        
        return None

    def create_query(self, query):
        try:
            with self.create_qldb_session() as session:
                query_lambda = lambda executor: self.execute_query(executor, query)
                query_retry = lambda retry_attempt: self.logger.info('Existen conflictos con este query, intento: {}'.format(retry_attempt))
                cursor = session.execute_lambda(query_lambda, query_retry)
                rows = []
                for row in cursor:
                    r = ion.dumps(row, binary=False, omit_version_marker=True)
                    r = ion.loads(r)
                    rows.append(dict(r))
                return rows
        except Exception:
            self.logger.exception('Error en query: {}'.format(query))
        
        return None