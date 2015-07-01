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

from openstack import resource

from helionsdk.dns import dns_service


class Version(resource.Resource):
    resource_key = 'version'
    resources_key = 'versions'
    base_path = '/'
    service = dns_service.DnsService(
        version=dns_service.DnsService.UNVERSIONED
    )

    # capabilities
    allow_list = True

    # Properties
    links = resource.prop('links')
    status = resource.prop('status')
    updated = resource.prop('updated')
