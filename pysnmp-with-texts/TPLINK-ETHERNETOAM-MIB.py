#
# PySNMP MIB module TPLINK-ETHERNETOAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ETHERNETOAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, Gauge32, ObjectIdentity, Integer32, Bits, NotificationType, Unsigned32, IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Gauge32", "ObjectIdentity", "Integer32", "Bits", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkEthernetOam = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 60))
tplinkEthernetOam.setRevisions(('2015-07-06 10:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkEthernetOam.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkEthernetOam.setLastUpdated('201507061030Z')
if mibBuilder.loadTexts: tplinkEthernetOam.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkEthernetOam.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkEthernetOam.setDescription('Private MIB for Ethernet OAM.')
tplinkEthernetOamMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1))
tplinkEthernetOamMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 2))
ethernetOamBasicConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1))
ethernetOamLinkMonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 2))
ethernetOamRfiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3))
ethernetOamRmtLbConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4))
ethernetOamDiscoveryInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 5))
ethernetOamStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 6))
ethernetOamEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 7))
mibBuilder.exportSymbols("TPLINK-ETHERNETOAM-MIB", tplinkEthernetOamMIBNotifications=tplinkEthernetOamMIBNotifications, tplinkEthernetOamMIBObjects=tplinkEthernetOamMIBObjects, ethernetOamRfiConfig=ethernetOamRfiConfig, tplinkEthernetOam=tplinkEthernetOam, ethernetOamBasicConfig=ethernetOamBasicConfig, PYSNMP_MODULE_ID=tplinkEthernetOam, ethernetOamDiscoveryInfo=ethernetOamDiscoveryInfo, ethernetOamLinkMonConfig=ethernetOamLinkMonConfig, ethernetOamStatistics=ethernetOamStatistics, ethernetOamEventLog=ethernetOamEventLog, ethernetOamRmtLbConfig=ethernetOamRmtLbConfig)
