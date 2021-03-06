# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument


def managed_network_managed_networks_list(cmd, client,
                                          resource_group_name=None,
                                          top=None,
                                          skiptoken=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name, top=top, skiptoken=skiptoken)
    return client.list_by_subscription(top=top, skiptoken=skiptoken)


def managed_network_managed_networks_show(cmd, client,
                                          resource_group_name,
                                          managed_network_name):
    return client.get(resource_group_name=resource_group_name, managed_network_name=managed_network_name)


def managed_network_managed_networks_create(cmd, client,
                                            resource_group_name,
                                            managed_network_name,
                                            location=None,
                                            tags=None,
                                            scope_management_groups=None,
                                            scope_subscriptions=None,
                                            scope_virtual_networks=None,
                                            scope_subnets=None):
    managed_network = {}
    managed_network['location'] = location  # string
    managed_network['tags'] = tags
    managed_network.setdefault('scope', {})['management_groups'] = None if scope_management_groups is None else scope_management_groups
    managed_network.setdefault('scope', {})['subscriptions'] = None if scope_subscriptions is None else scope_subscriptions
    managed_network.setdefault('scope', {})['virtual_networks'] = None if scope_virtual_networks is None else scope_virtual_networks
    managed_network.setdefault('scope', {})['subnets'] = None if scope_subnets is None else scope_subnets
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network=managed_network)


def managed_network_managed_networks_update(cmd, client,
                                            resource_group_name,
                                            managed_network_name,
                                            tags=None):
    parameters = {}
    parameters['tags'] = tags
    return client.update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, parameters=parameters)


def managed_network_managed_networks_delete(cmd, client,
                                            resource_group_name,
                                            managed_network_name):
    return client.delete(resource_group_name=resource_group_name, managed_network_name=managed_network_name)


def managed_network_scope_assignments_list(cmd, client,
                                           scope):
    return client.list(scope=scope)


def managed_network_scope_assignments_show(cmd, client,
                                           scope,
                                           scope_assignment_name):
    return client.get(scope=scope, scope_assignment_name=scope_assignment_name)


def managed_network_scope_assignments_create(cmd, client,
                                             scope,
                                             scope_assignment_name,
                                             location=None,
                                             assigned_managed_network=None):
    parameters = {}
    parameters['location'] = location  # string
    parameters['assigned_managed_network'] = assigned_managed_network  # string
    return client.create_or_update(scope=scope, scope_assignment_name=scope_assignment_name, parameters=parameters)


def managed_network_scope_assignments_update(cmd, client,
                                             scope,
                                             scope_assignment_name,
                                             location=None,
                                             assigned_managed_network=None):
    parameters = {}
    parameters['location'] = location  # string
    parameters['assigned_managed_network'] = assigned_managed_network  # string
    return client.create_or_update(scope=scope, scope_assignment_name=scope_assignment_name, parameters=parameters)


def managed_network_scope_assignments_delete(cmd, client,
                                             scope,
                                             scope_assignment_name):
    return client.delete(scope=scope, scope_assignment_name=scope_assignment_name)


def managed_network_managed_network_groups_list(cmd, client,
                                                resource_group_name,
                                                managed_network_name,
                                                top=None,
                                                skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name, managed_network_name=managed_network_name, top=top, skiptoken=skiptoken)


def managed_network_managed_network_groups_show(cmd, client,
                                                resource_group_name,
                                                managed_network_name,
                                                managed_network_group_name):
    return client.get(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_group_name=managed_network_group_name)


def managed_network_managed_network_groups_create(cmd, client,
                                                  resource_group_name,
                                                  managed_network_name,
                                                  managed_network_group_name,
                                                  managed_network_group):
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_group_name=managed_network_group_name, managed_network_group=managed_network_group)


def managed_network_managed_network_groups_update(cmd, client,
                                                  resource_group_name,
                                                  managed_network_name,
                                                  managed_network_group_name,
                                                  managed_network_group):
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_group_name=managed_network_group_name, managed_network_group=managed_network_group)


def managed_network_managed_network_groups_delete(cmd, client,
                                                  resource_group_name,
                                                  managed_network_name,
                                                  managed_network_group_name):
    return client.delete(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_group_name=managed_network_group_name)


def managed_network_managed_network_peering_policies_list(cmd, client,
                                                          resource_group_name,
                                                          managed_network_name,
                                                          top=None,
                                                          skiptoken=None):
    return client.list_by_managed_network(resource_group_name=resource_group_name, managed_network_name=managed_network_name, top=top, skiptoken=skiptoken)


def managed_network_managed_network_peering_policies_show(cmd, client,
                                                          resource_group_name,
                                                          managed_network_name,
                                                          managed_network_peering_policy_name):
    return client.get(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_peering_policy_name=managed_network_peering_policy_name)


def managed_network_managed_network_peering_policies_create(cmd, client,
                                                            resource_group_name,
                                                            managed_network_name,
                                                            managed_network_peering_policy_name,
                                                            properties_type,
                                                            location=None,
                                                            id=None,
                                                            properties_spokes=None,
                                                            properties_mesh=None):
    managed_network_policy = {}
    managed_network_policy['location'] = location  # string
    managed_network_policy.setdefault('properties', {})['type'] = properties_type  # choice
    managed_network_policy['id'] = id  # string
    managed_network_policy.setdefault('properties', {})['spokes'] = None if properties_spokes is None else properties_spokes
    managed_network_policy.setdefault('properties', {})['mesh'] = None if properties_mesh is None else properties_mesh
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_peering_policy_name=managed_network_peering_policy_name, managed_network_policy=managed_network_policy)


def managed_network_managed_network_peering_policies_update(cmd, client,
                                                            resource_group_name,
                                                            managed_network_name,
                                                            managed_network_peering_policy_name,
                                                            properties_type,
                                                            location=None,
                                                            id=None,
                                                            properties_spokes=None,
                                                            properties_mesh=None):
    managed_network_policy = {}
    managed_network_policy['location'] = location  # string
    managed_network_policy.setdefault('properties', {})['type'] = properties_type  # choice
    managed_network_policy['id'] = id  # string
    managed_network_policy.setdefault('properties', {})['spokes'] = None if properties_spokes is None else properties_spokes
    managed_network_policy.setdefault('properties', {})['mesh'] = None if properties_mesh is None else properties_mesh
    return client.create_or_update(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_peering_policy_name=managed_network_peering_policy_name, managed_network_policy=managed_network_policy)


def managed_network_managed_network_peering_policies_delete(cmd, client,
                                                            resource_group_name,
                                                            managed_network_name,
                                                            managed_network_peering_policy_name):
    return client.delete(resource_group_name=resource_group_name, managed_network_name=managed_network_name, managed_network_peering_policy_name=managed_network_peering_policy_name)


def managed_network_operations_list(cmd, client):
    return client.list()
