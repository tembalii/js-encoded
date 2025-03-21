#!/usr/bin/local/python3

import csv
import logging
import os

from app import config as cfg
from client.main import Client

logger = logging.getLogger(cfg.HANDLER_NAME)

TOKEN_URL = 'https://dev.com/auth/realms/glp/protocol/openid-connect/token'

CLIENT_ID = 'testclient'

CLIENT_SECRET = '56789'

BASE_URL = 'https://dev.com'
def gen_api_client(client_id, token_url, username, password):
    client = Client(
        api_url=BASE_URL,
        auth_kwargs={
            'client_id': client_id,
            'auth_url': token_url,
            'username': username,
            'password': password
        }
    )

    client.health_check()

    return client


def read_device_ids(file_path, column_name):
    if not os.path.isfile(file_path):
        raise ValueError('Invalid CSV path')

    ids = []

    with open(file_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            ids.append(row[column_name])

    return ids


if __name__ == '__main__':
    logger.info('SunKing : Device creation')

    username_input = input('\nUsername:')
    password_input = input('\nPassword:')

    client = gen_api_client(CLIENT_ID, TOKEN_URL, username_input, password_input)

    csv_file_path = input('\nCSV file path:')

    device_id_column = input('\nDevice ID column:')

    if not device_id_column:
        raise ValueError("No value provided for Device ID column")

    device_ids = read_device_ids(csv_file_path, device_id_column)

    logger.info('Number of IDs', len(device_ids))

    if len(device_ids) < 1:
        raise ValueError('No paygo IDs found')

    product_code = int(input('\nProduct Code:'))

    batch_number = int(input('\nBatch Number[00-99]:'))

    if not batch_number or batch_number > 99 or batch_number < 0:
        raise ValueError('Invalid batch number. Must be between 00 and 99')

    owner = input('\nOwner[glp]:')

    if not owner:
        raise ValueError('Invalid Owner.')

    encoding_options = ['+0-9+#+space', '1-5']
    encoding = input('\nEncoding [{}] :'.format(', '.join(encoding_options)))

    if encoding not in encoding_options:
        raise ValueError('Invalid encoding. Supported encoding inputs: {}'.format(', '.join(encoding_options)))

    # client.bulk_create_device(device_ids, product_code, batch_number, owner, encoding)
