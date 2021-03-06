#
# PySNMP MIB module ELTEX-MES-L2-TUNNEL-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-L2-TUNNEL-CONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
QosLayer2Cos, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "QosLayer2Cos")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, ModuleIdentity, TimeTicks, Bits, Integer32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, NotificationType, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Bits", "Integer32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "NotificationType", "Counter32", "iso")
MacAddress, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "TextualConvention")
eltMesL2TunnelConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13))
eltMesL2TunnelConfig.setRevisions(('2015-11-19 00:00',))
if mibBuilder.loadTexts: eltMesL2TunnelConfig.setLastUpdated('201511190000Z')
if mibBuilder.loadTexts: eltMesL2TunnelConfig.setOrganization('Eltex Enterprise Co, Ltd.')
eltMesLtcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1))
eltMesLtcGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 1))
eltMesLtcTunneledProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2))
eltMesLtcTunnelThreshold = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3))
eltMesLtcTunnelStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4))
class EltLtcTunneledProtocolIndex(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("stp", 1))

eltLtcNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcNotificationEnable.setStatus('deprecated')
eltLtcTunnelMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 1, 2), MacAddress().clone(hexValue="0100EEEE0000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunnelMacAddress.setStatus('deprecated')
eltLtcTunneledProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1), )
if mibBuilder.loadTexts: eltLtcTunneledProtocolTable.setStatus('deprecated')
eltLtcTunneledProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltLtcTunneledProtocolEntry.setStatus('deprecated')
eltLtcTunneledProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1, 1, 1), Bits().clone(namedValues=NamedValues(("stp", 0), ("workaround", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunneledProtocolType.setStatus('deprecated')
eltLtcTunnelCos = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1, 1, 2), QosLayer2Cos()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunnelCos.setStatus('deprecated')
eltLtcTunnelThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1), )
if mibBuilder.loadTexts: eltLtcTunnelThresholdTable.setStatus('deprecated')
eltLtcTunnelThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunnelThresholdProtocolIndex"))
if mibBuilder.loadTexts: eltLtcTunnelThresholdEntry.setStatus('deprecated')
eltLtcTunnelThresholdProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1, 1), EltLtcTunneledProtocolIndex())
if mibBuilder.loadTexts: eltLtcTunnelThresholdProtocolIndex.setStatus('deprecated')
eltLtcTunnelDropThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1, 2), Unsigned32()).setUnits('PDUs/sec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunnelDropThreshold.setStatus('deprecated')
eltLtcTunnelShutdownThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1, 3), Unsigned32()).setUnits('PDUs/sec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunnelShutdownThreshold.setStatus('deprecated')
eltLtcTunnelStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1), )
if mibBuilder.loadTexts: eltLtcTunnelStatisticsTable.setStatus('deprecated')
eltLtcTunnelStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunneledProtocolIndex"))
if mibBuilder.loadTexts: eltLtcTunnelStatisticsEntry.setStatus('deprecated')
eltLtcTunneledProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 1), EltLtcTunneledProtocolIndex())
if mibBuilder.loadTexts: eltLtcTunneledProtocolIndex.setStatus('deprecated')
eltLtcTunnelEncapStats = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 2), Counter32()).setUnits('encapsulated PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltLtcTunnelEncapStats.setStatus('deprecated')
eltLtcTunnelDecapStats = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 3), Counter32()).setUnits('de-encapsulated PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltLtcTunnelDecapStats.setStatus('deprecated')
eltLtcTunnelDropStats = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 4), Counter32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltLtcTunnelDropStats.setStatus('deprecated')
eltMesLtcMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2))
eltMesLtcMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2, 0))
eltLtcTunnelDropThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2, 0, 1)).setObjects(("ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunnelDropThreshold"))
if mibBuilder.loadTexts: eltLtcTunnelDropThresholdExceeded.setStatus('deprecated')
eltLtcTunnelShutdownThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2, 0, 2)).setObjects(("ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunnelShutdownThreshold"))
if mibBuilder.loadTexts: eltLtcTunnelShutdownThresholdExceeded.setStatus('deprecated')
mibBuilder.exportSymbols("ELTEX-MES-L2-TUNNEL-CONFIG-MIB", eltMesLtcMIBNotifications=eltMesLtcMIBNotifications, EltLtcTunneledProtocolIndex=EltLtcTunneledProtocolIndex, eltMesLtcMIBObjects=eltMesLtcMIBObjects, eltLtcTunnelCos=eltLtcTunnelCos, eltLtcTunnelShutdownThresholdExceeded=eltLtcTunnelShutdownThresholdExceeded, eltLtcTunneledProtocolEntry=eltLtcTunneledProtocolEntry, eltLtcTunnelMacAddress=eltLtcTunnelMacAddress, eltLtcTunneledProtocolTable=eltLtcTunneledProtocolTable, eltMesLtcTunnelStatistics=eltMesLtcTunnelStatistics, eltMesLtcTunneledProtocol=eltMesLtcTunneledProtocol, eltLtcTunnelEncapStats=eltLtcTunnelEncapStats, eltLtcTunnelDropStats=eltLtcTunnelDropStats, eltLtcTunnelStatisticsEntry=eltLtcTunnelStatisticsEntry, eltLtcTunnelDropThresholdExceeded=eltLtcTunnelDropThresholdExceeded, eltLtcTunnelThresholdProtocolIndex=eltLtcTunnelThresholdProtocolIndex, eltMesLtcGlobal=eltMesLtcGlobal, eltLtcTunneledProtocolIndex=eltLtcTunneledProtocolIndex, eltLtcTunnelStatisticsTable=eltLtcTunnelStatisticsTable, eltLtcTunnelDropThreshold=eltLtcTunnelDropThreshold, eltLtcTunnelDecapStats=eltLtcTunnelDecapStats, eltMesL2TunnelConfig=eltMesL2TunnelConfig, eltLtcNotificationEnable=eltLtcNotificationEnable, eltLtcTunnelShutdownThreshold=eltLtcTunnelShutdownThreshold, eltLtcTunneledProtocolType=eltLtcTunneledProtocolType, eltMesLtcMIBNotificationsPrefix=eltMesLtcMIBNotificationsPrefix, eltLtcTunnelThresholdEntry=eltLtcTunnelThresholdEntry, eltLtcTunnelThresholdTable=eltLtcTunnelThresholdTable, PYSNMP_MODULE_ID=eltMesL2TunnelConfig, eltMesLtcTunnelThreshold=eltMesLtcTunnelThreshold)
