import boto3
import datetime

def create_security_group(event, context):
    # Configurar la fecha actual
    current_date = datetime.datetime.now().strftime("%Y%m%d")

    # Nombre del grupo de seguridad
    group_name = "Alex251178-" + current_date

    # Crea una conexión al servicio EC2 de AWS
    ec2 = boto3.resource('ec2')

    # Crea el grupo de seguridad
    security_group = ec2.create_security_group(
        GroupName=group_name,
        Description='Security Group created by Lambda function',
        VpcId='tu_vpc_id_aqui'  # Reemplaza esto con el ID de tu VPC
    )

    # Agrega las reglas de entrada
    security_group.authorize_ingress(
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 443,
                'ToPort': 443,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 3000,
                'ToPort': 3000,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            }
        ]
    )

    # Agrega la regla de salida que permita todo el tráfico
    security_group.authorize_egress(
        IpPermissions=[
            {
                'IpProtocol': '-1',
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            }
        ]
    )

    print(f"Grupo de seguridad '{group_name}' creado exitosamente.")
    return {
        'statusCode': 200,
        'body': f"Grupo de seguridad '{group_name}' creado exitosamente."
    }

# Si deseas probar localmente, descomenta las siguientes líneas:
# event = {}
# context = {}
# print(create_security_group(event, context))



event = {}
context = {}
print(lambda_handler(event, context))
