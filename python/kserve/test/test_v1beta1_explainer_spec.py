# Copyright 2021 The KServe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KServe

    Python SDK for KServe  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kserve
from kserve.models.v1beta1_explainer_spec import V1beta1ExplainerSpec  # noqa: E501
from kserve.rest import ApiException

class TestV1beta1ExplainerSpec(unittest.TestCase):
    """V1beta1ExplainerSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1ExplainerSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kserve.models.v1beta1_explainer_spec.V1beta1ExplainerSpec()  # noqa: E501
        if include_optional :
            return V1beta1ExplainerSpec(
                active_deadline_seconds = 56, 
                affinity = None, 
                aix = kserve.models.v1beta1_aix_explainer_spec.V1beta1AIXExplainerSpec(
                    args = [
                        '0'
                        ], 
                    command = [
                        '0'
                        ], 
                    config = {
                        'key' : '0'
                        }, 
                    env = [
                        None
                        ], 
                    env_from = [
                        None
                        ], 
                    image = '0', 
                    image_pull_policy = '0', 
                    lifecycle = None, 
                    liveness_probe = None, 
                    name = '0', 
                    ports = [
                        None
                        ], 
                    readiness_probe = None, 
                    resources = None, 
                    runtime_version = '0', 
                    security_context = None, 
                    startup_probe = None, 
                    stdin = True, 
                    stdin_once = True, 
                    storage_uri = '0', 
                    termination_message_path = '0', 
                    termination_message_policy = '0', 
                    tty = True, 
                    type = '0', 
                    volume_devices = [
                        None
                        ], 
                    volume_mounts = [
                        None
                        ], 
                    working_dir = '0', ), 
                alibi = kserve.models.v1beta1_alibi_explainer_spec.V1beta1AlibiExplainerSpec(
                    args = [
                        '0'
                        ], 
                    command = [
                        '0'
                        ], 
                    config = {
                        'key' : '0'
                        }, 
                    env = [
                        None
                        ], 
                    env_from = [
                        None
                        ], 
                    image = '0', 
                    image_pull_policy = '0', 
                    lifecycle = None, 
                    liveness_probe = None, 
                    name = '0', 
                    ports = [
                        None
                        ], 
                    readiness_probe = None, 
                    resources = None, 
                    runtime_version = '0', 
                    security_context = None, 
                    startup_probe = None, 
                    stdin = True, 
                    stdin_once = True, 
                    storage_uri = '0', 
                    termination_message_path = '0', 
                    termination_message_policy = '0', 
                    tty = True, 
                    type = '0', 
                    volume_devices = [
                        None
                        ], 
                    volume_mounts = [
                        None
                        ], 
                    working_dir = '0', ), 
                automount_service_account_token = True, 
                batcher = kserve.models.v1beta1_batcher.V1beta1Batcher(
                    max_batch_size = 56, 
                    max_latency = 56, 
                    timeout = 56, ), 
                canary_traffic_percent = 56, 
                container_concurrency = 56, 
                containers = [
                    None
                    ], 
                dns_config = None, 
                dns_policy = '0', 
                enable_service_links = True, 
                ephemeral_containers = [
                    None
                    ], 
                host_aliases = [
                    None
                    ], 
                host_ipc = True, 
                host_network = True, 
                host_pid = True, 
                hostname = '0', 
                image_pull_secrets = [
                    None
                    ], 
                init_containers = [
                    None
                    ], 
                logger = kserve.models.v1beta1_logger_spec.V1beta1LoggerSpec(
                    mode = '0', 
                    url = '0', ), 
                max_replicas = 56, 
                min_replicas = 56, 
                node_name = '0', 
                node_selector = {
                    'key' : '0'
                    }, 
                overhead = {
                    'key' : None
                    }, 
                preemption_policy = '0', 
                priority = 56, 
                priority_class_name = '0', 
                readiness_gates = [
                    None
                    ], 
                restart_policy = '0', 
                runtime_class_name = '0', 
                scheduler_name = '0', 
                security_context = None, 
                service_account = '0', 
                service_account_name = '0', 
                share_process_namespace = True, 
                subdomain = '0', 
                termination_grace_period_seconds = 56, 
                timeout = 56, 
                tolerations = [
                    None
                    ], 
                topology_spread_constraints = [
                    None
                    ], 
                volumes = [
                    None
                    ]
            )
        else :
            return V1beta1ExplainerSpec(
        )

    def testV1beta1ExplainerSpec(self):
        """Test V1beta1ExplainerSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
