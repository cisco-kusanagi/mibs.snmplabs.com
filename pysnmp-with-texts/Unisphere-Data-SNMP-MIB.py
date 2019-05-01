#
# PySNMP MIB module Unisphere-Data-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SNMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:32:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, TimeTicks, Counter32, NotificationType, ModuleIdentity, Gauge32, Bits, iso, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "TimeTicks", "Counter32", "NotificationType", "ModuleIdentity", "Gauge32", "Bits", "iso", "Counter64", "IpAddress")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdEnable, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdEnable")
usdSnmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16))
usdSnmpMIB.setRevisions(('2002-08-15 20:18', '2002-08-14 19:09', '2001-11-07 17:09', '2001-11-07 15:00', '2001-05-08 12:06', '2000-08-02 00:00', '2000-05-09 00:00', '1999-02-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdSnmpMIB.setRevisionsDescriptions(('Added support for SNMPv3 trap.', 'Added support for proxy enable/disable feature. Added support for the VRRP trap catagory.', 'Added support for interface compress. New textual convention: UsdSnmpIntfCompRestrictedMask New objects: usdSnmpIntfCompCompressed usdSnmpIntfCompEnhanced usdSnmpIntfCompEnhancedDisplay usdSnmpIntfCompRestricted usdSnmpIntfCompRestrictedDisplay Obsoleted object: usdSnmpInterfaceMode Added support for trap severities and trap severity filtering at the global and host levels. New textual convention: UsdTrapSeverity New objects: usdSnmpTrapHostDiscards usdSnmpTrapHostSeverityFilter usdSnmpTrapTrapSeverity usdSnmpTrapGlobalDiscards usdSnmpTrapGlobalSeverityFilter', 'Added support for DVMRP and local address pool and ATM ping trap categories.', 'Make it SMIv2 conformant.', 'Added usdSnmpInterfaceMode.', 'Added View support. Added Named Access List support.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: usdSnmpMIB.setLastUpdated('200208152018Z')
if mibBuilder.loadTexts: usdSnmpMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: usdSnmpMIB.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 Email: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdSnmpMIB.setDescription('MIB objects for configuring SNMP-based management access into Juniper routing switch products.')
class UsdSnmpCommunityName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    description = 'An SNMP community name. Represents textual information taken from the NVT ASCII character set. The character repertoire of the string is restricted to printable, non-whitespace characters.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class UsdSnmpAccessListName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    description = 'An IP Access List name. Represents textual information taken from the NVT ASCII character set. The character repertoire of the string is restricted to printable, non-whitespace characters.'
    status = 'current'
    displayHint = '31a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class UsdSnmpTrapMask(TextualConvention, OctetString):
    description = 'This octet string is interpreted as a bit mask, in which each bit corresponds to a category of SNMP trap. Bit definitions are as follows, where bit 31 is the most significant bit of the first octet, and bit 0 is the least significant bit of the fourth octet: Bit Category ----- ----------------------------------------------- 0 SNMP standard coldStart/warmStart/authenticationFailure traps 1 Standard linkUp/linkDown traps 2 Platform inventory traps 3 Environment (power, temperature, fan and memory) traps 4 Accounting (bulk statistics) traps 5 File transfer status trap 6 BGP traps 7 Log configuration traps 8 CLI security alert trap 9 Ping traps 10 OSPF traps 11 TraceRoute traps 12 Standard DVMRP traps 13 Proprietary DVMRP trap 14 Local address pool traps 15 ATM ping traps 16 VRRP traps 17-31 Undefined.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class UsdTrapSeverity(TextualConvention, Integer32):
    description = 'The set of trap severity values:'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("trapEmergency", 0), ("trapAlert", 1), ("trapCritical", 2), ("trapError", 3), ("trapWarning", 4), ("trapNotice", 5), ("trapInformational", 6), ("trapDebug", 7))

class UsdSnmpIntfCompRestrictedMask(TextualConvention, OctetString):
    description = "This octet string is interpreted as a bit mask, in which each bit corresponds to an interface restriction. The DESCRIPTION clause of a MIB object having this SYNTAX should specify the semantics of bit values '1' and '0'. Bit definitions are as follows, where bit 31 is the most significant bit of the first octet, and bit 0 is the least significant bit of the fourth octet: Bit interface restriction ----- ----------------------------------------------- 0 ifAdminStatus Down 1-31 Undefined."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

usdSnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1))
usdSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2))
usdSnmpGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1))
usdSnmpInterfaceCompress = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3))
usdSnmpCommunity = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2))
usdSnmpTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3))
usdSnmpAuthFailId = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4))
usdSnmpMaxPduSize = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(484, 8192))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpMaxPduSize.setStatus('current')
if mibBuilder.loadTexts: usdSnmpMaxPduSize.setDescription('The maximum sized SNMP PDU, in bytes, that this agent is capable of handling. The default is 1500 bytes. The possibility of IP fragmentation should be considered when setting this object to large values.')
usdSnmpInterfaceMode = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("usdSnmpInterfaceModeVerbose", 1), ("usdSnmpInterfaceModeCompress", 2), ("usdSnmpInterfaceModeEnhanced", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpInterfaceMode.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpInterfaceMode.setDescription('The interface table mode for the SNMP agent(s) associated with this system. usdSnmpInterfaceModeVerbose(1) - the standard ifTable, ifXTable and ifStackTable contain entries for every standard and proprietary interface type supported by this system. usdSnmpInterfaceModeCompress(2) - the standard ifTable, ifXTable and ifStackTable contain a subset of interface types. Certain interface types like HDLC and IP and others are excluded from the standard tables but are manageable from proprietary MIBs. usdSnmpInterfaceModeEnhanced(3) - the standard ifTable, ifXTable and ifStackTable contain a subset of interface types. Enhanced mode cannot by configured at this time via SNMP. Attempts to set this value will fail. ')
usdSnmpProxyStatus = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 4), UsdEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpProxyStatus.setStatus('current')
if mibBuilder.loadTexts: usdSnmpProxyStatus.setDescription('Enable/disable SNMP proxy between virtual routers.')
usdSnmpIntfCompCompressed = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpIntfCompCompressed.setStatus('current')
if mibBuilder.loadTexts: usdSnmpIntfCompCompressed.setDescription('true(1) - the standard ifTable, ifXTable and ifStackTable contain a subset of interface types. Certain interface types like HDLC and IP and others are excluded from the standard tables but are manageable from proprietary MIBs. false(2) - the standard ifTable, ifXTable and ifStackTable contain entries for every standard and proprietary interface type supported by this system. ')
usdSnmpIntfCompEnhanced = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpIntfCompEnhanced.setReference('rstc.mi2 - Unisphere-Data-IF-MIB.UsdIfType')
if mibBuilder.loadTexts: usdSnmpIntfCompEnhanced.setStatus('current')
if mibBuilder.loadTexts: usdSnmpIntfCompEnhanced.setDescription("This object governs which interface types are visable to SNMP management clients that use the standard ifTable, ifXTable and ifStackTable. The object is a variable length octet string that is interpreted as a bit mask. Each bit respresents a specific Unisphere interface type that can be included or excluded in the standard interface tables. For each bit position in each octet of the string, a '1' or '0' indicates the corresponding interface type is either removed (compressed) from the standard interface MIB tables, or included respectively. Individual bit definitions follow the UsdIfType convention defined in the Unisphere-Data-IF-MIB. For example, ip(0) and ppp(1) correspond to bit definitions 0 and 1 respectively. In each octet, bit 0 is least significant, bit 7 most significant.")
usdSnmpIntfCompEnhancedDisplay = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpIntfCompEnhancedDisplay.setStatus('current')
if mibBuilder.loadTexts: usdSnmpIntfCompEnhancedDisplay.setDescription('This object displays the excluded interface types in human readable form. Three dots (...) at the end of display string indicates that the output has been truncated. ')
usdSnmpIntfCompRestricted = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 4), UsdSnmpIntfCompRestrictedMask()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpIntfCompRestricted.setStatus('current')
if mibBuilder.loadTexts: usdSnmpIntfCompRestricted.setDescription("This object governs which interface instances appear to SNMP management clients that use the standard ifTable, ifXTable and ifStackTable. The control is based on a set of interface restrictions defined by UsdSnmpInterfaceModeRestrictedMask. For each bit position in each octet of the string, a '1' or '0' controls whether an interface instance that matches the restriction is removed or included in the standard interface MIB tables. For example, setting the value of this object to 1 will remove all interface instances with an ifAdminStatus(2). In each octet, bit 0 is least significant, bit 7 most significant.")
usdSnmpIntfCompRestrictedDisplay = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpIntfCompRestrictedDisplay.setStatus('current')
if mibBuilder.loadTexts: usdSnmpIntfCompRestrictedDisplay.setDescription('This object displays the restrictions in human readable form. Three dots (...) at the end of display string indicates that the output has been truncated.')
usdSnmpCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1), )
if mibBuilder.loadTexts: usdSnmpCommunityTable.setStatus('current')
if mibBuilder.loadTexts: usdSnmpCommunityTable.setDescription("Table of SNMP management clients. Authentic SNMP clients are identified by a combination community name and IP address. Upon receipt of an SNMP request, this table is scanned for a matching community name. If an entry containing a matching community name is found, the entry's IP access list, if nonzero, is used to validate the source IP address received in the request; else, if the IP access list number in the matching entry is zero, the source IP address is accepted. Finally, the type of SNMP request is validated with respect to the access privilege of the matching entry (e.g. a SET Request is rejected for an entry having read-only privilege). Use of this table constitutes 'trivial authentication', i.e., no mechanism is employed to confirm the received SNMP request was indeed originated by the host identified by the IP source address.")
usdSnmpCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1), ).setIndexNames((1, "Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"))
if mibBuilder.loadTexts: usdSnmpCommunityEntry.setStatus('current')
if mibBuilder.loadTexts: usdSnmpCommunityEntry.setDescription('A table entry describing an authentic SNMP Community.')
usdSnmpCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 1), UsdSnmpCommunityName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpCommunityName.setStatus('current')
if mibBuilder.loadTexts: usdSnmpCommunityName.setDescription('An SNMP community name.')
usdSnmpCommunityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdSnmpCommunityRowStatus.setDescription("Controls creation/deletion of entries in this table. Only 'createAndGo' and 'destroy' enumeration values are supported.")
usdSnmpCommunityPrivilege = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("readOnly", 1), ("readWrite", 2), ("admin", 3))).clone('readOnly')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityPrivilege.setStatus('current')
if mibBuilder.loadTexts: usdSnmpCommunityPrivilege.setDescription("The access privilege for an SNMP Community authenticated by this entry (used in conjunction with MIB view as specified via usdSnmpCommunityView). readOnly Read-only access to MIB with associated view. readWrite Read-write access to MIB with associated view. admin Read-write access to entire MIB (for backward compatibility, automatically defaults to 'everything' view and 'readWrite' privilege).")
usdSnmpCommunityAccessList = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityAccessList.setStatus('current')
if mibBuilder.loadTexts: usdSnmpCommunityAccessList.setDescription('If nonzero, the number of an IP access list that describes the IP hosts permitted SNMP management access to this device via the corresponding community name contained in this entry.')
usdSnmpCommunityAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 5), UsdSnmpAccessListName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityAccessListName.setStatus('current')
if mibBuilder.loadTexts: usdSnmpCommunityAccessListName.setDescription('If not null, the name of an IP access list that describes the IP hosts permitted SNMP management access to this device via the corresponding community name contained in this entry.')
usdSnmpCommunityView = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("everything", 1), ("user", 2), ("nothing", 3))).clone('user')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpCommunityView.setStatus('current')
if mibBuilder.loadTexts: usdSnmpCommunityView.setDescription("The view associated with an SNMP Community authenticated by this entry. everything Access to the entire MIB. user Access to non-administrative portions of MIB. nothing No access. 'Administrative' portions of the MIB are those portions that pertain to management access into the managed device.")
usdSnmpTrapGlobalFilter = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 1), UsdSnmpTrapMask()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpTrapGlobalFilter.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapGlobalFilter.setDescription("This object provides global control over trap generation by this agent. For each bit position, a '1' or '0' indicates the corresponding trap category is enabled or disabled, respectively.")
usdSnmpTrapSource = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpTrapSource.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapSource.setDescription('The ifIndex of the interface whose IP address is used as the source IP address for outbound SNMP traps. If zero, no interface is specified, the mechanism for selecting a source IP address is implementation-dependent, and may vary with each trap sent.')
usdSnmpTrapHostTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3), )
if mibBuilder.loadTexts: usdSnmpTrapHostTable.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostTable.setDescription('Table of SNMP Trap recipient.')
usdSnmpTrapHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1), ).setIndexNames((0, "Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"))
if mibBuilder.loadTexts: usdSnmpTrapHostEntry.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostEntry.setDescription('A table entry describing an SNMP Trap recipient.')
usdSnmpTrapHostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpTrapHostIpAddress.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostIpAddress.setDescription('IP address of an authorized SNMP Trap recipient. This must be a host IP address.')
usdSnmpTrapHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostRowStatus.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostRowStatus.setDescription("Controls creation/deletion of entries in this table. Only 'createAndGo' and 'destroy' enumeration values are supported.")
usdSnmpTrapHostUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostUdpPort.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostUdpPort.setDescription('The destination UDP port to which traps will be sent.')
usdSnmpTrapHostCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 4), UsdSnmpCommunityName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostCommunity.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostCommunity.setDescription('An SNMP community name to be used in traps sent to this destination.')
usdSnmpTrapHostProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("v1", 0), ("v2c", 1), ("v3", 2))).clone('v1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostProtocolVersion.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostProtocolVersion.setDescription('The format of the SNMP trap PDU to be sent to this trap destination. v1 Trap-PDU defined in RFC1157, encapsulated in the message structure also defined in RFC1157. v2c SNMPv2-Trap-PDU defined in RFC1905, encapsulated in the message structure defined in RFC1901. v3 SNMPv2-Trap-PDU defined in RFC1905, encapsulated in the message structure defined in RFC2571.')
usdSnmpTrapHostFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 6), UsdSnmpTrapMask()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostFilter.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostFilter.setDescription("Bit mask designating the specific trap types enabled for transmission to this trap destination. For each bit position, a '1' or '0' indicates the corresponding trap type is enabled or disabled, respectively. Note, trap generation is further constrained by the value usdSnmpTrapGlobalFilter.")
usdSnmpTrapHostSends = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpTrapHostSends.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostSends.setDescription('The number of traps submitted for transmission to this destination.')
usdSnmpTrapHostDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpTrapHostDiscards.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostDiscards.setDescription("The number of trap requests that were discarded. A trap may be discarded because the trap type is either not a configured type in usdSnmpTrapHostFilter, or because the traps's priority is below the minimum trap severity filter defined by usdSnmpTrapHostSeverityFilter.")
usdSnmpTrapHostSeverityFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 9), UsdTrapSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSnmpTrapHostSeverityFilter.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapHostSeverityFilter.setDescription('The minimum severity value an snmp trap must have in order to be forwarded to this host.')
usdSnmpTrapProxy = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpTrapProxy.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapProxy.setDescription('The configuration setting for snmp trap proxying. Enabling this management object configures the associated SNMP agent to proxy internally generated traps. Note that some implementations may support a single snmp trap proxy per system.')
usdSnmpTrapTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 5), UsdTrapSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpTrapTrapSeverity.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapTrapSeverity.setDescription('The severity level of the trap.')
usdSnmpTrapGlobalDiscards = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSnmpTrapGlobalDiscards.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapGlobalDiscards.setDescription("The number of trap requests that were discarded. A trap may be discarded because the trap type is either not globally configured in usdSnmpTrapGlobalFilter, or because the traps's priority is below the minimum trap severity filter defined by usdSnmpTrapGlobalSeverityFilter.")
usdSnmpTrapGlobalSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 7), UsdTrapSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSnmpTrapGlobalSeverityFilter.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapGlobalSeverityFilter.setDescription('Traps flow through two levels of filtering: global and then host. The value of this object defines the global minimum severity level a trap must have in order to be forwarded to the host level trap processing. A trap will be discarded and counted in usdSnmpTrapGlobalDiscards if its severity level is less then the value of this object.')
usdSnmpAuthFailIdIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpAuthFailIdIpAddress.setStatus('current')
if mibBuilder.loadTexts: usdSnmpAuthFailIdIpAddress.setDescription('The source IP address contained in a received SNMP request that failed authentication.')
usdSnmpAuthFailIdUdpPort = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpAuthFailIdUdpPort.setStatus('current')
if mibBuilder.loadTexts: usdSnmpAuthFailIdUdpPort.setDescription('The source UDP port contained in a received SNMP request that failed authentication.')
usdSnmpAuthFailIdCommunity = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 3), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpAuthFailIdCommunity.setStatus('current')
if mibBuilder.loadTexts: usdSnmpAuthFailIdCommunity.setDescription('The SNMP community contained in a received SNMP request that failed authentication.')
usdSnmpAuthFailIdReason = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("other", 0), ("badCommunityName", 1), ("badCommmunityUse", 2), ("hostDenied", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: usdSnmpAuthFailIdReason.setStatus('current')
if mibBuilder.loadTexts: usdSnmpAuthFailIdReason.setDescription("The reason a received SNMP request failed authentication: other Unspecified reason. badCommunityName The community is not recognized. badCommunityUse The community does not have privilege for the SNMP request type (e.g. SET request with a community having read-only privilege). hostDenied The host IP address was denied by the community's associated access list.")
usdSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1))
usdSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2))
usdSnmpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 1)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance = usdSnmpCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpCompliance.setDescription('Obsolete compliance statement for entities which implement the Unisphere SNMP MIB. This statement became obsolete when View support and Named Access List support were added.')
usdSnmpCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 2)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGroup2"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance2 = usdSnmpCompliance2.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpCompliance2.setDescription('Obsolete compliance statement for entities which implement the Unisphere SNMP MIB. This statement became obsolete when usdSnmpInterfaceMode was added.')
usdSnmpCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 3)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGroup3"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance3 = usdSnmpCompliance3.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpCompliance3.setDescription('Obsolete compliance statement for entities which implement the Unisphere SNMP MIB. This statement became obsolete when support for interface compress, trap severities and trap severity filtering was added and usdSnmpInterfaceMode was obsoleted.')
usdSnmpCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 4)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGeneralGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAccessGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance4 = usdSnmpCompliance4.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpCompliance4.setDescription('The compliance statement for entities which implement the Unisphere SNMP MIB. This statement became obsolete when support for SNMP proxy enable/disable was added.')
usdSnmpCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 5)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpGeneralGroup2"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAccessGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGroup"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpCompliance5 = usdSnmpCompliance5.setStatus('current')
if mibBuilder.loadTexts: usdSnmpCompliance5.setDescription('The compliance statement for entities which implement the Unisphere SNMP MIB.')
usdSnmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 1)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGroup = usdSnmpGroup.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpGroup.setDescription('Obsolete collection of management objects pertaining to SNMP Agent capability in a Unisphere product. This group became obsolete when View support and Named Access List support were added.')
usdSnmpAuthFailGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 2)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAuthFailGroup = usdSnmpAuthFailGroup.setStatus('current')
if mibBuilder.loadTexts: usdSnmpAuthFailGroup.setDescription('A collection of management objects pertaining to an SNMP authentication failure in a Unisphere product.')
usdSnmpGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 3)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessListName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityView"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGroup2 = usdSnmpGroup2.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpGroup2.setDescription('Obsolete collection of management objects pertaining to SNMP Agent capability in a Unisphere product. This group became obsolete when usdSnmpInterfaceMode was added.')
usdSnmpGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 4)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpInterfaceMode"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessListName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityView"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGroup3 = usdSnmpGroup3.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpGroup3.setDescription('Obsolete collection of management objects pertaining to SNMP Agent capability in a Unisphere product. This group became obsolete when support for interface compress, trap severities and trap severity filtering was added and usdSnmpInterfaceMode was obsoleted.')
usdSnmpGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 5)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompCompressed"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhanced"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhancedDisplay"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestricted"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestrictedDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGeneralGroup = usdSnmpGeneralGroup.setStatus('obsolete')
if mibBuilder.loadTexts: usdSnmpGeneralGroup.setDescription('Obsolete collection of management objects pertaining to general SNMP Agent capabilities in a Unisphere product. This group became obsolete when proxey enable/disable support was added.')
usdSnmpAccessGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 6)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessListName"), ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityView"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpAccessGroup = usdSnmpAccessGroup.setStatus('current')
if mibBuilder.loadTexts: usdSnmpAccessGroup.setDescription('A collection of management objects pertaining to SNMP Agent access capabilities in a Unisphere product.')
usdSnmpTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 7)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostDiscards"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSeverityFilter"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapTrapSeverity"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalDiscards"), ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalSeverityFilter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpTrapGroup = usdSnmpTrapGroup.setStatus('current')
if mibBuilder.loadTexts: usdSnmpTrapGroup.setDescription('A collection of management objects pertaining to SNMP Agent trap capabilities in a Unisphere product.')
usdSnmpGeneralGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 8)).setObjects(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"), ("Unisphere-Data-SNMP-MIB", "usdSnmpProxyStatus"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompCompressed"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhanced"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhancedDisplay"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestricted"), ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestrictedDisplay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSnmpGeneralGroup2 = usdSnmpGeneralGroup2.setStatus('current')
if mibBuilder.loadTexts: usdSnmpGeneralGroup2.setDescription('A collection of management objects pertaining to general SNMP Agent capabilities in a Unisphere product.')
mibBuilder.exportSymbols("Unisphere-Data-SNMP-MIB", usdSnmpTrapHostUdpPort=usdSnmpTrapHostUdpPort, PYSNMP_MODULE_ID=usdSnmpMIB, usdSnmpTrapHostTable=usdSnmpTrapHostTable, usdSnmpCompliance2=usdSnmpCompliance2, usdSnmpCommunityAccessList=usdSnmpCommunityAccessList, usdSnmpGeneralGroup2=usdSnmpGeneralGroup2, usdSnmpTrapProxy=usdSnmpTrapProxy, usdSnmpTrapHostIpAddress=usdSnmpTrapHostIpAddress, UsdSnmpTrapMask=UsdSnmpTrapMask, usdSnmpMaxPduSize=usdSnmpMaxPduSize, usdSnmpIntfCompEnhancedDisplay=usdSnmpIntfCompEnhancedDisplay, UsdSnmpIntfCompRestrictedMask=UsdSnmpIntfCompRestrictedMask, usdSnmpCommunityTable=usdSnmpCommunityTable, usdSnmpGeneralGroup=usdSnmpGeneralGroup, usdSnmpTrapHostSends=usdSnmpTrapHostSends, usdSnmpTrap=usdSnmpTrap, usdSnmpCompliance4=usdSnmpCompliance4, usdSnmpCompliance5=usdSnmpCompliance5, usdSnmpTrapGlobalSeverityFilter=usdSnmpTrapGlobalSeverityFilter, usdSnmpCommunityPrivilege=usdSnmpCommunityPrivilege, usdSnmpGroups=usdSnmpGroups, usdSnmpObjects=usdSnmpObjects, usdSnmpGeneral=usdSnmpGeneral, usdSnmpTrapHostEntry=usdSnmpTrapHostEntry, usdSnmpCompliance3=usdSnmpCompliance3, usdSnmpMIB=usdSnmpMIB, usdSnmpTrapHostProtocolVersion=usdSnmpTrapHostProtocolVersion, usdSnmpIntfCompRestricted=usdSnmpIntfCompRestricted, usdSnmpTrapGlobalFilter=usdSnmpTrapGlobalFilter, usdSnmpCompliance=usdSnmpCompliance, usdSnmpGroup3=usdSnmpGroup3, usdSnmpIntfCompRestrictedDisplay=usdSnmpIntfCompRestrictedDisplay, usdSnmpIntfCompCompressed=usdSnmpIntfCompCompressed, usdSnmpAuthFailIdReason=usdSnmpAuthFailIdReason, usdSnmpInterfaceMode=usdSnmpInterfaceMode, usdSnmpTrapHostCommunity=usdSnmpTrapHostCommunity, UsdSnmpCommunityName=UsdSnmpCommunityName, usdSnmpAuthFailId=usdSnmpAuthFailId, UsdTrapSeverity=UsdTrapSeverity, usdSnmpTrapHostDiscards=usdSnmpTrapHostDiscards, usdSnmpAuthFailIdIpAddress=usdSnmpAuthFailIdIpAddress, usdSnmpCommunityEntry=usdSnmpCommunityEntry, usdSnmpAuthFailIdUdpPort=usdSnmpAuthFailIdUdpPort, UsdSnmpAccessListName=UsdSnmpAccessListName, usdSnmpCommunityAccessListName=usdSnmpCommunityAccessListName, usdSnmpGroup=usdSnmpGroup, usdSnmpTrapGlobalDiscards=usdSnmpTrapGlobalDiscards, usdSnmpTrapHostRowStatus=usdSnmpTrapHostRowStatus, usdSnmpCommunityName=usdSnmpCommunityName, usdSnmpIntfCompEnhanced=usdSnmpIntfCompEnhanced, usdSnmpConformance=usdSnmpConformance, usdSnmpCommunity=usdSnmpCommunity, usdSnmpCommunityRowStatus=usdSnmpCommunityRowStatus, usdSnmpTrapHostSeverityFilter=usdSnmpTrapHostSeverityFilter, usdSnmpTrapSource=usdSnmpTrapSource, usdSnmpAuthFailGroup=usdSnmpAuthFailGroup, usdSnmpTrapTrapSeverity=usdSnmpTrapTrapSeverity, usdSnmpAccessGroup=usdSnmpAccessGroup, usdSnmpCompliances=usdSnmpCompliances, usdSnmpAuthFailIdCommunity=usdSnmpAuthFailIdCommunity, usdSnmpProxyStatus=usdSnmpProxyStatus, usdSnmpInterfaceCompress=usdSnmpInterfaceCompress, usdSnmpCommunityView=usdSnmpCommunityView, usdSnmpTrapHostFilter=usdSnmpTrapHostFilter, usdSnmpTrapGroup=usdSnmpTrapGroup, usdSnmpGroup2=usdSnmpGroup2)
