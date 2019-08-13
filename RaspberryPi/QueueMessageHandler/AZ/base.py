__author__ = "Dillon Goeda"

import AZ.config as config
from azure.storage import CloudStorageAccount


def get_account():
    """Returns a CloudStorageAccount using the configuration in the config.py"""
    account_name = config.STORAGE_ACCOUNT_NAME
    account_key = config.STORAGE_ACCOUNT_KEY
    account = CloudStorageAccount(account_name, account_key)
    return account
