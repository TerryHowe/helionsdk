# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from helionsdk.dns import dns_service
from openstack import resource


class Domain(resource.Resource):
    resource_key = 'domain'
    resources_key = 'domains'
    base_path = '/domains'
    service = dns_service.DnsService()

    # capabilities
    allow_create = True
    allow_retrieve = True
    allow_update = True
    allow_delete = True
    allow_list = True
    put_update = True

    created_at = resource.prop('created_at')
    email = resource.prop('email')
    name = resource.prop('name')
    serial = resource.prop('serial')
    ttl = resource.prop('ttl')