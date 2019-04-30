#
# PySNMP MIB module HUAWEI-MDNS-RELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MDNS-RELAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:34:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, NotificationType, iso, Counter64, Bits, Integer32, ObjectIdentity, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "NotificationType", "iso", "Counter64", "Bits", "Integer32", "ObjectIdentity", "TimeTicks", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwMdnsRelayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326))
hwMdnsRelayMIB.setRevisions(('2014-01-06 11:16', '2014-01-06 11:16',))
if mibBuilder.loadTexts: hwMdnsRelayMIB.setLastUpdated('201401061116Z')
if mibBuilder.loadTexts: hwMdnsRelayMIB.setOrganization('Huawei Technologies Co.,Ltd.')
hwMdnsRelayObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1))
hwMdnsRelayGatewayIPGlobal = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMdnsRelayGatewayIPGlobal.setStatus('current')
hwMdnsRelaySourceIPGlobal = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMdnsRelaySourceIPGlobal.setStatus('current')
hwMdnsRelayCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3), )
if mibBuilder.loadTexts: hwMdnsRelayCfgTable.setStatus('current')
hwMdnsRelayCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1), ).setIndexNames((0, "HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayVlanId"))
if mibBuilder.loadTexts: hwMdnsRelayCfgEntry.setStatus('current')
hwMdnsRelayVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hwMdnsRelayVlanId.setStatus('current')
hwMdnsRelayEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMdnsRelayEnable.setStatus('current')
hwMdnsRelayProbeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 38400), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwMdnsRelayProbeInterval.setStatus('current')
hwMdnsRelayMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2))
hwMdnsRelayMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 1))
hwMdnsRelayMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 1, 1)).setObjects(("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayGatewayIPGlobal"), ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelaySourceIPGlobal"), ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayVlanId"), ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayEnable"), ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayProbeInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMdnsRelayMibGroup = hwMdnsRelayMibGroup.setStatus('current')
hwMdnsRelayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 2))
hwMdnsRelayMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 2, 1)).setObjects(("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMdnsRelayMIBCompliance = hwMdnsRelayMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-MDNS-RELAY-MIB", hwMdnsRelayMibConformance=hwMdnsRelayMibConformance, hwMdnsRelayMIB=hwMdnsRelayMIB, hwMdnsRelayMIBCompliances=hwMdnsRelayMIBCompliances, hwMdnsRelayCfgEntry=hwMdnsRelayCfgEntry, hwMdnsRelayProbeInterval=hwMdnsRelayProbeInterval, hwMdnsRelayMibGroups=hwMdnsRelayMibGroups, hwMdnsRelayGatewayIPGlobal=hwMdnsRelayGatewayIPGlobal, hwMdnsRelayVlanId=hwMdnsRelayVlanId, hwMdnsRelayMibGroup=hwMdnsRelayMibGroup, hwMdnsRelayCfgTable=hwMdnsRelayCfgTable, hwMdnsRelayMIBCompliance=hwMdnsRelayMIBCompliance, hwMdnsRelayEnable=hwMdnsRelayEnable, hwMdnsRelayObjects=hwMdnsRelayObjects, hwMdnsRelaySourceIPGlobal=hwMdnsRelaySourceIPGlobal, PYSNMP_MODULE_ID=hwMdnsRelayMIB)
