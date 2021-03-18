import boto3
import datetime


if __name__== '__main__':
    ec2client = boto3.client(
        'ec2',
        'us-east-2',
        aws_access_key_id="AKIAS6VOYMGSXSTB27FK",
        aws_secret_access_key="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"

    )

    reponse= ec2client.describe_instances()
    #  ''' Filters=[
    #         {
    #             'Name': 'tag:status',
    #             'Values': ['protected']
    #         }
    #     ]
    # )
    ids =[]
    for res in reponse['Reservations']:
        for instance in res['Instances']:
            print(instance['InstanceId'])
            print(instance['Tags'])
            for tag in instance['Tags']:
                if tag['Key'] == 'status' :
                    print(tag['Value'])
                    if tag['Value'] != 'protected':
                        print('Littel bitch termanated'+' '+instance['InstanceId'])
                        ids.append(instance['InstanceId'])
                        image_id =ec2client.create_image(InstanceId='i-0375386af21bce21b',Name='dan')
                        print(imageid[0])
                       # ec2client.terminate_instances(InstanceIds=[instance['InstanceId']])

                    else:
                        print('protection bitch')


