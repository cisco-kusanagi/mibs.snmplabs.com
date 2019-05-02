#
# PySNMP MIB module TWTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TWTRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:28:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mgmt, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, internet, TimeTicks, NotificationType, Bits, IpAddress, NotificationType, Counter64, Gauge32, Unsigned32, Counter32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "mgmt", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "internet", "TimeTicks", "NotificationType", "Bits", "IpAddress", "NotificationType", "Counter64", "Gauge32", "Unsigned32", "Counter32", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mgmt = MibIdentifier((1, 3, 6, 1, 2))
directory = MibIdentifier((1, 3, 6, 1, 1))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
mib_2 = MibIdentifier((1, 3, 6, 1, 2, 1)).setLabel("mib-2")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

npi = MibIdentifier((1, 3, 6, 1, 4, 1, 1101))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 1))
npi_Switching_MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2)).setLabel("npi-Switching-MIB")
switch_Common_MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1)).setLabel("switch-Common-MIB")
switchBasicHubInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 1))
switchBasicPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 2))
switch_DS24 = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13)).setLabel("switch-DS24")
switch_TidalWave = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 10)).setLabel("switch-TidalWave")
switch_FE1200PLUS = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1)).setLabel("switch-FE1200PLUS")
switch_FE1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 3)).setLabel("switch-FE1200")
switch_Cascade_MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2)).setLabel("switch-Cascade-MIB")
switchCmsBasicPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1))
switchCmsBasicClusterInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 1))
switchCmsBasicUnitInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 2))
switchCmsBasicPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3))
switchCmsAddrTrackPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 3))
switchCmsAddrTrackPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3))
dot1dBridge = MibIdentifier((1, 3, 6, 1, 2, 1, 17))
dot1dBase = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 1))
dot1dStp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 2))
dot1dSr = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 3))
dot1dTp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 4))
dot1dStatic = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 5))
devDeviceInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 1, 1))
devMonitorInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 1, 2))
devActionInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 1, 3))
devMonTrapReportLevel = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 1, 2, 2))
snmpDot3RptrMgt = MibIdentifier((1, 3, 6, 1, 2, 1, 22))
rptrBasicPackage = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1))
rptrMonitorPackage = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 2))
rptrAddrTrackPackage = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 3))
rptrRptrInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 1))
rptrGroupInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 2))
rptrPortInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 3))
rptrMonitorRptrInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 2, 1))
rptrMonitorGroupInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 2, 2))
rptrMonitorPortInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 2, 3))
rptrAddrTrackRptrInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 3, 1))
rptrAddrTrackGroupInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 3, 2))
rptrAddrTrackPortInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 3, 3))
rptrPortTable = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 3, 1))
rptrPortEntry = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1))
rptrPortIndex = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 2))
rptrPortGroupIndex = MibIdentifier((1, 3, 6, 1, 2, 1, 22, 1, 3, 1, 1, 1))
basicUnitTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 2, 1))
basicUnitEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 2, 1, 1))
basicUnitIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 2, 1, 1, 1))
basicPortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3, 1))
basicPortEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3, 1, 1))
basicPortUnitIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3, 1, 1, 1))
basicPortIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 1, 3, 1, 1, 2))
addrTrackPortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3, 1))
addrTrackPortEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3, 1, 1))
addrTrackPortUnitIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3, 1, 1, 1))
addrTrackPortPortIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 2, 3, 3, 1, 1, 2))
basicSwitchPowerState = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 1, 14))
switchPortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1))
switchPortEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1))
switchPortIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1, 1))
switchPortFullDuplex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1, 6))
switchPortFlowControl = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1, 7))
switchPortSpeed = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 2, 1, 1, 13))
switchAddrTrackInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 3))
switchAddrPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1))
switchAddrPortTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1, 1))
switchAddrPortEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1, 1, 1))
switchAddrPortIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1, 1, 1, 1))
switchPortMonitorInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 7))
switchPortMonitorTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 7, 4))
switchPortMonitorEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 7, 4, 1))
switchPortMonitorIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 7, 4, 1, 1))
switchPortMonitorMessageStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 7, 4, 1, 3))
switchAddrStaticInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 4))
switchAddrPortPackMaxCount = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 3, 1, 1, 1, 6))
switchAddrStaticPackMaxCount = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 4))
switchAddrStaticTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 6))
switchAddrStaticEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 6, 1))
switchAddrStaticIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 6, 1, 1))
switchAddrStaticSetAddress = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 4, 6, 1, 2))
switchThresholdInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 5))
basicThresholdTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4))
basicThresholdTableEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1))
switchThresholdPort = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1, 5))
switchThresholdType = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1, 6))
switchThresholdUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1, 4))
switchThresholdCounter = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 5, 4, 1, 9))
switchSecureAddrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 6))
switchAddrSecureTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4))
switchAddrSecureEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4, 1))
switchAddrSecurePortIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4, 1, 1))
switchAddrSecureIndex = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4, 1, 2))
switchAddrSecureAddress = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 6, 4, 1, 3))
switchVirtualLanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 8))
switchVirtualLanMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 8, 5))
switchPowerLinkInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 9))
switchPowerLinkOperationMode = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 2))
switchPowerLinkUserSettingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 5))
switchPowerLinkUserOperationMode = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 5, 1))
switchPowerLinkUserRange = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 5, 2))
switchPowerLinkStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 1, 9, 7))
switchTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 13))
switchTrapStaticCollisionAddress = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 13, 1))
switchTrapStaticCollisionAddress2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 13, 2))
switchTrapFilterCollisionAddress = MibIdentifier((1, 3, 6, 1, 4, 1, 1101, 2, 13, 13, 3))
dot1dStpPortTable = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 2, 15))
dot1dStpPortEntry = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 2, 15, 1))
dot1dStpPort = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 1))
newRoot = NotificationType((1, 3, 6, 1, 2, 1, 17) + (0,1)).setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: newRoot.setDescription(' Become the new root of the Spanning Tree.')
topologyChange = NotificationType((1, 3, 6, 1, 2, 1, 17) + (0,2)).setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: topologyChange.setDescription(' Spanning tree topology change.')
rptr_Reset = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,256)).setLabel("rptr-Reset").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: rptr_Reset.setDescription(' Successfully reset the switching hub.')
rptr_FReset1 = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,257)).setLabel("rptr-FReset1").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: rptr_FReset1.setDescription(' Fattory reset of the switching hub is successful.')
rptr_Port_Enabled = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,288)).setLabel("rptr-Port-Enabled").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "rptrPortGroupIndex"), ("TWTRAP-MIB", "rptrPortIndex"))
if mibBuilder.loadTexts: rptr_Port_Enabled.setDescription(' Enable a port.')
rptr_Port_Disabled = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,289)).setLabel("rptr-Port-Disabled").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "rptrPortGroupIndex"), ("TWTRAP-MIB", "rptrPortIndex"))
if mibBuilder.loadTexts: rptr_Port_Disabled.setDescription(' Disable a port.')
rptr_Port_Link_Up = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,292)).setLabel("rptr-Port-Link-Up").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "rptrPortGroupIndex"), ("TWTRAP-MIB", "rptrPortIndex"))
if mibBuilder.loadTexts: rptr_Port_Link_Up.setDescription(' Link state of a port has been changed from down to up.')
rptr_Port_Link_Down = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,293)).setLabel("rptr-Port-Link-Down").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "rptrPortGroupIndex"), ("TWTRAP-MIB", "rptrPortIndex"))
if mibBuilder.loadTexts: rptr_Port_Link_Down.setDescription(' Link state of a port has been changed from up to down.')
switch_Unit_Power_Status = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,512)).setLabel("switch-Unit-Power-Status").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "basicSwitchPowerState"))
if mibBuilder.loadTexts: switch_Unit_Power_Status.setDescription(' The power supply of the switching hub is changed.')
switch_Port_Monitor_Rx_CBPDU = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,514)).setLabel("switch-Port-Monitor-Rx-CBPDU").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "dot1dStpPort"), ("TWTRAP-MIB", "switchPortMonitorIndex"))
if mibBuilder.loadTexts: switch_Port_Monitor_Rx_CBPDU.setDescription(' The monitoring port received a configuration BPDU.')
switch_Port_Duplex_Change = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,532)).setLabel("switch-Port-Duplex-Change").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortIndex"), ("TWTRAP-MIB", "switchPortFullDuplex"))
if mibBuilder.loadTexts: switch_Port_Duplex_Change.setDescription(' Duplex status of the switching port is changed.')
switch_Port_Speed_Change = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,533)).setLabel("switch-Port-Speed-Change").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortIndex"), ("TWTRAP-MIB", "switchPortSpeed"))
if mibBuilder.loadTexts: switch_Port_Speed_Change.setDescription(' Speed of the switching port is changed.')
switch_Port_FlowControl_Changed = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,534)).setLabel("switch-Port-FlowControl-Changed").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortIndex"), ("TWTRAP-MIB", "switchPortFlowControl"))
if mibBuilder.loadTexts: switch_Port_FlowControl_Changed.setDescription(' Flow Control status of the switching port is changed due to auto-negotiate full duplex. ')
switch_Unit_Accumulate_reach = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,576)).setLabel("switch-Unit-Accumulate-reach").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchThresholdUnit"), ("TWTRAP-MIB", "switchThresholdType"), ("TWTRAP-MIB", "switchThresholdCounter"))
if mibBuilder.loadTexts: switch_Unit_Accumulate_reach.setDescription(' ')
switch_Unit_Rate_notification = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,577)).setLabel("switch-Unit-Rate-notification").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchThresholdUnit"), ("TWTRAP-MIB", "switchThresholdType"), ("TWTRAP-MIB", "switchThresholdCounter"))
if mibBuilder.loadTexts: switch_Unit_Rate_notification.setDescription(' ')
switch_Port_Accumulate_reach = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,579)).setLabel("switch-Port-Accumulate-reach").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchThresholdUnit"), ("TWTRAP-MIB", "switchThresholdPort"), ("TWTRAP-MIB", "switchThresholdType"), ("TWTRAP-MIB", "switchThresholdCounter"))
if mibBuilder.loadTexts: switch_Port_Accumulate_reach.setDescription(' ')
switch_Port_Rate_notification = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,580)).setLabel("switch-Port-Rate-notification").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchThresholdUnit"), ("TWTRAP-MIB", "switchThresholdPort"), ("TWTRAP-MIB", "switchThresholdType"), ("TWTRAP-MIB", "switchThresholdCounter"))
if mibBuilder.loadTexts: switch_Port_Rate_notification.setDescription(' ')
switch_Security_On = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,592)).setLabel("switch-Security-On").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: switch_Security_On.setDescription(' Enable filter function.')
switch_Security_Off = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,593)).setLabel("switch-Security-Off").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: switch_Security_Off.setDescription(' Disable filter function.')
switch_Security_Addr_Collision = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,595)).setLabel("switch-Security-Addr-Collision").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchTrapFilterCollisionAddress"), ("TWTRAP-MIB", "switchAddrSecurePortIndex"), ("TWTRAP-MIB", "switchAddrSecureIndex"), ("TWTRAP-MIB", "switchAddrSecureAddress"))
if mibBuilder.loadTexts: switch_Security_Addr_Collision.setDescription(' Set a collision address in filter table.')
switch_Security_Reserved_Addr_Collision = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,596)).setLabel("switch-Security-Reserved-Addr-Collision").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchTrapFilterCollisionAddress"), ("TWTRAP-MIB", "switchAddrStaticIndex"), ("TWTRAP-MIB", "switchAddrStaticSetAddress"))
if mibBuilder.loadTexts: switch_Security_Reserved_Addr_Collision.setDescription(' Set an address collision with reserved address.')
switch_Port_Monitor_On = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,608)).setLabel("switch-Port-Monitor-On").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: switch_Port_Monitor_On.setDescription(' Enable port monitor function.')
switch_Port_Monitor_Off = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,609)).setLabel("switch-Port-Monitor-Off").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: switch_Port_Monitor_Off.setDescription(' Disable port monitor function.')
switch_Port_Monitor_Port_On = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,610)).setLabel("switch-Port-Monitor-Port-On").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortIndex"))
if mibBuilder.loadTexts: switch_Port_Monitor_Port_On.setDescription(' Port monitor function is active on the specific port.')
switch_Port_Monitor_Port_Off = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,611)).setLabel("switch-Port-Monitor-Port-Off").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortIndex"))
if mibBuilder.loadTexts: switch_Port_Monitor_Port_Off.setDescription(' Port monitor function is removed from the specific port.')
switch_Port_Monitor_Active = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,612)).setLabel("switch-Port-Monitor-Active").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortMonitorIndex"))
if mibBuilder.loadTexts: switch_Port_Monitor_Active.setDescription(' Enable port monitor function of a monitor group.')
switch_Port_Monitor_Removed = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,613)).setLabel("switch-Port-Monitor-Removed").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortMonitorIndex"))
if mibBuilder.loadTexts: switch_Port_Monitor_Removed.setDescription(' Disable port monitor function of a monitor group.')
switch_Port_Monitor_Error = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,614)).setLabel("switch-Port-Monitor-Error").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortMonitorIndex"), ("TWTRAP-MIB", "switchPortMonitorMessageStatus"))
if mibBuilder.loadTexts: switch_Port_Monitor_Error.setDescription(' Operation error for port monitor function.')
switch_Virtual_LAN_On = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,624)).setLabel("switch-Virtual-LAN-On").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: switch_Virtual_LAN_On.setDescription(' Enable Virtual LAN function.')
switch_Virtual_LAN_Off = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,625)).setLabel("switch-Virtual-LAN-Off").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"))
if mibBuilder.loadTexts: switch_Virtual_LAN_Off.setDescription(' Disable Virtual LAN function.')
switch_VL_Port_On = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,626)).setLabel("switch-VL-Port-On").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortIndex"))
if mibBuilder.loadTexts: switch_VL_Port_On.setDescription(' Virtual LAN function is active on the specific port.')
switch_VL_Port_Off = NotificationType((1, 3, 6, 1, 4, 1, 1101, 2, 10, 1) + (0,627)).setLabel("switch-VL-Port-Off").setObjects(("TWTRAP-MIB", "devMonTrapReportLevel"), ("TWTRAP-MIB", "switchPortIndex"))
if mibBuilder.loadTexts: switch_VL_Port_Off.setDescription(' Virtual LAN function is removed from the specific port.')
mibBuilder.exportSymbols("TWTRAP-MIB", switchPortMonitorIndex=switchPortMonitorIndex, switchPortMonitorInfo=switchPortMonitorInfo, rptrPortGroupIndex=rptrPortGroupIndex, rptrAddrTrackPackage=rptrAddrTrackPackage, basicUnitTable=basicUnitTable, switchAddrStaticInfo=switchAddrStaticInfo, devMonitorInfo=devMonitorInfo, switch_Port_Duplex_Change=switch_Port_Duplex_Change, switchBasicPortInfo=switchBasicPortInfo, switchAddrPortInfo=switchAddrPortInfo, MacAddress=MacAddress, switchThresholdCounter=switchThresholdCounter, mib_2=mib_2, switch_FE1200PLUS=switch_FE1200PLUS, dot1dStpPortEntry=dot1dStpPortEntry, basicPortTable=basicPortTable, switchThresholdPort=switchThresholdPort, private=private, switch_Common_MIB=switch_Common_MIB, dot1dTp=dot1dTp, switch_Security_Addr_Collision=switch_Security_Addr_Collision, switch_VL_Port_On=switch_VL_Port_On, addrTrackPortEntry=addrTrackPortEntry, mgmt=mgmt, switch_Port_Accumulate_reach=switch_Port_Accumulate_reach, switchAddrStaticIndex=switchAddrStaticIndex, basicPortIndex=basicPortIndex, rptrAddrTrackGroupInfo=rptrAddrTrackGroupInfo, switch_FE1200=switch_FE1200, switchAddrStaticTable=switchAddrStaticTable, switchAddrSecureAddress=switchAddrSecureAddress, directory=directory, common=common, switchCmsAddrTrackPackage=switchCmsAddrTrackPackage, switch_Virtual_LAN_Off=switch_Virtual_LAN_Off, rptr_FReset1=rptr_FReset1, rptrPortInfo=rptrPortInfo, rptr_Port_Link_Up=rptr_Port_Link_Up, experimental=experimental, switchTrapStaticCollisionAddress=switchTrapStaticCollisionAddress, switch_Security_Reserved_Addr_Collision=switch_Security_Reserved_Addr_Collision, switchThresholdUnit=switchThresholdUnit, switch_Port_Monitor_Error=switch_Port_Monitor_Error, rptrPortEntry=rptrPortEntry, switchTrapFilterCollisionAddress=switchTrapFilterCollisionAddress, switchAddrPortTable=switchAddrPortTable, switch_Security_On=switch_Security_On, switch_Port_Monitor_Port_On=switch_Port_Monitor_Port_On, switchPortMonitorMessageStatus=switchPortMonitorMessageStatus, switchAddrSecurePortIndex=switchAddrSecurePortIndex, npi_Switching_MIB=npi_Switching_MIB, switchPortTable=switchPortTable, switchPortMonitorEntry=switchPortMonitorEntry, rptr_Port_Disabled=rptr_Port_Disabled, switchAddrStaticSetAddress=switchAddrStaticSetAddress, switchPortIndex=switchPortIndex, switchCmsBasicClusterInfo=switchCmsBasicClusterInfo, switchAddrPortEntry=switchAddrPortEntry, switchSecureAddrInfo=switchSecureAddrInfo, switch_Port_FlowControl_Changed=switch_Port_FlowControl_Changed, switch_Port_Monitor_Off=switch_Port_Monitor_Off, switchAddrStaticEntry=switchAddrStaticEntry, switchPortSpeed=switchPortSpeed, addrTrackPortPortIndex=addrTrackPortPortIndex, devDeviceInfo=devDeviceInfo, dot1dBase=dot1dBase, switchThresholdType=switchThresholdType, basicSwitchPowerState=basicSwitchPowerState, basicThresholdTableEntry=basicThresholdTableEntry, switch_TidalWave=switch_TidalWave, dot1dSr=dot1dSr, switchPortEntry=switchPortEntry, rptr_Port_Link_Down=rptr_Port_Link_Down, switch_Port_Monitor_Port_Off=switch_Port_Monitor_Port_Off, rptrMonitorPortInfo=rptrMonitorPortInfo, switchCmsBasicUnitInfo=switchCmsBasicUnitInfo, devMonTrapReportLevel=devMonTrapReportLevel, snmpDot3RptrMgt=snmpDot3RptrMgt, switch_Port_Monitor_Active=switch_Port_Monitor_Active, rptr_Port_Enabled=rptr_Port_Enabled, rptrMonitorRptrInfo=rptrMonitorRptrInfo, switchPowerLinkUserSettingInfo=switchPowerLinkUserSettingInfo, switchTrapStaticCollisionAddress2=switchTrapStaticCollisionAddress2, devActionInfo=devActionInfo, switchAddrStaticPackMaxCount=switchAddrStaticPackMaxCount, switch_Cascade_MIB=switch_Cascade_MIB, switch_Unit_Power_Status=switch_Unit_Power_Status, switch_Unit_Accumulate_reach=switch_Unit_Accumulate_reach, enterprises=enterprises, switchAddrSecureEntry=switchAddrSecureEntry, switchVirtualLanInfo=switchVirtualLanInfo, rptrPortIndex=rptrPortIndex, switchPortFullDuplex=switchPortFullDuplex, switch_VL_Port_Off=switch_VL_Port_Off, dot1dStatic=dot1dStatic, switchVirtualLanMessage=switchVirtualLanMessage, switch_Security_Off=switch_Security_Off, switchPowerLinkOperationMode=switchPowerLinkOperationMode, rptrRptrInfo=rptrRptrInfo, switchBasicHubInfo=switchBasicHubInfo, switch_Port_Monitor_On=switch_Port_Monitor_On, switchAddrTrackInfo=switchAddrTrackInfo, switchCmsBasicPortInfo=switchCmsBasicPortInfo, rptrMonitorGroupInfo=rptrMonitorGroupInfo, switchThresholdInfo=switchThresholdInfo, basicPortEntry=basicPortEntry, switchCmsAddrTrackPortInfo=switchCmsAddrTrackPortInfo, newRoot=newRoot, switchAddrSecureIndex=switchAddrSecureIndex, rptrMonitorPackage=rptrMonitorPackage, addrTrackPortTable=addrTrackPortTable, switchPowerLinkStatus=switchPowerLinkStatus, switch_Port_Speed_Change=switch_Port_Speed_Change, rptr_Reset=rptr_Reset, npi=npi, rptrPortTable=rptrPortTable, basicUnitIndex=basicUnitIndex, dot1dStpPortTable=dot1dStpPortTable, basicUnitEntry=basicUnitEntry, switchAddrPortIndex=switchAddrPortIndex, rptrAddrTrackPortInfo=rptrAddrTrackPortInfo, switch_Port_Monitor_Removed=switch_Port_Monitor_Removed, dot1dStpPort=dot1dStpPort, switchTrapInfo=switchTrapInfo, switchPowerLinkUserRange=switchPowerLinkUserRange, topologyChange=topologyChange, rptrAddrTrackRptrInfo=rptrAddrTrackRptrInfo, switch_Port_Monitor_Rx_CBPDU=switch_Port_Monitor_Rx_CBPDU, basicThresholdTable=basicThresholdTable, switchAddrSecureTable=switchAddrSecureTable, switchPowerLinkUserOperationMode=switchPowerLinkUserOperationMode, switch_Port_Rate_notification=switch_Port_Rate_notification, switch_DS24=switch_DS24, dot1dBridge=dot1dBridge, rptrBasicPackage=rptrBasicPackage, switchAddrPortPackMaxCount=switchAddrPortPackMaxCount, switchCmsBasicPackage=switchCmsBasicPackage, switchPowerLinkInfo=switchPowerLinkInfo, rptrGroupInfo=rptrGroupInfo, addrTrackPortUnitIndex=addrTrackPortUnitIndex, switch_Virtual_LAN_On=switch_Virtual_LAN_On, switchPortFlowControl=switchPortFlowControl, switch_Unit_Rate_notification=switch_Unit_Rate_notification, basicPortUnitIndex=basicPortUnitIndex, dot1dStp=dot1dStp, switchPortMonitorTable=switchPortMonitorTable)
