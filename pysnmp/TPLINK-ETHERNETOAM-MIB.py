#
# PySNMP MIB module TPLINK-ETHERNETOAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ETHERNETOAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, IpAddress, MibIdentifier, Integer32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, TimeTicks, iso, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "Integer32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "TimeTicks", "iso", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkEthernetOam = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 60))
tplinkEthernetOam.setRevisions(('2015-07-06 10:30',))
if mibBuilder.loadTexts: tplinkEthernetOam.setLastUpdated('201507061030Z')
if mibBuilder.loadTexts: tplinkEthernetOam.setOrganization('TPLINK')
tplinkEthernetOamMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1))
tplinkEthernetOamMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 2))
ethernetOamBasicConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1))
ethernetOamLinkMonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2))
ethernetOamRfiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3))
ethernetOamRmtLbConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4))
ethernetOamDiscoveryInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5))
ethernetOamStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6))
ethernetOamEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7))
mibBuilder.exportSymbols("TPLINK-ETHERNETOAM-MIB", ethernetOamBasicConfig=ethernetOamBasicConfig, ethernetOamStatistics=ethernetOamStatistics, ethernetOamDiscoveryInfo=ethernetOamDiscoveryInfo, ethernetOamLinkMonConfig=ethernetOamLinkMonConfig, ethernetOamRfiConfig=ethernetOamRfiConfig, ethernetOamEventLog=ethernetOamEventLog, tplinkEthernetOamMIBObjects=tplinkEthernetOamMIBObjects, PYSNMP_MODULE_ID=tplinkEthernetOam, ethernetOamRmtLbConfig=ethernetOamRmtLbConfig, tplinkEthernetOamMIBNotifications=tplinkEthernetOamMIBNotifications, tplinkEthernetOam=tplinkEthernetOam)
