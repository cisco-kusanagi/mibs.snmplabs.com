#
# PySNMP MIB module CISCO-VLAN-BRIDGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-BRIDGING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPortList, = mibBuilder.importSymbols("CISCO-TC", "CiscoPortList")
vtpVlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "vtpVlanIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Integer32, Counter64, Counter32, ModuleIdentity, Unsigned32, ObjectIdentity, Bits, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Integer32", "Counter64", "Counter32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Bits", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanBridgingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 56))
ciscoVlanBridgingMIB.setRevisions(('2003-08-22 00:00', '1996-09-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setRevisionsDescriptions(('Deprecate cvbStpForwardingMap and define cvbStpForwardingMap2k to support up to 2k bridge ports.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setLastUpdated('200308220000Z')
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vlans@cisco.com cs-lan-switch-snmp')
if mibBuilder.loadTexts: ciscoVlanBridgingMIB.setDescription('A set of managed objects for optimizing access to bridging related data from RFC 1493. This MIB is modeled after portions of RFC 1493, adding VLAN ID based indexing and bitmapped encoding of frequently accessed data.')
ciscoVlanBridgingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 1))
cvbStp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1))
cvbStpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1), )
if mibBuilder.loadTexts: cvbStpTable.setStatus('current')
if mibBuilder.loadTexts: cvbStpTable.setDescription('This table contains device STP status information for each VLAN.')
cvbStpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VTP-MIB", "vtpVlanIndex"))
if mibBuilder.loadTexts: cvbStpEntry.setStatus('current')
if mibBuilder.loadTexts: cvbStpEntry.setDescription('Device STP status for specified VLAN.')
cvbStpForwardingMap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvbStpForwardingMap.setStatus('deprecated')
if mibBuilder.loadTexts: cvbStpForwardingMap.setDescription('An indication of which ports are forwarding by spanning tree for the specified VLAN. The octet string contains one bit per port on the bridge for the specified VLAN. Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. The bit value interpretation is related to RFC 1493 dot1dStpPortState values is as follows: 1 = forwarding 0 = disabled, blocking, listening, learning, broken, or nonexistent')
cvbStpForwardingMap2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 56, 1, 1, 1, 1, 3), CiscoPortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvbStpForwardingMap2k.setStatus('current')
if mibBuilder.loadTexts: cvbStpForwardingMap2k.setDescription('An indication of which ports are forwarding by spanning tree for the specified VLAN. The octet string contains one bit per port on the bridge for the specified VLAN. This object has STP status information of up to 2k ports with the port number from 1 to 2048. Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. The bit value interpretation is related to RFC 1493 dot1dStpPortState values is as follows: 1 = forwarding 0 = disabled, blocking, listening, learning, broken, or nonexistent.')
ciscoVlanBridgingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 3))
ciscoVlanBridgingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1))
ciscoVlanBridgingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2))
ciscoVlanBridgingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1, 1)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "ciscoVlanBridgingMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBCompliance = ciscoVlanBridgingMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoVlanBridgingMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco VLAN Bridging MIB.')
ciscoVlanBridgingMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 1, 2)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "ciscoVlanBridgingMIBGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBCompliance2 = ciscoVlanBridgingMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanBridgingMIBCompliance2.setDescription('The compliance statement for entities which implement the Cisco VLAN Bridging MIB.')
ciscoVlanBridgingMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2, 1)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "cvbStpForwardingMap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBGroup = ciscoVlanBridgingMIBGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoVlanBridgingMIBGroup.setDescription('A collection of objects providing the STP status information of up to 1k ports with the port number from 1 to 1024.')
ciscoVlanBridgingMIBGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 56, 3, 2, 2)).setObjects(("CISCO-VLAN-BRIDGING-MIB", "cvbStpForwardingMap2k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVlanBridgingMIBGroup2 = ciscoVlanBridgingMIBGroup2.setStatus('current')
if mibBuilder.loadTexts: ciscoVlanBridgingMIBGroup2.setDescription('A collection of objects providing the STP status information of up to 2k ports with the port number from 1 to 2048.')
mibBuilder.exportSymbols("CISCO-VLAN-BRIDGING-MIB", ciscoVlanBridgingMIB=ciscoVlanBridgingMIB, cvbStp=cvbStp, cvbStpTable=cvbStpTable, ciscoVlanBridgingMIBConformance=ciscoVlanBridgingMIBConformance, ciscoVlanBridgingMIBCompliance=ciscoVlanBridgingMIBCompliance, ciscoVlanBridgingMIBCompliance2=ciscoVlanBridgingMIBCompliance2, ciscoVlanBridgingMIBObjects=ciscoVlanBridgingMIBObjects, PYSNMP_MODULE_ID=ciscoVlanBridgingMIB, ciscoVlanBridgingMIBGroup2=ciscoVlanBridgingMIBGroup2, ciscoVlanBridgingMIBGroups=ciscoVlanBridgingMIBGroups, ciscoVlanBridgingMIBGroup=ciscoVlanBridgingMIBGroup, cvbStpForwardingMap=cvbStpForwardingMap, cvbStpEntry=cvbStpEntry, ciscoVlanBridgingMIBCompliances=ciscoVlanBridgingMIBCompliances, cvbStpForwardingMap2k=cvbStpForwardingMap2k)
