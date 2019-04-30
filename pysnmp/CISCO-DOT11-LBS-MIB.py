#
# PySNMP MIB module CISCO-DOT11-LBS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-LBS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, ObjectIdentity, Gauge32, Counter32, Unsigned32, IpAddress, MibIdentifier, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Gauge32", "Counter32", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "Counter64")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
ciscoDot11LbsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 454))
ciscoDot11LbsMIB.setRevisions(('2004-11-17 00:00',))
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setLastUpdated('200411170000Z')
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setOrganization('Cisco System Inc.')
ciscoDot11LbsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 0))
ciscoDot11LbsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1))
ciscoDot11LbsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2))
ciscoDot11LbsConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1))
ciscoDot11LbsStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 2))
class Cdot11LbsTrackMethodType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rssi", 0))

class Cdot11LbsPsPacketType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("extended", 1), ("short", 2))

cdot11LbsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1), )
if mibBuilder.loadTexts: cdot11LbsProfileTable.setStatus('current')
cdot11LbsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"))
if mibBuilder.loadTexts: cdot11LbsProfileEntry.setStatus('current')
cdot11LbsProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: cdot11LbsProfileName.setStatus('current')
cdot11LbsServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerAddressType.setStatus('current')
cdot11LbsServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerAddress.setStatus('current')
cdot11LbsServerUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerUdpPort.setStatus('current')
cdot11LbsTrackMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 5), Cdot11LbsTrackMethodType().clone(namedValues=NamedValues(("rssi", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsTrackMethod.setStatus('current')
cdot11LbsPsPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 6), Cdot11LbsPsPacketType().clone('extended')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsPsPacketType.setStatus('current')
cdot11LbsTrackMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 7), MacAddress().clone(hexValue="014096000010")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsTrackMulticast.setStatus('current')
cdot11LbsMatchChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsMatchChannel.setStatus('current')
cdot11LbsProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsProfileRowStatus.setStatus('current')
cdot11LbsProfInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2), )
if mibBuilder.loadTexts: cdot11LbsProfInterfaceTable.setStatus('current')
cdot11LbsProfInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdot11LbsProfInterfaceEntry.setStatus('current')
cdot11LbsProfInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsProfInterfaceRowStatus.setStatus('current')
ciscoDot11LbsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1))
ciscoDot11LbsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2))
ciscoDot11LbsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1, 1)).setObjects(("CISCO-DOT11-LBS-MIB", "ciscoDot11LbsConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11LbsMIBCompliance = ciscoDot11LbsMIBCompliance.setStatus('current')
ciscoDot11LbsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2, 1)).setObjects(("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddressType"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddress"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerUdpPort"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMethod"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsPsPacketType"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMulticast"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsMatchChannel"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfileRowStatus"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfInterfaceRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11LbsConfigGroup = ciscoDot11LbsConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-LBS-MIB", cdot11LbsMatchChannel=cdot11LbsMatchChannel, cdot11LbsServerUdpPort=cdot11LbsServerUdpPort, ciscoDot11LbsMIB=ciscoDot11LbsMIB, Cdot11LbsTrackMethodType=Cdot11LbsTrackMethodType, cdot11LbsTrackMethod=cdot11LbsTrackMethod, cdot11LbsProfInterfaceTable=cdot11LbsProfInterfaceTable, ciscoDot11LbsMIBCompliances=ciscoDot11LbsMIBCompliances, cdot11LbsServerAddressType=cdot11LbsServerAddressType, PYSNMP_MODULE_ID=ciscoDot11LbsMIB, cdot11LbsTrackMulticast=cdot11LbsTrackMulticast, cdot11LbsProfInterfaceEntry=cdot11LbsProfInterfaceEntry, cdot11LbsProfileTable=cdot11LbsProfileTable, cdot11LbsProfileRowStatus=cdot11LbsProfileRowStatus, cdot11LbsProfileName=cdot11LbsProfileName, ciscoDot11LbsConfigGroup=ciscoDot11LbsConfigGroup, ciscoDot11LbsStatistics=ciscoDot11LbsStatistics, ciscoDot11LbsConfigInfo=ciscoDot11LbsConfigInfo, cdot11LbsPsPacketType=cdot11LbsPsPacketType, ciscoDot11LbsMIBConformance=ciscoDot11LbsMIBConformance, ciscoDot11LbsMIBObjects=ciscoDot11LbsMIBObjects, cdot11LbsServerAddress=cdot11LbsServerAddress, Cdot11LbsPsPacketType=Cdot11LbsPsPacketType, cdot11LbsProfInterfaceRowStatus=cdot11LbsProfInterfaceRowStatus, cdot11LbsProfileEntry=cdot11LbsProfileEntry, ciscoDot11LbsMIBGroups=ciscoDot11LbsMIBGroups, ciscoDot11LbsMIBCompliance=ciscoDot11LbsMIBCompliance, ciscoDot11LbsMIBNotifs=ciscoDot11LbsMIBNotifs)
