import boto3
import configparser
from pathlib import Path


config = configparser.ConfigParser()
config.read_file(open("config.cfg"))

S3 = boto3.resource(service_name="s3", region_name="eu-west-1", aws_access_key_id=config.get("AWS", "AWSAccessKeyId"),
                    aws_secret_access_key=config.get("AWS", "AWSSecretKey"))

# take dowloaded videos from local host and put them in s3.
# list all video in an s3 bucket.
# get a specific video from s3 bucket.


def list_s3_files(bucket_name):
    objects = []
    for my_bucket_object in S3.Bucket(bucket_name).objects.all():
        objects.append(my_bucket_object.key)

    return objects


# def download_video(video_name):

def download_all_files(bucket_name):
    """get all files in an s3 bucket.
    """

    try:
        my_bucket = S3.Bucket(bucket_name)
        for s3_object in my_bucket.objects.all():
            filename = s3_object.key
            my_bucket.download_file(s3_object.key, filename)
    except Exception as e:
        raise e
    return True


# download_all_files("landingzone1999c7acde43-8029-49ce-b848-153513fd51c6")
