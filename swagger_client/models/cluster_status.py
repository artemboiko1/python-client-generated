# coding: utf-8

"""
    Alertmanager API

    API of the Prometheus Alertmanager (https://github.com/prometheus/alertmanager)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ClusterStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'status': 'str',
        'peers': 'list[PeerStatus]'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'peers': 'peers'
    }

    def __init__(self, name=None, status=None, peers=None):  # noqa: E501
        """ClusterStatus - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._status = None
        self._peers = None
        self.discriminator = None
        if name is not None:
            self.name = name
        self.status = status
        if peers is not None:
            self.peers = peers

    @property
    def name(self):
        """Gets the name of this ClusterStatus.  # noqa: E501


        :return: The name of this ClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterStatus.


        :param name: The name of this ClusterStatus.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this ClusterStatus.  # noqa: E501


        :return: The status of this ClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterStatus.


        :param status: The status of this ClusterStatus.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ready", "settling", "disabled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def peers(self):
        """Gets the peers of this ClusterStatus.  # noqa: E501


        :return: The peers of this ClusterStatus.  # noqa: E501
        :rtype: list[PeerStatus]
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this ClusterStatus.


        :param peers: The peers of this ClusterStatus.  # noqa: E501
        :type: list[PeerStatus]
        """

        self._peers = peers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ClusterStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
