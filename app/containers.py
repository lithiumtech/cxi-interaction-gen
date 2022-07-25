# internal 
from services.dynamodb import DynoDb

#site-packages
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from dependency_injector import containers, providers

class Core(containers.DeclarativeContainer): 
    # pass some sort of configuration
    config = providers.Configuration()

class Gateways(containers.DeclarativeContainer): 
    config = providers.Configuration()

    db_client = providers.Singleton(
        boto3.client,
        service_name="dynamodb",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key
    )

    db_resource = providers.Singleton(
        boto3.resource,
        service_name="dynamodb",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key
    )

class Services(containers.DeclarativeContainer):

    config = providers.Configuration()
    gateways = providers.DependenciesContainer()

    # boto3.resource('dynamodb')
    db = providers.Singleton(
        DynoDb,
        client = gateways.client,
        resource = gateways.resource
    )

class Application(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files = ["app_config.yaml"])
    services = providers.Container(
        Services
    )