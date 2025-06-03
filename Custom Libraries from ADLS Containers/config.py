"""Configuration settings for Databricks ADLS integration"""

# ADLS Storage Settings
STORAGE_ACCOUNT = "araostorage"
CONTAINER_NAME = "araolibraryloadtest"
MOUNT_POINT = "/mnt/libs"

# Databricks Secrets
SECRET_SCOPE = "adls-secrets"
SECRET_KEY = "adls-access-key"

# ADLS Paths
def get_adls_path(path: str = "") -> str:
    """Generate full ADLS path with optional subpath"""
    return f"abfss://{CONTAINER_NAME}@{STORAGE_ACCOUNT}.dfs.core.usgovcloudapi.net/{path.strip('/')}"

# Local DBFS Paths
TEMP_DIR = "/dbfs/tmp"
LIBS_DIR = f"{TEMP_DIR}/libs"

# Package Information
PACKAGE_NAME = "mylib"
PACKAGE_VERSION = "0.1"
WHEEL_FILENAME = f"{PACKAGE_NAME}-{PACKAGE_VERSION}-py3-none-any.whl" 