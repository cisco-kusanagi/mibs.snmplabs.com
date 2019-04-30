#
# PySNMP MIB module ARP-Spoofing-Prevent-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARP-Spoofing-Prevent-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, NotificationType, Bits, TimeTicks, ModuleIdentity, Integer32, Counter32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "NotificationType", "Bits", "TimeTicks", "ModuleIdentity", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "iso")
RowStatus, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "DisplayString", "TextualConvention")
swARPSpoofingPreventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 62))
if mibBuilder.loadTexts: swARPSpoofingPreventMIB.setLastUpdated('0805120000Z')
if mibBuilder.loadTexts: swARPSpoofingPreventMIB.setOrganization('D-Link Corp.')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swARPSpoofingPreventCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 62, 1))
swARPSpoofingPreventInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 62, 2))
swARPSpoofingPreventMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 62, 3))
swARPSpoofingPreventMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1), )
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtTable.setStatus('current')
swARPSpoofingPreventMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1), ).setIndexNames((0, "ARP-Spoofing-Prevent-MIB", "swARPSpoofingPreventMgmtGatewayIP"), (0, "ARP-Spoofing-Prevent-MIB", "swARPSpoofingPreventMgmtGatewayMAC"))
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtEntry.setStatus('current')
swARPSpoofingPreventMgmtGatewayIP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtGatewayIP.setStatus('current')
swARPSpoofingPreventMgmtGatewayMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtGatewayMAC.setStatus('current')
swARPSpoofingPreventMgmtPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtPorts.setStatus('current')
swARPSpoofingPreventMgmtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtStatus.setStatus('current')
mibBuilder.exportSymbols("ARP-Spoofing-Prevent-MIB", swARPSpoofingPreventMgmtGatewayIP=swARPSpoofingPreventMgmtGatewayIP, swARPSpoofingPreventCtrl=swARPSpoofingPreventCtrl, swARPSpoofingPreventMgmtStatus=swARPSpoofingPreventMgmtStatus, swARPSpoofingPreventMgmtTable=swARPSpoofingPreventMgmtTable, swARPSpoofingPreventMgmt=swARPSpoofingPreventMgmt, PYSNMP_MODULE_ID=swARPSpoofingPreventMIB, swARPSpoofingPreventMgmtEntry=swARPSpoofingPreventMgmtEntry, PortList=PortList, swARPSpoofingPreventMgmtPorts=swARPSpoofingPreventMgmtPorts, swARPSpoofingPreventMIB=swARPSpoofingPreventMIB, swARPSpoofingPreventInfo=swARPSpoofingPreventInfo, swARPSpoofingPreventMgmtGatewayMAC=swARPSpoofingPreventMgmtGatewayMAC)
