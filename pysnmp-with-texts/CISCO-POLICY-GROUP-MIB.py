#
# PySNMP MIB module CISCO-POLICY-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-POLICY-GROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:08:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ObjectIdentity, ModuleIdentity, Integer32, Unsigned32, iso, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, NotificationType, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "ModuleIdentity", "Integer32", "Unsigned32", "iso", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "NotificationType", "TimeTicks", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoPolicyGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 507))
ciscoPolicyGroupMIB.setRevisions(('2006-01-13 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setRevisionsDescriptions(('Initial revision of this MIB module.',))
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setLastUpdated('200601131600Z')
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPolicyGroupMIB.setDescription('The MIB module is for configuration of policy and policy group. A policy group can be described as a set of entities identified by IP addresses or other means. Members of a policy group will be subjected to the same policy. In this MIB, user can apply a policy to policy group(s) as well as configure and retrieve the group membership.')
class CpgPolicyName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form, describes the name of a policy.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CpgPolicyNameOrEmpty(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the CpgPolicyName convention. The latter defines a non-empty policy name. This extension permits the additional value of empty string.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CpgGroupName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form, describes the name of a policy group.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

ciscoPolicyGroupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 0))
ciscoPolicyGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 1))
ciscoPolicyGroupMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 2))
cpgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1))
cpgPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2))
cpgGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1), )
if mibBuilder.loadTexts: cpgGroupTable.setStatus('current')
if mibBuilder.loadTexts: cpgGroupTable.setDescription('A table indicates the policy groups in the device.')
cpgGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1), ).setIndexNames((1, "CISCO-POLICY-GROUP-MIB", "cpgGroupName"))
if mibBuilder.loadTexts: cpgGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cpgGroupEntry.setDescription('A row instance contains the name of a policy group, the source method which creates this group, the number of IP addresses contained in the group and the status of this instance. A row instance can be created or removed by the system or by setting the appropriate value of the RowStatus object.')
cpgGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 1), CpgGroupName())
if mibBuilder.loadTexts: cpgGroupName.setStatus('current')
if mibBuilder.loadTexts: cpgGroupName.setDescription('Indicates the name of a policy group in the device.')
cpgGroupSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("accessList", 2), ("configured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgGroupSourceType.setStatus('current')
if mibBuilder.loadTexts: cpgGroupSourceType.setDescription('Indicates the source i.e. the method used to create this group. unknown(1) indicates that the source of this group cannot be identified. accessList(2) indicates that this group is added via the ACL (Access Control List) feature. configured(3) indicates that this group is added via this policy group configuration.')
cpgGroupIpAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgGroupIpAddrCount.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpAddrCount.setDescription('Indicates the number of IP address(es) contained in this group. This is the number of entries for this group in the cpgGroupIpTable. The initial value of this object in a row created via cpgGroupRowStatus object is zero.')
cpgGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cpgGroupRowStatus.setDescription('This object is used to manage the creation and deletion of rows in this table.')
cpgGroupIpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2), )
if mibBuilder.loadTexts: cpgGroupIpTable.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpTable.setDescription('A table provides management information for policy group and its IP address(es) membership in the device.')
cpgGroupIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpGroupName"), (0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddrType"), (0, "CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddress"))
if mibBuilder.loadTexts: cpgGroupIpEntry.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpEntry.setDescription('A row instance contains the IP address mask, source type and its status. A row instance can be created or removed by the system or by setting the appropriate value of its RowStatus object. A row instance is indexed by a group name, type and value of an IP address. The group name index must exist in the cpgGroupTable. If a group name is deleted from cpgGroupTable, entries in this table using this group as an index will also be automatically removed.')
cpgGroupIpGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 1), CpgGroupName())
if mibBuilder.loadTexts: cpgGroupIpGroupName.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpGroupName.setDescription('Indicates the policy group name. This group should exist in cpgGroupTable.')
cpgGroupIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: cpgGroupIpAddrType.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpAddrType.setDescription('The type of Internet address of a group member.')
cpgGroupIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cpgGroupIpAddress.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpAddress.setDescription('The Internet address of a group member. The type of this address is determined by the value of the cpgGroupIpAddrType object. The cpgGroupIpAddress may not be empty due to the SIZE restriction.')
cpgGroupIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 4), InetAddress().clone(hexValue="FFFFFFFF")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgGroupIpMask.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpMask.setDescription("Specifies the mask to be logical-ANDed with the IP address denoted in cpgGroupIpAddress object to indicate IP address group membership. The type of this mask is determined by the value of the cpgGroupIpAddrType object. Value of this object can not be modified when the corresponding instance of cpgGroupIpRowStatus is 'active'.")
cpgGroupIpSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("configured", 2), ("dot1x", 3), ("nac", 4), ("webAuth", 5), ("macAuth", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgGroupIpSourceType.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpSourceType.setDescription('Indicates the source of this IP address. other(1) indicates the source of this IP address is not one of the following types. configured(2) indicates this IP address is configured via this policy group and IP address configuration. dot1x(3) indicates this IP address is added by 802.1x feature. nac(4) indicates this IP address is added by NAC (network admission control) feature. webAuth(5) indicates this IP address is added by Web-Proxy Authentication feature. macAuth(6) indicatest this IP address is added by MAC Authentication Bypass feature.')
cpgGroupIpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgGroupIpRowStatus.setStatus('current')
if mibBuilder.loadTexts: cpgGroupIpRowStatus.setDescription("This object is used to manage the creation and deletion of rows in this table. Once a row becomes active, values within this row cannot be modified, except by setting this object value to 'notInService' first, or deleting and re-creating it. A conceptual row can be removed by setting this object value to 'destroy' if and only if the value of corresponding instance of cpgGroupIpSourceType is 'configured'.")
cpgPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1), )
if mibBuilder.loadTexts: cpgPolicyTable.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyTable.setDescription('A table describes the policies in the device.')
cpgPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1), ).setIndexNames((1, "CISCO-POLICY-GROUP-MIB", "cpgPolicyName"))
if mibBuilder.loadTexts: cpgPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyEntry.setDescription('A row instance contains the name of a policy in the device.')
cpgPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1, 1), CpgPolicyName())
if mibBuilder.loadTexts: cpgPolicyName.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyName.setDescription('Indicates a policy name in the device.')
cpgPolicyGroupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpgPolicyGroupCount.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupCount.setDescription('Indicates the number of policy group(s) associated with this policy. This is the number of entries for this policy in the cpgPolicyGroupTable.')
cpgPolicyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2), )
if mibBuilder.loadTexts: cpgPolicyGroupTable.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupTable.setDescription('A table provides the mechanism to configure association between a policy and a policy group. When a policy associates with a policy group, this policy is applied to all the members of the group. A policy can associate with multiple groups and vice versa.')
cpgPolicyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupPolicyName"), (1, "CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupGroupName"))
if mibBuilder.loadTexts: cpgPolicyGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupEntry.setDescription('A row instance contains the RowStatus object to configure the association between a policy and a policy group. A row instance can be created or removed by the system or by setting the appropriate value of the RowStatus object. A row instance is indexed by a policy name and a policy group name. The policy name index must exist in cpgPolicyTable. The policy group name index must exist in cpgGroupTable. If a policy group is removed from cpgGroupTable, entries in this table using this group as an index will be automatically removed.')
cpgPolicyGroupPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 1), CpgPolicyName())
if mibBuilder.loadTexts: cpgPolicyGroupPolicyName.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupPolicyName.setDescription('This object indicates the policy name used to associate to the group denoted by cpgPolicyGroupGroupName. This policy must exist in cpgPolicyTable.')
cpgPolicyGroupGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 2), CpgGroupName())
if mibBuilder.loadTexts: cpgPolicyGroupGroupName.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupGroupName.setDescription('This object indicates the group name used to associate to the policy denoted by cpgPolicyGroupPolicyName. This group must exist in cpgGroupTable.')
cpgPolicyGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 507, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpgPolicyGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cpgPolicyGroupRowStatus.setDescription('This object is used to manage the creation and deletion of rows in this table.')
ciscoPolicyGroupMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 1))
ciscoPolicyGroupMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2))
ciscoPolicyGroupMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 1, 1)).setObjects(("CISCO-POLICY-GROUP-MIB", "ciscoCpgPolicyInfoGroup"), ("CISCO-POLICY-GROUP-MIB", "ciscoCpgGroupInfoGroup"), ("CISCO-POLICY-GROUP-MIB", "ciscoCpgGroupIpInfoGroup"), ("CISCO-POLICY-GROUP-MIB", "ciscoCpgPolicyGroupInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupMIBCompliance = ciscoPolicyGroupMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoPolicyGroupMIBCompliance.setDescription('The compliance statement for the CISCO-POLICY-GROUP-MIB')
ciscoCpgGroupInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 1)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgGroupSourceType"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpAddrCount"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgGroupInfoGroup = ciscoCpgGroupInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCpgGroupInfoGroup.setDescription('A collection of objects which provides information on policy groups in the device.')
ciscoCpgGroupIpInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 2)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgGroupIpMask"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpSourceType"), ("CISCO-POLICY-GROUP-MIB", "cpgGroupIpRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgGroupIpInfoGroup = ciscoCpgGroupIpInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCpgGroupIpInfoGroup.setDescription('A collection of objects which provides information on policy group and IP addresses membership.')
ciscoCpgPolicyInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 3)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgPolicyInfoGroup = ciscoCpgPolicyInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCpgPolicyInfoGroup.setDescription('A collection of objects which provides the policies data in the device.')
ciscoCpgPolicyGroupInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 507, 2, 2, 4)).setObjects(("CISCO-POLICY-GROUP-MIB", "cpgPolicyGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCpgPolicyGroupInfoGroup = ciscoCpgPolicyGroupInfoGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCpgPolicyGroupInfoGroup.setDescription('A collection of object which provides information on group and policy association.')
mibBuilder.exportSymbols("CISCO-POLICY-GROUP-MIB", ciscoCpgPolicyInfoGroup=ciscoCpgPolicyInfoGroup, ciscoCpgGroupInfoGroup=ciscoCpgGroupInfoGroup, cpgPolicyGroupPolicyName=cpgPolicyGroupPolicyName, cpgGroupName=cpgGroupName, ciscoPolicyGroupMIB=ciscoPolicyGroupMIB, ciscoPolicyGroupMIBConformance=ciscoPolicyGroupMIBConformance, ciscoPolicyGroupMIBCompliances=ciscoPolicyGroupMIBCompliances, PYSNMP_MODULE_ID=ciscoPolicyGroupMIB, cpgPolicyGroupCount=cpgPolicyGroupCount, CpgGroupName=CpgGroupName, ciscoPolicyGroupMIBNotifs=ciscoPolicyGroupMIBNotifs, cpgPolicyName=cpgPolicyName, ciscoCpgGroupIpInfoGroup=ciscoCpgGroupIpInfoGroup, cpgGroupIpGroupName=cpgGroupIpGroupName, cpgGroupIpSourceType=cpgGroupIpSourceType, cpgGroupIpAddrType=cpgGroupIpAddrType, cpgGroupTable=cpgGroupTable, cpgPolicyGroupTable=cpgPolicyGroupTable, cpgGroupIpMask=cpgGroupIpMask, cpgGroupIpAddrCount=cpgGroupIpAddrCount, ciscoCpgPolicyGroupInfoGroup=ciscoCpgPolicyGroupInfoGroup, CpgPolicyNameOrEmpty=CpgPolicyNameOrEmpty, cpgPolicyTable=cpgPolicyTable, ciscoPolicyGroupMIBObjects=ciscoPolicyGroupMIBObjects, cpgGroup=cpgGroup, ciscoPolicyGroupMIBCompliance=ciscoPolicyGroupMIBCompliance, cpgGroupIpEntry=cpgGroupIpEntry, cpgPolicyGroupGroupName=cpgPolicyGroupGroupName, cpgGroupIpRowStatus=cpgGroupIpRowStatus, cpgGroupIpTable=cpgGroupIpTable, ciscoPolicyGroupMIBGroups=ciscoPolicyGroupMIBGroups, cpgGroupSourceType=cpgGroupSourceType, cpgPolicy=cpgPolicy, cpgPolicyGroupRowStatus=cpgPolicyGroupRowStatus, cpgGroupIpAddress=cpgGroupIpAddress, CpgPolicyName=CpgPolicyName, cpgGroupRowStatus=cpgGroupRowStatus, cpgPolicyGroupEntry=cpgPolicyGroupEntry, cpgGroupEntry=cpgGroupEntry, cpgPolicyEntry=cpgPolicyEntry)
