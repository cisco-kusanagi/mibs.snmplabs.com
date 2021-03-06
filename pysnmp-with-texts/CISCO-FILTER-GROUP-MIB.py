#
# PySNMP MIB module CISCO-FILTER-GROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FILTER-GROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:58:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoIpProtocol, = mibBuilder.importSymbols("CISCO-TC", "CiscoIpProtocol")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Unsigned32, Integer32, ModuleIdentity, iso, NotificationType, Gauge32, MibIdentifier, IpAddress, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Integer32", "ModuleIdentity", "iso", "NotificationType", "Gauge32", "MibIdentifier", "IpAddress", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64")
StorageType, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "TextualConvention", "RowStatus", "DisplayString")
ciscoFilterGroupMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 474))
ciscoFilterGroupMIB.setRevisions(('2005-04-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFilterGroupMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFilterGroupMIB.setLastUpdated('200504270000Z')
if mibBuilder.loadTexts: ciscoFilterGroupMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoFilterGroupMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive, San Jose CA 95134-1706. USA Tel: +1 800 553-NETS E-mail: ip-acl@cisco.com')
if mibBuilder.loadTexts: ciscoFilterGroupMIB.setDescription('The MIB module is for creating and configuring object groups to support packet filtering and access control on IP and other protocols. The cfgFilterGroupTable allows users to create delete, and get information about filter groups. Filter groups are uniquely identified by the group names. Filter groups can either be of network, protocol, service and icmp and filter group type cannot be changed once it has been created. The cfgFilterNetworkGroupTable is used for managing information about IP Addresses. The cfgFilterIpProtocolGroupTable is used for managing information about protocols. The cfgFilterIpServiceGroupTable is used for managing information about services(ports). The cfgFilterICMPGroupTable is used for managing information about ICMP protocol. The cfgFilterNestedGroupTable is used for supporting nesting of filter groups(i.e configuring filter groups inside the other filter groups). Terminologies used: ICMP - Internet Control Message Protocol.')
ciscoFilterGroupMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 474, 0))
ciscoFilterGroupMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 474, 1))
ciscoFilterGroupMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 474, 2))
cfgFilterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1))
class CfgFilterGroupName(TextualConvention, OctetString):
    description = 'This textual convention defines the filter group. Filter group provides a name for combining multiple types of objects of same category. The object value shall be an alphanumeric string.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

cfgFilterGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1), )
if mibBuilder.loadTexts: cfgFilterGroupTable.setStatus('current')
if mibBuilder.loadTexts: cfgFilterGroupTable.setDescription('This table is used for creating/deleting filter groups. A filter group allows grouping of filter objects of same type. Filter group is identified by a name and this group can be used in other tables to simplify filter creation. Filter objects are Internet addresses, Internet Address masks, protocols, ports(services) and ICMP types.')
cfgFilterGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"))
if mibBuilder.loadTexts: cfgFilterGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cfgFilterGroupEntry.setDescription('An entry in filter group table. Each entry contains information such as filter group type, filter description.')
cfgFilterGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 1), CfgFilterGroupName())
if mibBuilder.loadTexts: cfgFilterGroupName.setStatus('current')
if mibBuilder.loadTexts: cfgFilterGroupName.setDescription('This object identifies unique name for the filter group.')
cfgFilterGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("network", 1), ("ipProtocol", 2), ("ipService", 3), ("icmp", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterGroupType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterGroupType.setDescription("This object identifies the type of the filter group. The possible values are: network (1) : specifies network group. This group contains information on the IP address and address mask. This information is available in cfgFilterNetworkGroupTable. ipProtocol (2) : specifies IP protocol group. This group contains protocol value. This information is available in cfgFilterIpProtocolGroupTable. ipService (3) : specifies IP service group. This group contains information on UDP/TCP port. This information is available in cfgFilterIpServiceGroupTable. icmp (4) : specifies the ICMP group. This group contains information on ICMP Message Type and ICMP message code. This information is available in cfgFilterICMPGroupTable. The value of this object cannot be changed when cfgFilterGroupRowStatus is 'active'.")
cfgFilterGroupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterGroupDescription.setStatus('current')
if mibBuilder.loadTexts: cfgFilterGroupDescription.setDescription('This object is used for configuring description for the filter group.')
cfgFilterGroupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterGroupStorageType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterGroupStorageType.setDescription('The storage type for this conceptual row.')
cfgFilterGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfgFilterGroupRowStatus.setDescription("This object is used for adding/deleting entries in this table. This object can be set to 'active' only if cfgFilterGroupType is configured for the row.")
cfgFilterNetworkGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2), )
if mibBuilder.loadTexts: cfgFilterNetworkGroupTable.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNetworkGroupTable.setDescription("This table is used for adding/deleting network filter group. A network filter group is used to specify host IP addresses or subnet ranges. This is applicable only for the cfgFilterGroupType value of 'network'.")
cfgFilterNetworkGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"), (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkGroupIndex"))
if mibBuilder.loadTexts: cfgFilterNetworkGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNetworkGroupEntry.setDescription('An entry in network filter group table. Each entry contains information on the IP address and the mask value that can be used in filtering the packet. Multiple entries with the same value of cfgFilterGroupName belong to the same network filter group.')
cfgFilterNetworkGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfgFilterNetworkGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNetworkGroupIndex.setDescription('This object identifies an unique entry for a network filter group.')
cfgFilterNetworkAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterNetworkAddressType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNetworkAddressType.setDescription("This is the internet address type of for the cfgFilterNetworkAddress and cfgFilterNetworkMask. The value of this object cannot be changed when cfgFilterGroupRowStatus is 'active'.")
cfgFilterNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 3), InetAddress().clone('0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterNetworkAddress.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNetworkAddress.setDescription('The source/destination internet address to be configured. A value of zero causes all source/destination address to match in an IP filter where this group is used. The object value has to be consistent with the type specified in cfgFilterNetworkAddressType.')
cfgFilterNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 4), InetAddress().clone(hexValue="ffffffff")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterNetworkMask.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNetworkMask.setDescription("This is the wild card mask for the cfgFilterNetworkAddress bits that must match. Presence of 0 bits in the mask indicate that corresponding bits in the cfgFilterNetworkAddress must match in order for the matching to be successful, and 1 bits are don't care bits in the matching. A value of zero causes only IP packets of source and destination address the same as cfgFilterNetworkAddress to match. This object value has to be consistent with the type specified in cfgFilterNetworkAddressType.")
cfgFilterNetworkStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterNetworkStorageType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNetworkStorageType.setDescription('The storage type for this conceptual row.')
cfgFilterNetworkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterNetworkRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNetworkRowStatus.setDescription("This object is used for adding/deleting entries in this table. This object can be set to 'active' only with valid value for cfgFilterNetworkAddressType object.")
cfgFilterIpProtocolGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3), )
if mibBuilder.loadTexts: cfgFilterIpProtocolGroupTable.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpProtocolGroupTable.setDescription("This table is used for adding/deleting protocol filter group. A protocol filter group is used to specify protocol(s). This is applicable only for the cfgFilterGroupType value of 'ipProtocol'.")
cfgFilterIpProtocolGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"), (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterIpProtocolGroupIndex"))
if mibBuilder.loadTexts: cfgFilterIpProtocolGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpProtocolGroupEntry.setDescription('Each entry is an IP Protocol traffic filter within an IP filter profile. Entries with the same cfgFilterGroupName belong to the same protocol filter group.')
cfgFilterIpProtocolGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfgFilterIpProtocolGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpProtocolGroupIndex.setDescription('This index uniquely identifies the entries in this table.')
cfgFilterIpProtocolNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1, 2), CiscoIpProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterIpProtocolNumber.setReference('RFC-790, ASSIGNED NUMBERS, September 1981, Section INTERNET PROTOCOL NUMBERS.')
if mibBuilder.loadTexts: cfgFilterIpProtocolNumber.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpProtocolNumber.setDescription("This object identifies the internet protocol number in the packets. These IP protocol numbers are defined in the Network Group Request For Comments(RFC) documents. For example, Cisco commonly used protocol includes: 1 - Internet Control Message Protocol (ICMP) 2 - Internet Gateway Message Protocol (IGMP) 4 - IP in IP tunneling 6 - Transmission Control Protocol (TCP) 9 - Cisco's IGRP routing protocol (IGRP) 17 - User Datagram Protocol (UDP) 47 - Cisco's GRE tunneling (GRE) 50 - Encapsulation Security Payload 51 - Authentication Header Protocol 88 - Cisco's EIGRP routing protocol 89 - OSPF routing protocol 94 - KA9Q NOS compatible IP over IP tunneling 103 - Protocol Independent Multicast 108 - Payload Compression Protocol.")
cfgFilterIpProtocolStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterIpProtocolStorageType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpProtocolStorageType.setDescription('The storage type for this conceptual row.')
cfgFilterIpProtocolGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterIpProtocolGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpProtocolGroupRowStatus.setDescription("This object is used for adding/deleting entries in this table. This object can be set to 'active' only with valid value for cfgFilterIpProtocolNumber object.")
cfgFilterIpServiceGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4), )
if mibBuilder.loadTexts: cfgFilterIpServiceGroupTable.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpServiceGroupTable.setDescription("This table is used for adding/deleting service filter group. A service filter group is used to specify specific or ranges of TCP/UDP ports to be defined. This filter group can be used as either the source port(s) or destination port(s) in the associated cfgFilterExtTable. This is applicable only for the cfgFilterGroupType value of 'ipService'.")
cfgFilterIpServiceGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"), (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterIpServiceGroupIndex"))
if mibBuilder.loadTexts: cfgFilterIpServiceGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpServiceGroupEntry.setDescription('Each entry is an IP Protocol traffic filter within an IP filter profile. Entries with the same cfgFilterGroupName belong to the same protocol filter group.')
cfgFilterIpServiceGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfgFilterIpServiceGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpServiceGroupIndex.setDescription('This index uniquely identifies the entries in this table.')
cfgFilterIpServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tcp", 1), ("udp", 2), ("tcpUdp", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterIpServiceType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpServiceType.setDescription('This object identifies the protocol type of the port for this group. The possible value(s) are : tcp(1) : TCP port. udp(2) : UDP port. tcpUdp(3) : TCP/UDP port. This value is applicable for a port which is same for both TCP and UDP.')
cfgFilterIpServicePortLow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 3), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterIpServicePortLow.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpServicePortLow.setDescription('This object identifies the source or destination port number. This is the inclusive lower bound of the transport-layer source/destination port range that is to be matched in the filter where this group is defined. This value must be equal to or less than the value specified for this entry in cfgFilterServicePortHigh.')
cfgFilterIpServicePortHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 4), InetPortNumber().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterIpServicePortHigh.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpServicePortHigh.setDescription("This object identifies the source or destination port number. This is the inclusive upper bound of the transport-layer source/destination port range that is to be matched in the filter where this group is defined. This value must be equal to or greater than the value specified for this entry in cfgFilterServicePortLow. If this value is '0', the udp or tcp port number is ignored during matching.")
cfgFilterIpServiceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterIpServiceStorageType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpServiceStorageType.setDescription('The storage type for this conceptual row.')
cfgFilterIpServiceGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterIpServiceGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfgFilterIpServiceGroupRowStatus.setDescription("This object is used for adding/deleting entries in this table. This object can be set to 'active' only with valid value for cfgFilterIpServiceType object.")
cfgFilterICMPGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5), )
if mibBuilder.loadTexts: cfgFilterICMPGroupTable.setStatus('current')
if mibBuilder.loadTexts: cfgFilterICMPGroupTable.setDescription("This table contains lists of filters for ICMP Type filter group. An ICMP Type filter group can be configured with multiple entries each representing the ICMP message types and ICMP message code. This is applicable only for the cfgFilterGroupType value of 'icmp'.")
cfgFilterICMPGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-FILTER-GROUP-MIB", "cfgFilterGroupName"), (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterICMPGroupIndex"))
if mibBuilder.loadTexts: cfgFilterICMPGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cfgFilterICMPGroupEntry.setDescription('An entry in ICMP filter group table. Each entry contains information on the ICMP message type and ICMP code. Multiple Entries with the same value of cfgFilterGroupName belong to the same ICMP filter group.')
cfgFilterICMPGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfgFilterICMPGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cfgFilterICMPGroupIndex.setDescription('This index identifies an unique entry in this table.')
cfgFilterICMPType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 255)).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterICMPType.setReference('RFC-792 INTERNET CONTROL MESSAGE PROTOCOL')
if mibBuilder.loadTexts: cfgFilterICMPType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterICMPType.setDescription("This object specifies the ICMP message type to be configured in ICMP filter group. Setting this object to '-1' will make the filtering match any ICMP message type. Some of the commonly used ICMP Message types are: 0 - Echo Reply 3 - Destination Unreachable 4 - Source Quench 5 - Redirect 8 - Echo 11 - Time Exceeded 12 - Parameter Problem 13 - Timestamp 14 - Timestamp Reply 15 - Information Request 16 - Information Reply 17 - Mask Request 18 - Mask Reply 31 - Conversion Error 32 - Mobile Redirect.")
cfgFilterICMPCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 255)).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterICMPCode.setReference('RFC-792 INTERNET CONTROL MESSAGE PROTOCOL')
if mibBuilder.loadTexts: cfgFilterICMPCode.setStatus('current')
if mibBuilder.loadTexts: cfgFilterICMPCode.setDescription("This object specifies the ICMP message code to be configured in ICMP filter group. Setting this object to '-1' will make the filtering match any ICMP code.")
cfgFilterICMPStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterICMPStorageType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterICMPStorageType.setDescription('The storage type for this conceptual row.')
cfgFilterICMPGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterICMPGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfgFilterICMPGroupRowStatus.setDescription("This object is used for adding/deleting entries in this table. This object can be set to 'active' only with valid value for cfgFilterICMPType object.")
cfgFilterNestedGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6), )
if mibBuilder.loadTexts: cfgFilterNestedGroupTable.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNestedGroupTable.setDescription('This table contains lists of filter groups that are configured in other filter group. This table is used for configuring a group as member of another group.')
cfgFilterNestedGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-FILTER-GROUP-MIB", "cfgFilterParentGroupName"), (0, "CISCO-FILTER-GROUP-MIB", "cfgFilterNestedGroupName"))
if mibBuilder.loadTexts: cfgFilterNestedGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNestedGroupEntry.setDescription('An entry in nested filter group table. Each entry contains information on the a group that is configured in another group.')
cfgFilterParentGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1, 1), CfgFilterGroupName())
if mibBuilder.loadTexts: cfgFilterParentGroupName.setStatus('current')
if mibBuilder.loadTexts: cfgFilterParentGroupName.setDescription('This object identifies the filter group that is previously created and to which another filter group identified by cfgFilterNestedGroupName will be added. The value for this object must correspond to entry in cfgFilterGroupTable.')
cfgFilterNestedGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1, 2), CfgFilterGroupName())
if mibBuilder.loadTexts: cfgFilterNestedGroupName.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNestedGroupName.setDescription('This object identifies the filter group that is previously created and is being added to another filter group identified by cfgFilterParentGroupName. The value for this object must correspond to entry in cfgFilterGroupTable. The value for this object should not be same as the value of cfgFilterParentGroupName. The value for this object must be unique amongst the multiple instances with the same value of cfgFilterParentGroupName.')
cfgFilterNestedStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterNestedStorageType.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNestedStorageType.setDescription('The storage type for this conceptual row.')
cfgFilterNestedGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 1, 6, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfgFilterNestedGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfgFilterNestedGroupRowStatus.setDescription('This object is used for adding/deleting entries in this table.')
ciscoFilterGroupMIBCompl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 474, 2, 1))
ciscoFilterGroupMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 474, 2, 2))
ciscoFilterGroupConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 474, 2, 1, 1)).setObjects(("CISCO-FILTER-GROUP-MIB", "ciscoFilterObjectGroup"), ("CISCO-FILTER-GROUP-MIB", "ciscoFilterNetworkGroup"), ("CISCO-FILTER-GROUP-MIB", "ciscoFilterIpProtocolGroup"), ("CISCO-FILTER-GROUP-MIB", "ciscoFilterIpServiceGroup"), ("CISCO-FILTER-GROUP-MIB", "ciscoFilterICMPGroup"), ("CISCO-FILTER-GROUP-MIB", "ciscoFilterNestedGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFilterGroupConfigMIBCompliance = ciscoFilterGroupConfigMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoFilterGroupConfigMIBCompliance.setDescription('The compliance statement for entities implementing the Cisco IP Protocol Filter MIB.')
ciscoFilterObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 2)).setObjects(("CISCO-FILTER-GROUP-MIB", "cfgFilterGroupType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterGroupDescription"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterGroupStorageType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFilterObjectGroup = ciscoFilterObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFilterObjectGroup.setDescription('Configuration parameters for filter groups.')
ciscoFilterNetworkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 3)).setObjects(("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkAddressType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkAddress"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkMask"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkStorageType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterNetworkRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFilterNetworkGroup = ciscoFilterNetworkGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFilterNetworkGroup.setDescription('Configuration parameters for network filters.')
ciscoFilterIpProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 4)).setObjects(("CISCO-FILTER-GROUP-MIB", "cfgFilterIpProtocolNumber"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpProtocolStorageType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpProtocolGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFilterIpProtocolGroup = ciscoFilterIpProtocolGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFilterIpProtocolGroup.setDescription('Configuration parameters for protocol filters.')
ciscoFilterIpServiceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 5)).setObjects(("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServiceType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServicePortLow"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServicePortHigh"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServiceStorageType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterIpServiceGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFilterIpServiceGroup = ciscoFilterIpServiceGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFilterIpServiceGroup.setDescription('Configuration parameters for port filters.')
ciscoFilterICMPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 6)).setObjects(("CISCO-FILTER-GROUP-MIB", "cfgFilterICMPType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterICMPCode"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterICMPStorageType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterICMPGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFilterICMPGroup = ciscoFilterICMPGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFilterICMPGroup.setDescription('Configuration parameters related to ICMP filter group.')
ciscoFilterNestedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 474, 1, 7)).setObjects(("CISCO-FILTER-GROUP-MIB", "cfgFilterNestedStorageType"), ("CISCO-FILTER-GROUP-MIB", "cfgFilterNestedGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFilterNestedGroup = ciscoFilterNestedGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoFilterNestedGroup.setDescription('Configuration parameters related to nesting of filter group.')
mibBuilder.exportSymbols("CISCO-FILTER-GROUP-MIB", cfgFilterNetworkMask=cfgFilterNetworkMask, cfgFilterGroupName=cfgFilterGroupName, cfgFilterParentGroupName=cfgFilterParentGroupName, ciscoFilterGroupMIBNotifs=ciscoFilterGroupMIBNotifs, cfgFilterNestedGroupTable=cfgFilterNestedGroupTable, cfgFilterGroupDescription=cfgFilterGroupDescription, cfgFilterICMPGroupRowStatus=cfgFilterICMPGroupRowStatus, ciscoFilterGroupMIB=ciscoFilterGroupMIB, cfgFilterGroupType=cfgFilterGroupType, cfgFilterIpProtocolGroupIndex=cfgFilterIpProtocolGroupIndex, cfgFilterIpProtocolNumber=cfgFilterIpProtocolNumber, cfgFilterICMPGroupEntry=cfgFilterICMPGroupEntry, ciscoFilterIpServiceGroup=ciscoFilterIpServiceGroup, CfgFilterGroupName=CfgFilterGroupName, cfgFilterNetworkAddress=cfgFilterNetworkAddress, cfgFilterIpProtocolGroupEntry=cfgFilterIpProtocolGroupEntry, cfgFilterICMPGroupIndex=cfgFilterICMPGroupIndex, ciscoFilterGroupMIBConform=ciscoFilterGroupMIBConform, cfgFilterNestedGroupName=cfgFilterNestedGroupName, cfgFilterICMPGroupTable=cfgFilterICMPGroupTable, ciscoFilterNestedGroup=ciscoFilterNestedGroup, cfgFilterIpServiceGroupTable=cfgFilterIpServiceGroupTable, ciscoFilterGroupConfigMIBCompliance=ciscoFilterGroupConfigMIBCompliance, ciscoFilterGroupMIBObjects=ciscoFilterGroupMIBObjects, ciscoFilterObjectGroup=ciscoFilterObjectGroup, cfgFilterICMPType=cfgFilterICMPType, cfgFilterNetworkGroupEntry=cfgFilterNetworkGroupEntry, cfgFilterIpServiceType=cfgFilterIpServiceType, cfgFilterGroupEntry=cfgFilterGroupEntry, cfgFilterIpServiceGroupEntry=cfgFilterIpServiceGroupEntry, ciscoFilterICMPGroup=ciscoFilterICMPGroup, cfgFilterNetworkGroupTable=cfgFilterNetworkGroupTable, cfgFilterNetworkRowStatus=cfgFilterNetworkRowStatus, cfgFilterIpProtocolStorageType=cfgFilterIpProtocolStorageType, cfgFilterIpServicePortHigh=cfgFilterIpServicePortHigh, ciscoFilterIpProtocolGroup=ciscoFilterIpProtocolGroup, cfgFilterNetworkGroupIndex=cfgFilterNetworkGroupIndex, PYSNMP_MODULE_ID=ciscoFilterGroupMIB, cfgFilterConfig=cfgFilterConfig, cfgFilterGroupRowStatus=cfgFilterGroupRowStatus, cfgFilterIpProtocolGroupTable=cfgFilterIpProtocolGroupTable, cfgFilterIpServiceGroupIndex=cfgFilterIpServiceGroupIndex, cfgFilterGroupTable=cfgFilterGroupTable, cfgFilterIpServicePortLow=cfgFilterIpServicePortLow, cfgFilterICMPCode=cfgFilterICMPCode, cfgFilterNestedStorageType=cfgFilterNestedStorageType, ciscoFilterGroupMIBCompl=ciscoFilterGroupMIBCompl, ciscoFilterNetworkGroup=ciscoFilterNetworkGroup, cfgFilterGroupStorageType=cfgFilterGroupStorageType, ciscoFilterGroupMIBGroups=ciscoFilterGroupMIBGroups, cfgFilterIpServiceGroupRowStatus=cfgFilterIpServiceGroupRowStatus, cfgFilterNestedGroupEntry=cfgFilterNestedGroupEntry, cfgFilterICMPStorageType=cfgFilterICMPStorageType, cfgFilterIpProtocolGroupRowStatus=cfgFilterIpProtocolGroupRowStatus, cfgFilterNestedGroupRowStatus=cfgFilterNestedGroupRowStatus, cfgFilterIpServiceStorageType=cfgFilterIpServiceStorageType, cfgFilterNetworkAddressType=cfgFilterNetworkAddressType, cfgFilterNetworkStorageType=cfgFilterNetworkStorageType)
