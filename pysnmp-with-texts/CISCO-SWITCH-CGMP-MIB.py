#
# PySNMP MIB module CISCO-SWITCH-CGMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-CGMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:13:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, Gauge32, ObjectIdentity, Unsigned32, ModuleIdentity, IpAddress, Counter64, TimeTicks, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "Gauge32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "IpAddress", "Counter64", "TimeTicks", "Integer32", "iso")
MacAddress, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "RowStatus", "DisplayString")
ciscoSwitchCgmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 101))
ciscoSwitchCgmpMIB.setRevisions(('1998-05-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setLastUpdated('9805070000Z')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setOrganization('Cisco Systems, Inc')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-ipmulticast@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIB.setDescription('Switch-side Cisco Group Management Protocol MIB for Layer 2 Switch devices.')
ciscoSwitchCgmpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 1))
sCgmpInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1))
class SCgmpVlanIndex(TextualConvention, Integer32):
    description = 'The VLAN-id of a VLAN on either ISL trunk, 802.1q trunk or port-based VLAN implementations.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1023)

sCgmpEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpEnable.setStatus('current')
if mibBuilder.loadTexts: sCgmpEnable.setDescription('This variable allows user to enable or disable Cisco Group Management Protocol (CGMP).')
sCgmpFastLeaveEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpFastLeaveEnable.setStatus('current')
if mibBuilder.loadTexts: sCgmpFastLeaveEnable.setDescription('This variable allows user to enable or disable Cisco Group Management Protocol (CGMP) Fast Leave processing.')
sCgmpRouterHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 6000))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpRouterHoldTime.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterHoldTime.setDescription('Multicast routers that support CGMP will send CGMP join message to advertise themselves to switches within a network. A switch that receives a CGMP message will save the information and set a timer equal to this router hold time. When the router hold time expires, the switch will remove the Router entry from CGMP. The default value is 300 seconds.')
sCgmpRouterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4), )
if mibBuilder.loadTexts: sCgmpRouterTable.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterTable.setDescription('List of Router entries present on the switch.')
sCgmpRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterVlanIndex"), (0, "BRIDGE-MIB", "dot1dBasePort"), (0, "CISCO-SWITCH-CGMP-MIB", "sCgmpRouterMacAddress"))
if mibBuilder.loadTexts: sCgmpRouterEntry.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterEntry.setDescription("Entry containing multicast router information for a particular router. These entries are created when a router sends a CGMP join for itself on a particular vlan. Entries may be removed when a router entry's sCgmpRouterHoldTime expires, or when explicitly removed by a user.")
sCgmpRouterVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 1), SCgmpVlanIndex())
if mibBuilder.loadTexts: sCgmpRouterVlanIndex.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterVlanIndex.setDescription('An index value that uniquely identifies the vlan on which the router identified by this router entry is located. This value may be the same as used in the CISCO-VLAN-MEMBERSHIP-MIB and the CISCO-VTP-MIB for the same given vlan, if VTP is present and in use on the switch.')
sCgmpRouterMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 3), MacAddress())
if mibBuilder.loadTexts: sCgmpRouterMacAddress.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterMacAddress.setDescription('An 802 MAC Address in canonical format. This is the MAC address of the router itself.')
sCgmpRouterEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 101, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sCgmpRouterEntryStatus.setStatus('current')
if mibBuilder.loadTexts: sCgmpRouterEntryStatus.setDescription('This object is used by a management station to delete the row entry in sCgmpRouterTable following the RowStatus textual convention. The managment station may remove this entry by setting destroy (6). Entries may not be created. Entries removed may reappear in normal CGMP operation when the router sends another self join.')
ciscoSwitchCgmpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3))
ciscoSwitchCgmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1))
ciscoSwitchCgmpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2))
ciscoSwitchCgmpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 1, 1)).setObjects(("CISCO-SWITCH-CGMP-MIB", "sCgmpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCgmpMIBCompliance = ciscoSwitchCgmpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchCgmpMIBCompliance.setDescription('The compliance statement for switches implementing the Cisco Group Management Protocol')
sCgmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 101, 3, 2, 1)).setObjects(("CISCO-SWITCH-CGMP-MIB", "sCgmpEnable"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpFastLeaveEnable"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterHoldTime"), ("CISCO-SWITCH-CGMP-MIB", "sCgmpRouterEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sCgmpGroup = sCgmpGroup.setStatus('current')
if mibBuilder.loadTexts: sCgmpGroup.setDescription('Switch-side Cisco Group Management Protocol.')
mibBuilder.exportSymbols("CISCO-SWITCH-CGMP-MIB", ciscoSwitchCgmpMIBObjects=ciscoSwitchCgmpMIBObjects, ciscoSwitchCgmpMIB=ciscoSwitchCgmpMIB, sCgmpInfo=sCgmpInfo, sCgmpRouterVlanIndex=sCgmpRouterVlanIndex, sCgmpRouterHoldTime=sCgmpRouterHoldTime, sCgmpRouterMacAddress=sCgmpRouterMacAddress, sCgmpRouterEntry=sCgmpRouterEntry, sCgmpRouterEntryStatus=sCgmpRouterEntryStatus, ciscoSwitchCgmpMIBGroups=ciscoSwitchCgmpMIBGroups, ciscoSwitchCgmpMIBCompliance=ciscoSwitchCgmpMIBCompliance, sCgmpFastLeaveEnable=sCgmpFastLeaveEnable, ciscoSwitchCgmpMIBCompliances=ciscoSwitchCgmpMIBCompliances, sCgmpGroup=sCgmpGroup, sCgmpEnable=sCgmpEnable, ciscoSwitchCgmpMIBConformance=ciscoSwitchCgmpMIBConformance, PYSNMP_MODULE_ID=ciscoSwitchCgmpMIB, sCgmpRouterTable=sCgmpRouterTable, SCgmpVlanIndex=SCgmpVlanIndex)
