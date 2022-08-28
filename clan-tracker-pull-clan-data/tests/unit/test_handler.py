import pytest

from hello_world import app
from schema.aws.cloudwatch.cloudwatchalarmstatechange import AWSEvent
from schema.aws.cloudwatch.cloudwatchalarmstatechange import CloudWatchAlarmStateChange
from schema.aws.cloudwatch.cloudwatchalarmstatechange import Marshaller

@pytest.fixture()
def eventBridgeEvent():
    """ Generates EventBridge Event"""

    return {
            "version":"0",
            "id":"7bf73129-1428-4cd3-a780-95db273d1602",
            "detail-type":"CloudWatch Alarm State Change",
            "source":"aws.cloudwatch",
            "account":"123456789012",
            "time":"2015-11-11T21:29:54Z",
            "region":"us-east-1",
            "resources":[
              "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"
            ],
            "detail":{
              "ADD-YOUR-FIELDS-HERE":""
            }
    }


def test_lambda_handler(eventBridgeEvent, mocker):

    ret = app.lambda_handler(eventBridgeEvent, "")

    awsEventRet:AWSEvent = Marshaller.unmarshall(ret, AWSEvent)
    detailRet:CloudWatchAlarmStateChange = awsEventRet.detail

    assert awsEventRet.detail_type.startswith("HelloWorldFunction updated event of ")
