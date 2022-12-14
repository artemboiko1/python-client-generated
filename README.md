# swagger-client
API of the Prometheus Alertmanager (https://github.com/prometheus/alertmanager)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AlertApi(swagger_client.ApiClient(configuration))
active = true # bool | Show active alerts (optional) (default to true)
silenced = true # bool | Show silenced alerts (optional) (default to true)
inhibited = true # bool | Show inhibited alerts (optional) (default to true)
unprocessed = true # bool | Show unprocessed alerts (optional) (default to true)
filter = ['filter_example'] # list[str] | A list of matchers to filter alerts by (optional)
receiver = 'receiver_example' # str | A regex matching receivers to filter alerts by (optional)

try:
    api_response = api_instance.get_alerts(active=active, silenced=silenced, inhibited=inhibited, unprocessed=unprocessed, filter=filter, receiver=receiver)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->get_alerts: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AlertApi(swagger_client.ApiClient(configuration))
body = [swagger_client.PostableAlert()] # list[PostableAlert] | The alerts to create

try:
    api_instance.post_alerts(body)
except ApiException as e:
    print("Exception when calling AlertApi->post_alerts: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */api/v2/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertApi* | [**get_alerts**](docs/AlertApi.md#get_alerts) | **GET** /alerts | 
*AlertApi* | [**post_alerts**](docs/AlertApi.md#post_alerts) | **POST** /alerts | 
*AlertgroupApi* | [**get_alert_groups**](docs/AlertgroupApi.md#get_alert_groups) | **GET** /alerts/groups | 
*GeneralApi* | [**get_status**](docs/GeneralApi.md#get_status) | **GET** /status | 
*ReceiverApi* | [**get_receivers**](docs/ReceiverApi.md#get_receivers) | **GET** /receivers | 
*SilenceApi* | [**delete_silence**](docs/SilenceApi.md#delete_silence) | **DELETE** /silence/{silenceID} | 
*SilenceApi* | [**get_silence**](docs/SilenceApi.md#get_silence) | **GET** /silence/{silenceID} | 
*SilenceApi* | [**get_silences**](docs/SilenceApi.md#get_silences) | **GET** /silences | 
*SilenceApi* | [**post_silences**](docs/SilenceApi.md#post_silences) | **POST** /silences | 

## Documentation For Models

 - [Alert](docs/Alert.md)
 - [AlertGroup](docs/AlertGroup.md)
 - [AlertGroups](docs/AlertGroups.md)
 - [AlertStatus](docs/AlertStatus.md)
 - [AlertmanagerConfig](docs/AlertmanagerConfig.md)
 - [AlertmanagerStatus](docs/AlertmanagerStatus.md)
 - [ClusterStatus](docs/ClusterStatus.md)
 - [GettableAlert](docs/GettableAlert.md)
 - [GettableAlerts](docs/GettableAlerts.md)
 - [GettableSilence](docs/GettableSilence.md)
 - [GettableSilences](docs/GettableSilences.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [LabelSet](docs/LabelSet.md)
 - [Matcher](docs/Matcher.md)
 - [Matchers](docs/Matchers.md)
 - [PeerStatus](docs/PeerStatus.md)
 - [PostableAlert](docs/PostableAlert.md)
 - [PostableAlerts](docs/PostableAlerts.md)
 - [PostableSilence](docs/PostableSilence.md)
 - [Receiver](docs/Receiver.md)
 - [Silence](docs/Silence.md)
 - [SilenceStatus](docs/SilenceStatus.md)
 - [VersionInfo](docs/VersionInfo.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


