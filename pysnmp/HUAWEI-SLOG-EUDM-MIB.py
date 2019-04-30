#
# PySNMP MIB module HUAWEI-SLOG-EUDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SLOG-EUDM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:36:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ObjectIdentity, ModuleIdentity, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Unsigned32, MibIdentifier, NotificationType, Bits, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "ModuleIdentity", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Unsigned32", "MibIdentifier", "NotificationType", "Bits", "IpAddress", "Integer32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
hwSLOGEudm = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2))
if mibBuilder.loadTexts: hwSLOGEudm.setLastUpdated('200304081633Z')
if mibBuilder.loadTexts: hwSLOGEudm.setOrganization('Huawei Technologies co.,Ltd.')
class FlowLogType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("flowLogSysLog", 1), ("flowLogExport", 2))

hwSLOG = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16))
hwSLogEudmGlobalCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1))
hwSLogEudmAttackLogInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSLogEudmAttackLogInterval.setStatus('current')
hwSLogEudmFlowLogInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSLogEudmFlowLogInterval.setStatus('current')
hwSLogEudmStreamLogInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSLogEudmStreamLogInterval.setStatus('current')
hwSLogEudmFlowLogMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 4), FlowLogType().clone('flowLogSysLog')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSLogEudmFlowLogMode.setStatus('current')
hwSLogEudmServerIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSLogEudmServerIP.setStatus('current')
hwSLogEudmServerPort = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSLogEudmServerPort.setStatus('current')
hwSLogInterZoneEnableCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2))
hwSLogEudmFlowLogEnableTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1), )
if mibBuilder.loadTexts: hwSLogEudmFlowLogEnableTable.setStatus('current')
hwSLogEudmFlowLogEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1), ).setIndexNames((0, "HUAWEI-SLOG-EUDM-MIB", "hwSLogFlowEnableZoneID1"), (0, "HUAWEI-SLOG-EUDM-MIB", "hwSLogFlowEnableZoneID2"))
if mibBuilder.loadTexts: hwSLogEudmFlowLogEnableEntry.setStatus('current')
hwSLogFlowEnableZoneID1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwSLogFlowEnableZoneID1.setStatus('current')
hwSLogFlowEnableZoneID2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: hwSLogFlowEnableZoneID2.setStatus('current')
hwSLogEudmFlowEnableFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSLogEudmFlowEnableFlag.setStatus('current')
hwSLogEudmEnableHostAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 3999), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSLogEudmEnableHostAcl.setStatus('current')
hwSLOGEudmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3))
hwSLOGEudmCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3, 1))
hwSLOGEudmMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3, 2))
hwSLOGEudmGlobalCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3, 2, 1)).setObjects(("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmAttackLogInterval"), ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmStreamLogInterval"), ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmFlowLogMode"), ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmFlowLogInterval"), ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmServerIP"), ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmServerPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSLOGEudmGlobalCfgGroup = hwSLOGEudmGlobalCfgGroup.setStatus('current')
hwSLOGEudmFlowLogEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3, 2, 2)).setObjects(("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmFlowEnableFlag"), ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmEnableHostAcl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSLOGEudmFlowLogEnableGroup = hwSLOGEudmFlowLogEnableGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SLOG-EUDM-MIB", hwSLOG=hwSLOG, hwSLogFlowEnableZoneID1=hwSLogFlowEnableZoneID1, FlowLogType=FlowLogType, hwSLogEudmServerIP=hwSLogEudmServerIP, hwSLOGEudmMibGroups=hwSLOGEudmMibGroups, hwSLogEudmServerPort=hwSLogEudmServerPort, hwSLOGEudmFlowLogEnableGroup=hwSLOGEudmFlowLogEnableGroup, hwSLogEudmStreamLogInterval=hwSLogEudmStreamLogInterval, hwSLogEudmAttackLogInterval=hwSLogEudmAttackLogInterval, PYSNMP_MODULE_ID=hwSLOGEudm, hwSLogEudmFlowLogEnableEntry=hwSLogEudmFlowLogEnableEntry, hwSLOGEudmCompliance=hwSLOGEudmCompliance, hwSLogEudmEnableHostAcl=hwSLogEudmEnableHostAcl, hwSLogEudmFlowLogMode=hwSLogEudmFlowLogMode, hwSLogInterZoneEnableCfg=hwSLogInterZoneEnableCfg, hwSLOGEudmConformance=hwSLOGEudmConformance, hwSLogEudmFlowEnableFlag=hwSLogEudmFlowEnableFlag, hwSLogFlowEnableZoneID2=hwSLogFlowEnableZoneID2, hwSLogEudmFlowLogInterval=hwSLogEudmFlowLogInterval, hwSLOGEudm=hwSLOGEudm, hwSLOGEudmGlobalCfgGroup=hwSLOGEudmGlobalCfgGroup, hwSLogEudmFlowLogEnableTable=hwSLogEudmFlowLogEnableTable, hwSLogEudmGlobalCfg=hwSLogEudmGlobalCfg)