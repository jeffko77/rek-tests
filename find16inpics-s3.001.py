import boto3
s3 = boto3.resource('s3')
bucket = 'custom-labels-console-us-east-2-d03e0eafd7'
bucketObj = s3.Bucket('custom-labels-console-us-east-2-d03e0eafd7')

def detect_text(photo, bucket):

    session = boto3.Session(profile_name='default')
    client = session.client('rekognition')

    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})

    textDetections = response['TextDetections']
    for text in textDetections:
        ##print(text['DetectedText'])
        if text['DetectedText'] == str(16):
            print(photo)
'''    print('Detected text\n----------')
    for text in textDetections:
        print('Detected text:' + text['DetectedText'])
        print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            print('Parent Id: {}'.format(text['ParentId']))
        print('Type:' + text['Type'])
        print()
    return len(textDetections)
'''


def findtext(filename):
    photo = filename
    ##print("Filename:" + str(photo))
    text_count = detect_text(photo, bucket)
    ##print("Text detected: " + str(text_count))

if __name__ == "__main__":

    for obj in bucketObj.objects.all():
        findtext(str(obj.key))    
