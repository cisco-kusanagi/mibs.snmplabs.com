#
# PySNMP MIB module ELTEX-MES-L2-TUNNEL-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-L2-TUNNEL-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:01:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
QosLayer2Cos, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "QosLayer2Cos")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Unsigned32, Counter64, TimeTicks, Gauge32, ModuleIdentity, IpAddress, ObjectIdentity, Counter32, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Unsigned32", "Counter64", "TimeTicks", "Gauge32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Counter32", "MibIdentifier", "NotificationType", "iso")
TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
eltMesL2TunnelConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13))
eltMesL2TunnelConfig.setRevisions(('2015-11-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesL2TunnelConfig.setRevisionsDescriptions(('Deprecate all objects in this module.',))
if mibBuilder.loadTexts: eltMesL2TunnelConfig.setLastUpdated('201511190000Z')
if mibBuilder.loadTexts: eltMesL2TunnelConfig.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltMesL2TunnelConfig.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesL2TunnelConfig.setDescription('This MIB module is for layer 2 tunneling related configurations on a device. Tunneling allows separate local networks to be considered as a single VLAN. These separate networks are connected via an ISP, which will tunnel the packets from one network to another, making it appear as if the two networks are actually just one.')
eltMesLtcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1))
eltMesLtcGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 1))
eltMesLtcTunneledProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2))
eltMesLtcTunnelThreshold = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3))
eltMesLtcTunnelStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4))
class EltLtcTunneledProtocolIndex(TextualConvention, Integer32):
    description = 'A tunneled protocol of an interface. Supported value is stp(1).'
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("stp", 1))

eltLtcNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcNotificationEnable.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcNotificationEnable.setDescription('This object indicates whether the system will generate the eltLtcTunnelDropThresholdExceeded and eltLtcTunnelShutdownThresholdExceeded notifications.')
eltLtcTunnelMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 1, 2), MacAddress().clone(hexValue="0100EEEE0000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunnelMacAddress.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelMacAddress.setDescription('The destination MAC address that replaces the original destination MAC address of tunneled frames.')
eltLtcTunneledProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1), )
if mibBuilder.loadTexts: eltLtcTunneledProtocolTable.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunneledProtocolTable.setDescription('This table contains information about the protocols being tunneled. Only tunneled protocol filtering capable interfaces are shown.')
eltLtcTunneledProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltLtcTunneledProtocolEntry.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunneledProtocolEntry.setDescription('Information about the protocols being tunneled. Only tunneled protocol filtering capable interfaces are shown.')
eltLtcTunneledProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1, 1, 1), Bits().clone(namedValues=NamedValues(("stp", 0), ("workaround", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunneledProtocolType.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunneledProtocolType.setDescription("Indicates tunneled protocol of the interface. If a BIT is set, then the value of the corresponding protocol is tunneled. Specifically, if the 'stp(0)' BIT is set, then the Spanning Tree Protocol PDU is tunneled. At this moment, there are no other supported protocols. If the bit for a given protocol is set for an interface, then the statistics for that interface and protocol will start to be monitored.")
eltLtcTunnelCos = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1, 1, 2), QosLayer2Cos()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunnelCos.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelCos.setDescription('Specifies the user priority of the tunneled PDUs for the interface.')
eltLtcTunnelThresholdTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1), )
if mibBuilder.loadTexts: eltLtcTunnelThresholdTable.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelThresholdTable.setDescription('This table contains information about the thresholds for protocol tunneling. Only tunneled protocol filtering capable interfaces are shown. The objects will be on a per interface, per protocol basis.')
eltLtcTunnelThresholdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunnelThresholdProtocolIndex"))
if mibBuilder.loadTexts: eltLtcTunnelThresholdEntry.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelThresholdEntry.setDescription('Information about the thresholds for protocol tunneling. Only tunneled protocol filtering capable interfaces are shown. The entries will be on a per interface, per protocol basis')
eltLtcTunnelThresholdProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1, 1), EltLtcTunneledProtocolIndex())
if mibBuilder.loadTexts: eltLtcTunnelThresholdProtocolIndex.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelThresholdProtocolIndex.setDescription('A tunneled protocol of an interface.')
eltLtcTunnelDropThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1, 2), Unsigned32()).setUnits('PDUs/sec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunnelDropThreshold.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelDropThreshold.setDescription('The drop threshold on an interface for a given protocol. After reaching this drop threshold, the interface will start dropping PDUs for the given protocol. This value cannot be greater than the value of eltLtcTunnelShutdownThreshold. A value of 0 indicates that no limit is set.')
eltLtcTunnelShutdownThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1, 3), Unsigned32()).setUnits('PDUs/sec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltLtcTunnelShutdownThreshold.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelShutdownThreshold.setDescription('The shutdown threshold on an interface for a given protocol. After reaching the shutdown threshold, the interface will shutdown for the given protocol. This value cannot be less than the value of eltLtcTunnelDropThreshold. A value of 0 indicates that no limit is set.')
eltLtcTunnelStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1), )
if mibBuilder.loadTexts: eltLtcTunnelStatisticsTable.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelStatisticsTable.setDescription('This table contains protocol tunneling statistics on the interface.')
eltLtcTunnelStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunneledProtocolIndex"))
if mibBuilder.loadTexts: eltLtcTunnelStatisticsEntry.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelStatisticsEntry.setDescription('Protocol tunneling statistics on the interface.')
eltLtcTunneledProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 1), EltLtcTunneledProtocolIndex())
if mibBuilder.loadTexts: eltLtcTunneledProtocolIndex.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunneledProtocolIndex.setDescription('A tunneled protocol of an interface.')
eltLtcTunnelEncapStats = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 2), Counter32()).setUnits('encapsulated PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltLtcTunnelEncapStats.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelEncapStats.setDescription('The tunneled PDU encapsulation statistics of an interface. These statistics cover the number of tunneled ingress PDUs.')
eltLtcTunnelDecapStats = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 3), Counter32()).setUnits('de-encapsulated PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltLtcTunnelDecapStats.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelDecapStats.setDescription('The tunneled PDU de-encapsulation statistics of an interface. These statistics cover the number of tunneled egress PDUs.')
eltLtcTunnelDropStats = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 4), Counter32()).setUnits('PDUs').setMaxAccess("readonly")
if mibBuilder.loadTexts: eltLtcTunnelDropStats.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelDropStats.setDescription('The number of PDUs dropped on an interface for a given protocol. The PDUs will be dropped when the eltLtcTunnelDropThreshold is reached.')
eltMesLtcMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2))
eltMesLtcMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2, 0))
eltLtcTunnelDropThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2, 0, 1)).setObjects(("ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunnelDropThreshold"))
if mibBuilder.loadTexts: eltLtcTunnelDropThresholdExceeded.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelDropThresholdExceeded.setDescription('This notification is generated when the eltLtcTunnelDropThreshold has been exceeded.')
eltLtcTunnelShutdownThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2, 0, 2)).setObjects(("ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunnelShutdownThreshold"))
if mibBuilder.loadTexts: eltLtcTunnelShutdownThresholdExceeded.setStatus('deprecated')
if mibBuilder.loadTexts: eltLtcTunnelShutdownThresholdExceeded.setDescription('This notification is generated when the eltLtcTunnelShutdownThreshold has been exceeded.')
mibBuilder.exportSymbols("ELTEX-MES-L2-TUNNEL-CONFIG-MIB", eltLtcTunnelShutdownThresholdExceeded=eltLtcTunnelShutdownThresholdExceeded, eltLtcNotificationEnable=eltLtcNotificationEnable, eltMesLtcTunnelThreshold=eltMesLtcTunnelThreshold, eltLtcTunnelCos=eltLtcTunnelCos, eltMesLtcGlobal=eltMesLtcGlobal, eltMesLtcMIBNotificationsPrefix=eltMesLtcMIBNotificationsPrefix, eltLtcTunnelThresholdProtocolIndex=eltLtcTunnelThresholdProtocolIndex, eltLtcTunneledProtocolType=eltLtcTunneledProtocolType, eltLtcTunnelThresholdTable=eltLtcTunnelThresholdTable, eltLtcTunneledProtocolTable=eltLtcTunneledProtocolTable, eltLtcTunnelMacAddress=eltLtcTunnelMacAddress, eltLtcTunnelDropThresholdExceeded=eltLtcTunnelDropThresholdExceeded, eltLtcTunnelDropThreshold=eltLtcTunnelDropThreshold, eltLtcTunnelStatisticsTable=eltLtcTunnelStatisticsTable, EltLtcTunneledProtocolIndex=EltLtcTunneledProtocolIndex, eltLtcTunnelThresholdEntry=eltLtcTunnelThresholdEntry, eltLtcTunnelDropStats=eltLtcTunnelDropStats, eltMesLtcTunneledProtocol=eltMesLtcTunneledProtocol, eltLtcTunnelEncapStats=eltLtcTunnelEncapStats, PYSNMP_MODULE_ID=eltMesL2TunnelConfig, eltLtcTunneledProtocolEntry=eltLtcTunneledProtocolEntry, eltMesL2TunnelConfig=eltMesL2TunnelConfig, eltLtcTunnelDecapStats=eltLtcTunnelDecapStats, eltLtcTunneledProtocolIndex=eltLtcTunneledProtocolIndex, eltLtcTunnelShutdownThreshold=eltLtcTunnelShutdownThreshold, eltMesLtcMIBObjects=eltMesLtcMIBObjects, eltMesLtcMIBNotifications=eltMesLtcMIBNotifications, eltLtcTunnelStatisticsEntry=eltLtcTunnelStatisticsEntry, eltMesLtcTunnelStatistics=eltMesLtcTunnelStatistics)
