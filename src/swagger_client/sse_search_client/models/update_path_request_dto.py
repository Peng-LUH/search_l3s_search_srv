# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdatePathRequestDto(object):
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
        'title': 'str',
        'description': 'str',
        'target_audience': 'list[str]',
        'owner': 'str',
        'lifecycle': 'object',
        'requirements': 'list[str]',
        'path_goals': 'list[str]',
        'recommended_unit_sequence': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'target_audience': 'targetAudience',
        'owner': 'owner',
        'lifecycle': 'lifecycle',
        'requirements': 'requirements',
        'path_goals': 'pathGoals',
        'recommended_unit_sequence': 'recommendedUnitSequence'
    }

    def __init__(self, title=None, description=None, target_audience=None, owner=None, lifecycle=None, requirements=None, path_goals=None, recommended_unit_sequence=None):  # noqa: E501
        """UpdatePathRequestDto - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._description = None
        self._target_audience = None
        self._owner = None
        self._lifecycle = None
        self._requirements = None
        self._path_goals = None
        self._recommended_unit_sequence = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if target_audience is not None:
            self.target_audience = target_audience
        if owner is not None:
            self.owner = owner
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if requirements is not None:
            self.requirements = requirements
        if path_goals is not None:
            self.path_goals = path_goals
        if recommended_unit_sequence is not None:
            self.recommended_unit_sequence = recommended_unit_sequence

    @property
    def title(self):
        """Gets the title of this UpdatePathRequestDto.  # noqa: E501


        :return: The title of this UpdatePathRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdatePathRequestDto.


        :param title: The title of this UpdatePathRequestDto.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this UpdatePathRequestDto.  # noqa: E501


        :return: The description of this UpdatePathRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePathRequestDto.


        :param description: The description of this UpdatePathRequestDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def target_audience(self):
        """Gets the target_audience of this UpdatePathRequestDto.  # noqa: E501


        :return: The target_audience of this UpdatePathRequestDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this UpdatePathRequestDto.


        :param target_audience: The target_audience of this UpdatePathRequestDto.  # noqa: E501
        :type: list[str]
        """

        self._target_audience = target_audience

    @property
    def owner(self):
        """Gets the owner of this UpdatePathRequestDto.  # noqa: E501


        :return: The owner of this UpdatePathRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UpdatePathRequestDto.


        :param owner: The owner of this UpdatePathRequestDto.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def lifecycle(self):
        """Gets the lifecycle of this UpdatePathRequestDto.  # noqa: E501


        :return: The lifecycle of this UpdatePathRequestDto.  # noqa: E501
        :rtype: object
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        """Sets the lifecycle of this UpdatePathRequestDto.


        :param lifecycle: The lifecycle of this UpdatePathRequestDto.  # noqa: E501
        :type: object
        """

        self._lifecycle = lifecycle

    @property
    def requirements(self):
        """Gets the requirements of this UpdatePathRequestDto.  # noqa: E501


        :return: The requirements of this UpdatePathRequestDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this UpdatePathRequestDto.


        :param requirements: The requirements of this UpdatePathRequestDto.  # noqa: E501
        :type: list[str]
        """

        self._requirements = requirements

    @property
    def path_goals(self):
        """Gets the path_goals of this UpdatePathRequestDto.  # noqa: E501


        :return: The path_goals of this UpdatePathRequestDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._path_goals

    @path_goals.setter
    def path_goals(self, path_goals):
        """Sets the path_goals of this UpdatePathRequestDto.


        :param path_goals: The path_goals of this UpdatePathRequestDto.  # noqa: E501
        :type: list[str]
        """

        self._path_goals = path_goals

    @property
    def recommended_unit_sequence(self):
        """Gets the recommended_unit_sequence of this UpdatePathRequestDto.  # noqa: E501


        :return: The recommended_unit_sequence of this UpdatePathRequestDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._recommended_unit_sequence

    @recommended_unit_sequence.setter
    def recommended_unit_sequence(self, recommended_unit_sequence):
        """Sets the recommended_unit_sequence of this UpdatePathRequestDto.


        :param recommended_unit_sequence: The recommended_unit_sequence of this UpdatePathRequestDto.  # noqa: E501
        :type: list[str]
        """

        self._recommended_unit_sequence = recommended_unit_sequence

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
        if issubclass(UpdatePathRequestDto, dict):
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
        if not isinstance(other, UpdatePathRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
