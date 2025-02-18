#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright (c) 2018 by Delphix. All rights reserved.
#
# Author  : Marcin Przepiorowski
# Date    : September 2018


import logging
from dxm.lib.DxEngine.DxMaskingEngine import DxMaskingEngine
from dxm.lib.DxProfile.DxProfileExpList import DxProfileExpList
from dxm.lib.DxLogging import print_error
from dxm.lib.DxLogging import print_message
from dxm.lib.masking_api.api.profile_set_api import ProfileSetApi
from dxm.lib.masking_api.rest import ApiException
from dxm.lib.masking_api.genericmodel import GenericModel

class DxProfile(object):

    swagger_types = {
        'profile_set_id': 'int',
        'profile_set_name': 'str',
        'profile_expression_ids': 'list[int]',
        'created_by': 'str',
        'created_time': 'datetime',
        'description': 'str'
    }

    swagger_map = {
        'profile_set_id': 'profileSetId',
        'profile_set_name': 'profileSetName',
        'profile_expression_ids': 'profileExpressionIds',
        'created_by': 'createdBy',
        'created_time': 'createdTime',
        'description': 'description'
    }

    def __init__(self):
        """
        Constructor
        """
        #ProfileSet.__init__(self)
        self.__engine = DxMaskingEngine
        self.__logger = logging.getLogger()
        self.__logger.debug("creating DxProfileSet object")

        self.__api = ProfileSetApi
        self.__apiexc = ApiException
        self.__obj = None

    @property
    def obj(self):
        if self.__obj is not None:
            return self.__obj
        else:
            return None

    @property
    def profile_set_id(self):
        if self.obj is not None:
            return self.obj.profile_set_id
        else:
            return None

    @property
    def profile_set_name(self):
        if self.obj is not None:
            return self.obj.profile_set_name
        else:
            return None

    @property
    def profile_expression_ids(self):
        if self.obj is not None:
            return self.obj.profile_expression_ids
        else:
            return None

    @profile_expression_ids.setter
    def profile_expression_ids(self, value):
        self.obj.profile_expression_ids = value

    @property
    def description(self):
        if self.obj is not None and hasattr(self.obj,'description'):
            return self.obj.description
        else:
            return None

    @property
    def created_by(self):
        if self.obj is not None:
            return self.obj.created_by
        else:
            return None

    @property
    def created_time(self):
        if self.obj is not None:
            return self.obj.created_time
        else:
            return None


    def create_profile(self, profile_set_name, profile_expression_ids, created_by, description):

        self.__obj = GenericModel({ x:None for x in self.swagger_map.values()}, self.swagger_types, self.swagger_map)
        self.obj.profile_set_name = profile_set_name
        self.obj.profile_expression_ids = profile_expression_ids
        self.obj.created_by = created_by
        self.obj.description = description


    def from_profileset(self, profile):
        self.__obj = profile
        self.__obj.swagger_map = self.swagger_map
        self.__obj.swagger_types = self.swagger_types

    def set_expressions_using_names(self, expression_list):
        """
        Set an expression list using an expression names
        param1: expression_list: a list with expression names to set
        return 0 if all OK
        return 1 if expression not found
        """

        expression_ids_list = []
        profileexplist = DxProfileExpList()
        for expname in expression_list:
            peref = profileexplist.get_profileExpId_by_name(expname)
            if peref:
                expression_ids_list.append(peref)
            else:
                return []

        return expression_ids_list

    def add(self):
        """
        Add profile to Masking engine and print status message
        return a None if non error
        return 1 in case of error
        """

        if (self.obj.profile_set_name is None):
            print_error("Profile name is required")
            self.__logger.error("Profile name is required")
            return 1

        if (self.obj.profile_expression_ids is None):
            print_error("expression list is required")
            self.__logger.error("expression list is required")
            return 1

        try:
            self.__logger.debug("create profile input %s" % str(self))
            api_instance = self.__api(self.__engine.api_client)
            response = api_instance.create_profile_set(self.obj)
            self.from_profileset(response)
            self.__logger.debug("profile response %s"
                                % str(response))
            print_message("Profile %s added" % self.obj.profile_set_name)
            return 0
        except self.__apiexc as e:
            print_error(e.body)
            self.__logger.error(e)
            return 1

    def delete(self):
        """
        Delete profile set from Engine
        return a 0 if non error
        return 1 in case of error
        """

        try:
            api_instance = self.__api(self.__engine.api_client)
            response = api_instance.delete_profile_set(
                self.obj.profile_set_id,
                _request_timeout=self.__engine.get_timeout())
            self.__logger.debug("Profile response %s"
                                % str(response))
            print_message("Profile %s deleted" % self.obj.profile_set_name)
            return 0
        except self.__apiexc as e:
            print_error(e.body)
            self.__logger.error(e)
            return 1

    def update(self):
        """
        Update profile in Engine
        return a 0 if non error
        return 1 in case of error
        """

        try:
            api_instance = self.__api(self.__engine.api_client)
            self.__logger.debug("update profile request %s"
                                % str(self))
            response = api_instance.update_profile_set(
                self.obj.profile_set_id,
                self.obj,
                _request_timeout=self.__engine.get_timeout())
            self.__logger.debug("update response %s"
                                % str(response))
            print_message("Profile %s updated" % self.obj.profile_set_name)
            return 0
        except self.__apiexc as e:
            print_error(e.body)
            self.__logger.error(e)
            return 1
