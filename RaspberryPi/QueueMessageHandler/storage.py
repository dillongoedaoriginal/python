"""This is a wrapper library for azure blob storage"""
__author__ = "Dillon Goeda"


def upload(account, container, file_name, file_path):
    service = account.create_block_blob_service()
    service.create_blob_from_path(container, file_name, file_path)


def download(account, container_name, blob_name, path_to_file):
    service = account.create_block_blob_service()
    service.get_blob_to_path(container_name, blob_name, path_to_file)


def create_container(account, container_name):
    service = account.create_block_blob_service()
    service.create_container(container_name)
