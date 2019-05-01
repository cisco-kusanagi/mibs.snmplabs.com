#
# PySNMP MIB module CISCO-COPS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COPS-CLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:54:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, TimeTicks, Counter64, iso, ModuleIdentity, NotificationType, Integer32, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "TimeTicks", "Counter64", "iso", "ModuleIdentity", "NotificationType", "Integer32", "Gauge32", "Counter32")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
ciscoCopsClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 140))
ciscoCopsClientMIB.setRevisions(('2005-11-14 00:00', '2000-06-11 00:00', '1999-09-16 00:40',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCopsClientMIB.setRevisionsDescriptions(('Updated the imports such that Unsigned32 is imported from SNMPv2-SMI instead of CISCO-TC. Changed the syntax of the textual conventions CopsRole, CopsRoleCombination, CopsDomainName from DisplayString to OCTET STRING.', 'Added support for optional role configuration.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCopsClientMIB.setLastUpdated('200511140000Z')
if mibBuilder.loadTexts: ciscoCopsClientMIB.setOrganization('Cisco Systems Inc. ')
if mibBuilder.loadTexts: ciscoCopsClientMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wbu@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCopsClientMIB.setDescription('This MIB module is for configuration & statistic query of Common Open Policy Service(COPS) client feature on the Cisco device. COPS is a simple client/server model for supporting policy control over QoS Signaling Protocols and provisioned QoS resource management. COPS is a simple query and response protocol that can be used to exchange policy information between a policy server (Policy Decision Point or PDP) and its clients (Policy Enforcement Points or PEPs).')
class CopsRole(TextualConvention, OctetString):
    description = "A display string where valid letters are a-z, A-Z, 0-9, ., - and _. Name can not start with an '_'. Policies are assigned to a 'role', and one or more 'roles' are assigned to interfaces, such that an interface takes on the policies indirectly as the policies of the roles assigned to that interface."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class CopsRoleCombination(TextualConvention, OctetString):
    description = "A display string consisting of a set of roles concatenated with '+' characters where the roles are in lexicographic order from minimum to maximum. Policies are assigned to a 'role', and one or more 'roles' are assigned to interfaces, such that an interface takes on the policies indirectly as the policies of the roles assigned to that interface. When one or more roles assigned to an interface, that set of roles is known as a role-combination."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CopsDomainName(TextualConvention, OctetString):
    description = "A display string where valid letters are a-z, A-Z, 0-9, ., - and _. Name can not start with an '_'. The COPS domain which a COPS client type belongs to. This is so that a COPS server supporting multiple domains can push the correct set of domain policies to a device."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class CopsClientType(TextualConvention, Integer32):
    description = 'An enumerated value for all the supported COPS client type. rsvp(1) Resource Reservation Protocol(RSVP). RSVP is a signaling mechanism that the applications will use to signal parameters to the network, so that network can assign QoS for the application data stream. provisioning(2) Provisioning. A client type for COPS to support policy provisioning. This client type is independent of the type of policy (QoS, VPNs, Security, etc.) and it is based on the concept of PIBs (Policy Information Bases [PIB]).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rsvp", 1), ("provisioning", 2))

ccopsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 1))
ccopsGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1))
ccopsServerMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('servers').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsServerMax.setStatus('current')
if mibBuilder.loadTexts: ccopsServerMax.setDescription('Maximum number of configurable COPS servers allowed for each client type. A value of zero indicates no limitation on the number of configurable COPS servers.')
ccopsMaxRole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 2), Unsigned32()).setUnits('roles').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsMaxRole.setStatus('current')
if mibBuilder.loadTexts: ccopsMaxRole.setDescription('Indicates the maximum number of roles supported by this device. A value of zero indicates no limitation on the number of roles.')
ccopsMaxRoleCombination = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 3), Unsigned32()).setUnits('role-combinations').setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsMaxRoleCombination.setStatus('current')
if mibBuilder.loadTexts: ccopsMaxRoleCombination.setDescription('Indicates the maximum number of role-combinations supported by this device. A value of zero indicates no limitation on the number of role-combinations. Each CopsRoleCombination may contain up to ccopsMaxRole roles.')
ccopsServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4), )
if mibBuilder.loadTexts: ccopsServerConfigTable.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigTable.setDescription('A list of possible COPS servers that the COPS client will try to connect to in order of ccopsServerConfigPriority.')
ccopsServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-COPS-CLIENT-MIB", "ccopsServerConfigClientType"), (1, "CISCO-COPS-CLIENT-MIB", "ccopsServerConfigName"))
if mibBuilder.loadTexts: ccopsServerConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigEntry.setDescription('A set of configuration information regarding a single COPS server from the point of view of a COPS client. The entry is created and deleted by using ccopsServerConfigStatus. An entry may not exist in the active state unless all objects in the entry have an appropriate value. Each client type can have its own COPS servers. By creating, deleting or modifying an entry in this table, users can add, delete or modify a COPS server for a particular client type for the device. In order to get policies from COPS server for a client type, user has to create an entry for such client type.')
ccopsServerConfigClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 1), CopsClientType())
if mibBuilder.loadTexts: ccopsServerConfigClientType.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigClientType.setDescription('The type of policies to be retrieved from this server.')
ccopsServerConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: ccopsServerConfigName.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigName.setDescription('The IP address or the hostname of a COPS server. If a hostname is used, it will be resolved to an address prior to each attempt to setup a connection to a PDP. If the PEP cannot resolve the hostname, the connection attempt will fail. Use of IP address values is preferred, except in cases where a hostname must/should be used (e.g. if the PDP has a dynamic address)')
ccopsServerConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsServerConfigPriority.setReference('Reference Internet Draft, The COPS (Common Open Policy Service) Protocol, PDP Redirect.')
if mibBuilder.loadTexts: ccopsServerConfigPriority.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigPriority.setDescription('The priority of this entry relative to other entries. The COPS client will attempt to contact COPS servers for the appropriate Client-Type in the order of their priority values. COPS servers designated by the COPS protocol PDP-Redirect mechanism are always used in preference to any entries in this table. When ccopsServerMax mib object is not zero, the valid value for ccopsServerConfigPriority ranges from zero to ccopsServerMax minus one. When the ccopsServerMax mib object is zero, any valid unsigned value may be used. For servers with different value of ccopsServerConfigPriority, the server with lowest value has highest priority. For servers with same value of ccopsServerConfigPriority and ccopsServerConfigClientType, the relative priority of Servers is determined by a numerical comparison of their IP addresses, with the lowest address having higher priority.')
ccopsServerConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(3288)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsServerConfigPort.setReference('Reference Internet Draft, The COPS (Common Open Policy Service) Protocol, Port number.')
if mibBuilder.loadTexts: ccopsServerConfigPort.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigPort.setDescription('The destination port number to which COPS server messages should be sent. By default the COPS service will be provided on the well-known COPS protocol port number 3288.')
ccopsServerConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsServerConfigStatus.setStatus('current')
if mibBuilder.loadTexts: ccopsServerConfigStatus.setDescription('The status of COPS server configuration for a client type. An entry may not exist in the active state unless all objects in the entry have an appropriate value. Once a row becomes active, value in any other column within such row cannot be modified except by setting ccopsServerConfigStatus to notInService(2) for such row.')
ccopsInitialTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsInitialTimeout.setStatus('current')
if mibBuilder.loadTexts: ccopsInitialTimeout.setDescription('If the device can not connect to the last connected COPS server, it uses this value for the initial retry time-out and then retries to connect after this time-out period. This value is re-used for the first retry after every successful connection. When the device is connecting to COPS server the first time or the last connected COPS server is no longer available, it will attempt to contact COPS servers existing in ccopsServerConfigTable for the appropriate Client-Type in the order of their priority values.')
ccopsTimeoutIncrement = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsTimeoutIncrement.setStatus('current')
if mibBuilder.loadTexts: ccopsTimeoutIncrement.setDescription('On every consecutive failure to connect to all existing COPS server for a client type, the COPS client increases the retry time-out by ccopsTimeoutIncrement but not greater than ccopsTimeoutMax.')
ccopsTimeoutMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsTimeoutMax.setStatus('current')
if mibBuilder.loadTexts: ccopsTimeoutMax.setDescription('The maximum retry time-out that the COPS client allows. On every consecutive failure to connect to all COPS servers, the COPS client increases the retry time-out up to ccopsTimeoutMax.')
ccopsDomainTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8), )
if mibBuilder.loadTexts: ccopsDomainTable.setStatus('current')
if mibBuilder.loadTexts: ccopsDomainTable.setDescription('A list of COPS domains for each client type supported in the device.')
ccopsDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1), ).setIndexNames((0, "CISCO-COPS-CLIENT-MIB", "ccopsDomainClientType"))
if mibBuilder.loadTexts: ccopsDomainEntry.setStatus('current')
if mibBuilder.loadTexts: ccopsDomainEntry.setDescription('A set of domain configuration information regarding a single COPS client type. An entry will exist for each COPS client type which is supported in the device. For each COPS client type supported in the device, a domain name should be specified if the COPS server for that client type has multiple domains defined in its database.')
ccopsDomainClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1, 1), CopsClientType())
if mibBuilder.loadTexts: ccopsDomainClientType.setStatus('current')
if mibBuilder.loadTexts: ccopsDomainClientType.setDescription('The type of COPS client.')
ccopsDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 8, 1, 2), CopsDomainName().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsDomainName.setReference('Reference CISCO-QOS-MIB, qosPolicySource.')
if mibBuilder.loadTexts: ccopsDomainName.setStatus('current')
if mibBuilder.loadTexts: ccopsDomainName.setDescription('The COPS domain which this client type belongs to. This is so that a COPS server supporting multiple domains can push the correct set of domain policies to this device. Zero length name is default. COPS server have a default set of policies for clients who have zero length domain names. Changing the COPS domain name while qosPolicySource is cops(2) will result in requesting new policies from the cops server and configuring the device with those new policies. The value of ccopsDomainName is ignored if qosPolicySource is local(1).')
ccopsRoleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9), )
if mibBuilder.loadTexts: ccopsRoleTable.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleTable.setDescription('A list of roles. The number of entries is determined by ccopsMaxRole.')
ccopsRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1), ).setIndexNames((1, "CISCO-COPS-CLIENT-MIB", "ccopsRoleName"))
if mibBuilder.loadTexts: ccopsRoleEntry.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleEntry.setDescription('Entry containing COPS-PR role information. The entry is created, deleted and modified by using ccopsRoleStatus. There is a maximum on the number of roles which may be configured per device. In order to make a role available for interface to construct its role combination, such role must exist in the role table. Deleting a role in ccopsRoleTable also removes that role from all role combinations for all interfaces. Therefore, a particular role can not be added into the role combination for any interface if it is removed from this table.')
ccopsRoleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1, 1), CopsRole())
if mibBuilder.loadTexts: ccopsRoleName.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleName.setDescription('The name of the role. Only roles which were defined in COPS server should be used. COPS server will only supply the policies for those roles defined in its database.')
ccopsRoleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 9, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccopsRoleStatus.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleStatus.setDescription('This object is used to manage creation, deletion and modification of rows in this table. An entry may not exist in the active state unless all objects in the entry have an appropriate value. Once a row becomes active, value in any other column within such row cannot be modified except by setting ccopsRoleStatus to notInService(2) for such row. Deleting a row results in removing this ccopsRoleName from all role combinations in the ccopsIfTable')
ccopsIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10), )
if mibBuilder.loadTexts: ccopsIfTable.setStatus('current')
if mibBuilder.loadTexts: ccopsIfTable.setDescription('A list of interface entries. An entry will exist for each interface which supports COPS-PR feature.')
ccopsIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ccopsIfEntry.setStatus('current')
if mibBuilder.loadTexts: ccopsIfEntry.setDescription('Entry containing COPS status for a particular interface. By default each interface has no roles. It then has a role combination that is the zero length string. Roles in a role combination for an interface are reported to the PDP by the PEP. An interface may have multiple roles. Adding/deleting roles results in changes to the role combination for an interface. Therefore, a new set of QoS policies will be used for the interface with the new role combination.')
ccopsIfRoleCombination = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 10, 1, 1), CopsRoleCombination()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccopsIfRoleCombination.setStatus('current')
if mibBuilder.loadTexts: ccopsIfRoleCombination.setDescription('A display string, role combination, that is associated with an interface. This is the administratively-desired role combination which represents roles that are currently set by the administrator for a particular interface in the COPS domain. If copsMaxRoleCombination is one, the new role will be applied to all interfaces which support COPS feature on the device. Agent returns inconsistentValue if this role does not exist in ccopsRoleTable, resourceUnavailable if the role combination exceeds copsMaxRoleCombination in the device, wrongValue if a non-lexicographically-ordered value is written to it. On some platforms, roles may be assigned per port group rather than per port. If multiple ports belong to a port group, the role combination assigned to any of the ports in such group will apply to all ports in the same group. On some platforms, there can be a single role combination for the entire device. The role combination assigned to any of the interfaces will apply to all interfaces which support COPS feature in the device.')
ccopsRoleConfigSupported = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 140, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccopsRoleConfigSupported.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleConfigSupported.setDescription('Indicates whether this device supports the ccopsMaxRole and ccopsRoleTable, and thereby, whether a role must be present in the ccopsRoleTable before it can be used within a value of ccopsIfRoleCombination.')
ccopsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 2))
ccopsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 3))
ccopsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1))
ccopsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2))
ccopsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1, 1)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsGlobalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsMIBCompliance = ccopsMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ccopsMIBCompliance.setDescription('The compliance statement for the CISCO-COPS-CLIENT-MIB.')
ccopsMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 1, 2)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsGlobalGroupRev2"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsMIBComplianceRev2 = ccopsMIBComplianceRev2.setStatus('current')
if mibBuilder.loadTexts: ccopsMIBComplianceRev2.setDescription('The compliance statement for the CISCO-COPS-CLIENT-MIB.')
ccopsGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 1)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsServerMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPriority"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPort"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigStatus"), ("CISCO-COPS-CLIENT-MIB", "ccopsInitialTimeout"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutIncrement"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsDomainName"), ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRole"), ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRoleCombination"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleStatus"), ("CISCO-COPS-CLIENT-MIB", "ccopsIfRoleCombination"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsGlobalGroup = ccopsGlobalGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ccopsGlobalGroup.setDescription('A collection of objects providing the COPS ability on the device. Devices implementing the COPS client feature should support this group.')
ccopsGlobalGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 2)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsServerMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPriority"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigPort"), ("CISCO-COPS-CLIENT-MIB", "ccopsServerConfigStatus"), ("CISCO-COPS-CLIENT-MIB", "ccopsInitialTimeout"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutIncrement"), ("CISCO-COPS-CLIENT-MIB", "ccopsTimeoutMax"), ("CISCO-COPS-CLIENT-MIB", "ccopsDomainName"), ("CISCO-COPS-CLIENT-MIB", "ccopsMaxRoleCombination"), ("CISCO-COPS-CLIENT-MIB", "ccopsIfRoleCombination"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleConfigSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsGlobalGroupRev2 = ccopsGlobalGroupRev2.setStatus('current')
if mibBuilder.loadTexts: ccopsGlobalGroupRev2.setDescription('A collection of objects providing the COPS ability on the device.')
ccopsRoleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 140, 3, 2, 3)).setObjects(("CISCO-COPS-CLIENT-MIB", "ccopsMaxRole"), ("CISCO-COPS-CLIENT-MIB", "ccopsRoleStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsRoleGroup = ccopsRoleGroup.setStatus('current')
if mibBuilder.loadTexts: ccopsRoleGroup.setDescription('A collection of objects which allow an agent to require a limited set of allowed roles be specified, and to reject any role-combination containing any other role.')
mibBuilder.exportSymbols("CISCO-COPS-CLIENT-MIB", ccopsIfRoleCombination=ccopsIfRoleCombination, ccopsMIBGroups=ccopsMIBGroups, ccopsInitialTimeout=ccopsInitialTimeout, ccopsDomainName=ccopsDomainName, ccopsDomainEntry=ccopsDomainEntry, ccopsServerConfigStatus=ccopsServerConfigStatus, ccopsRoleName=ccopsRoleName, CopsRole=CopsRole, ccopsServerConfigEntry=ccopsServerConfigEntry, ccopsServerMax=ccopsServerMax, ccopsRoleConfigSupported=ccopsRoleConfigSupported, ccopsServerConfigPriority=ccopsServerConfigPriority, ccopsMIBCompliances=ccopsMIBCompliances, ccopsMIBConformance=ccopsMIBConformance, ccopsServerConfigClientType=ccopsServerConfigClientType, ccopsRoleTable=ccopsRoleTable, ccopsMIBCompliance=ccopsMIBCompliance, ccopsServerConfigTable=ccopsServerConfigTable, ccopsRoleStatus=ccopsRoleStatus, ccopsIfEntry=ccopsIfEntry, PYSNMP_MODULE_ID=ciscoCopsClientMIB, ccopsRoleEntry=ccopsRoleEntry, ccopsDomainClientType=ccopsDomainClientType, CopsClientType=CopsClientType, ccopsGlobalGroupRev2=ccopsGlobalGroupRev2, ccopsRoleGroup=ccopsRoleGroup, ccopsGlobalObjects=ccopsGlobalObjects, ccopsDomainTable=ccopsDomainTable, CopsRoleCombination=CopsRoleCombination, ccopsServerConfigPort=ccopsServerConfigPort, ccopsMIBComplianceRev2=ccopsMIBComplianceRev2, ccopsTimeoutIncrement=ccopsTimeoutIncrement, ccopsMIBObjects=ccopsMIBObjects, ccopsMaxRole=ccopsMaxRole, ccopsMaxRoleCombination=ccopsMaxRoleCombination, ciscoCopsClientMIB=ciscoCopsClientMIB, ccopsIfTable=ccopsIfTable, CopsDomainName=CopsDomainName, ccopsTimeoutMax=ccopsTimeoutMax, ccopsMIBNotifications=ccopsMIBNotifications, ccopsServerConfigName=ccopsServerConfigName, ccopsGlobalGroup=ccopsGlobalGroup)
