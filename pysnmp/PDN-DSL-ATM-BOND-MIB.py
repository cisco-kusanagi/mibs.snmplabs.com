#
# PySNMP MIB module PDN-DSL-ATM-BOND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DSL-ATM-BOND-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, ModuleIdentity, Unsigned32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, ObjectIdentity, IpAddress, Counter32, MibIdentifier, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Unsigned32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "ObjectIdentity", "IpAddress", "Counter32", "MibIdentifier", "Bits", "iso")
RowStatus, TruthValue, DisplayString, TextualConvention, DateAndTime, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention", "DateAndTime", "TestAndIncr")
pdnDslAtmBondMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33))
pdnDslAtmBondMIB.setRevisions(('2005-08-03 00:00', '2005-08-01 00:00', '2005-07-26 00:00', '2005-06-07 00:00',))
if mibBuilder.loadTexts: pdnDslAtmBondMIB.setLastUpdated('200508030000Z')
if mibBuilder.loadTexts: pdnDslAtmBondMIB.setOrganization('Paradyne Networks, Inc. MIB Working Group')
pdnDslAtmBondNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 0))
pdnDslAtmBondObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1))
pdnDslAtmBondAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 2))
pdnDslAtmBondConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3))
class PdnDslAtmBondGroupIndexTC(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PdnDslAtmBondGroupIdentityTC(TextualConvention, Unsigned32):
    reference = "T1E1.4, Section 9.1.4, `Format of the Autonomous Status Message (ASM)', Table 9-1`ASM Message Format'. G.998.1, Section 9.1.4, `Format of the Autonomous Status Message (ASM)', Table 9-1`ASM Message Format'."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class PdnDslAtmBondGroupBearerNumberTC(TextualConvention, Unsigned32):
    reference = "T1E1.4, Section 9.1.4, `Format of the Autonomous Status Message (ASM)', Table 9-1`ASM Message Format'. G.998.1, Section 9.1.4, `Format of the Autonomous Status Message (ASM)', Table 9-1`ASM Message Format'."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4)

class PdnDslAtmBondLinkStatusAsmTC(TextualConvention, Integer32):
    reference = "T1E1.4, Section 9.1.4, `Format of the Autonomous Status Message (ASM)', Table 9-1`ASM Message Format'. G.998.1, Section 9.1.4, `Format of the Autonomous Status Message (ASM)', Table 9-1`ASM Message Format'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notProvisioned", 1), ("shouldNotBeUsed", 2), ("acceptableToCarryBondedTraffic", 3), ("selectedToCarryBondedTraffic", 4))

class PdnDslAtmBondAsmRxStatusTC(TextualConvention, Integer32):
    reference = "T1E1.4, Section 9.1.3, `Frequency of Autonomous Status Messages'. G.998.1, Section 9.1.3, `Frequency of Autonomous Status Messages'. T1E1.4, Section 9.1.4, `Format of the Autonomous Status Message (ASM)', Table 9-1`ASM Message Format'. G.998.1, Section 9.1.4, `Format of the Autonomous Status Message (ASM)', Table 9-1`ASM Message Format'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("receivedASM", 1), ("notReceivedASM", 2))

class PdnDslAtmBondGroupDataRateTC(TextualConvention, Integer32):
    reference = "T1E1.4, Section 11.4.1, `Group Provisioning'. G.998.1, Section 11.4.1, `Group Provisioning'."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), )
class PdnDslAtmBondGroupDiffDelayTolTC(TextualConvention, Unsigned32):
    reference = "T1E1.4, Section 11.4.1, `Group Provisioning'. G.998.1, Section 11.4.1, `Group Provisioning'."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class PdnDslAtmBondGroupStatusTC(TextualConvention, Integer32):
    reference = "T1E1.4, Section 11.4.2, `Group Performance'. G.998.1, Section 11.4.2, `Group Performance'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("operational", 1), ("unavailable", 2))

class PdnDslAtmBondGroupFailReasonTC(TextualConvention, Integer32):
    reference = "T1E1.4, Section 11.4.3, `Group Failures'. G.998.1, Section 11.4.3, `Group Failures'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notApplicable", 1), ("unknown", 2), ("atucMinDataRateNotMet", 3), ("aturMinDataRateNotMet", 4), ("atucDiffDelayExceeded", 5), ("aturDiffDelayExceeded", 6))

pdnDslAtmBondNextGroupIndex = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDslAtmBondNextGroupIndex.setStatus('current')
pdnDslAtmBondNbrOfGroups = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondNbrOfGroups.setStatus('current')
pdnDslAtmBondGroupTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3), )
if mibBuilder.loadTexts: pdnDslAtmBondGroupTable.setStatus('current')
pdnDslAtmBondGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1), ).setIndexNames((0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"))
if mibBuilder.loadTexts: pdnDslAtmBondGroupEntry.setStatus('current')
pdnDslAtmBondGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 1), PdnDslAtmBondGroupIndexTC())
if mibBuilder.loadTexts: pdnDslAtmBondGroupIndex.setStatus('current')
pdnDslAtmBondGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupRowStatus.setStatus('current')
pdnDslAtmBondGroupNbrRefs = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondGroupNbrRefs.setStatus('current')
pdnDslAtmBondGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondGroupIfIndex.setStatus('current')
pdnDslAtmBondGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 5), PdnDslAtmBondGroupIdentityTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupID.setStatus('current')
pdnDslAtmBondGroupAlarmConfProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 6), SnmpAdminString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 32), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupAlarmConfProfileName.setStatus('current')
pdnDslAtmBondGroupAtucMaxNetDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 7), PdnDslAtmBondGroupDataRateTC()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupAtucMaxNetDataRate.setStatus('current')
pdnDslAtmBondGroupAturMaxNetDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 8), PdnDslAtmBondGroupDataRateTC()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupAturMaxNetDataRate.setStatus('current')
pdnDslAtmBondGroupAtucMinNetDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 9), PdnDslAtmBondGroupDataRateTC()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupAtucMinNetDataRate.setStatus('current')
pdnDslAtmBondGroupAturMinNetDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 10), PdnDslAtmBondGroupDataRateTC()).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupAturMinNetDataRate.setStatus('current')
pdnDslAtmBondGroupAtucDiffDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 11), PdnDslAtmBondGroupDiffDelayTolTC()).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupAtucDiffDelay.setStatus('current')
pdnDslAtmBondGroupAturDiffDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 12), PdnDslAtmBondGroupDiffDelayTolTC()).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupAturDiffDelay.setStatus('current')
pdnDslAtmBondGroupStatusNotifyEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 3, 1, 13), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondGroupStatusNotifyEnabled.setStatus('current')
pdnDslAtmBondMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4), )
if mibBuilder.loadTexts: pdnDslAtmBondMappingTable.setStatus('current')
pdnDslAtmBondMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1), ).setIndexNames((0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondDslIfIndex"), (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondBearerNbr"))
if mibBuilder.loadTexts: pdnDslAtmBondMappingEntry.setStatus('current')
pdnDslAtmBondDslIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: pdnDslAtmBondDslIfIndex.setStatus('current')
pdnDslAtmBondBearerNbr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1, 2), PdnDslAtmBondGroupBearerNumberTC())
if mibBuilder.loadTexts: pdnDslAtmBondBearerNbr.setStatus('current')
pdnDslAtmBondMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondMappingRowStatus.setStatus('current')
pdnDslAtmBondMappingGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 4, 1, 4), PdnDslAtmBondGroupIndexTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondMappingGroupIndex.setStatus('current')
pdnDslAtmBondGroupIndexMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 5), )
if mibBuilder.loadTexts: pdnDslAtmBondGroupIndexMappingTable.setStatus('current')
pdnDslAtmBondGroupIndexMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 5, 1), ).setIndexNames((0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"))
if mibBuilder.loadTexts: pdnDslAtmBondGroupIndexMappingEntry.setStatus('current')
pdnDslAtmBondGroupIndexMappingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 5, 1, 1), PdnDslAtmBondGroupIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondGroupIndexMappingIndex.setStatus('current')
pdnDslAtmBondGroupInvMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 6), )
if mibBuilder.loadTexts: pdnDslAtmBondGroupInvMappingTable.setStatus('current')
pdnDslAtmBondGroupInvMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 6, 1), ).setIndexNames((0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"), (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondDslIfIndex"))
if mibBuilder.loadTexts: pdnDslAtmBondGroupInvMappingEntry.setStatus('current')
pdnDslAtmBondInvMappingBearerNbr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 6, 1, 1), PdnDslAtmBondGroupBearerNumberTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondInvMappingBearerNbr.setStatus('current')
pdnDslAtmBondPerfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7), )
if mibBuilder.loadTexts: pdnDslAtmBondPerfTable.setStatus('current')
pdnDslAtmBondPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1), ).setIndexNames((0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"))
if mibBuilder.loadTexts: pdnDslAtmBondPerfEntry.setStatus('current')
pdnDslAtmBondPerfCurrAtucNetDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 1), PdnDslAtmBondGroupDataRateTC()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfCurrAtucNetDataRate.setStatus('current')
pdnDslAtmBondPerfCurrAturNetDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 2), PdnDslAtmBondGroupDataRateTC()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfCurrAturNetDataRate.setStatus('current')
pdnDslAtmBondPerfPrevAtucNetDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 3), PdnDslAtmBondGroupDataRateTC()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfPrevAtucNetDataRate.setStatus('current')
pdnDslAtmBondPerfPrevAturNetDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 4), PdnDslAtmBondGroupDataRateTC()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfPrevAturNetDataRate.setStatus('current')
pdnDslAtmBondPerfGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 5), PdnDslAtmBondGroupStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfGroupStatus.setStatus('current')
pdnDslAtmBondPerfFailReason = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 6), PdnDslAtmBondGroupFailReasonTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfFailReason.setStatus('current')
pdnDslAtmBondPerfFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfFailCount.setStatus('current')
pdnDslAtmBondPerfRunTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 8), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfRunTime.setStatus('current')
pdnDslAtmBondPerfUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 9), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfUAS.setStatus('current')
pdnDslAtmBondPerfAtucRxCellLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfAtucRxCellLoss.setStatus('current')
pdnDslAtmBondPerfAturRxCellLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 7, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondPerfAturRxCellLoss.setStatus('current')
pdnDslAtmBond15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8), )
if mibBuilder.loadTexts: pdnDslAtmBond15MinIntervalTable.setStatus('current')
pdnDslAtmBond15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1), ).setIndexNames((0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"), (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalNumber"))
if mibBuilder.loadTexts: pdnDslAtmBond15MinIntervalEntry.setStatus('current')
pdnDslAtmBond15MinIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: pdnDslAtmBond15MinIntervalNumber.setStatus('current')
pdnDslAtmBond15MinIntervalStartDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond15MinIntervalStartDateAndTime.setStatus('current')
pdnDslAtmBond15MinIntervalFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond15MinIntervalFailCount.setStatus('current')
pdnDslAtmBond15MinIntervalRunTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond15MinIntervalRunTime.setStatus('current')
pdnDslAtmBond15MinIntervalUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond15MinIntervalUAS.setStatus('current')
pdnDslAtmBond15MinIntervalAtucRxCellLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond15MinIntervalAtucRxCellLoss.setStatus('current')
pdnDslAtmBond15MinIntervalAturRxCellLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 8, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond15MinIntervalAturRxCellLoss.setStatus('current')
pdnDslAtmBond1DayIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9), )
if mibBuilder.loadTexts: pdnDslAtmBond1DayIntervalTable.setStatus('current')
pdnDslAtmBond1DayIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1), ).setIndexNames((0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"), (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalNumber"))
if mibBuilder.loadTexts: pdnDslAtmBond1DayIntervalEntry.setStatus('current')
pdnDslAtmBond1DayIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)))
if mibBuilder.loadTexts: pdnDslAtmBond1DayIntervalNumber.setStatus('current')
pdnDslAtmBond1DayIntervalStartDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond1DayIntervalStartDateAndTime.setStatus('current')
pdnDslAtmBond1DayIntervalFailCount = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond1DayIntervalFailCount.setStatus('current')
pdnDslAtmBond1DayIntervalRunTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond1DayIntervalRunTime.setStatus('current')
pdnDslAtmBond1DayIntervalUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond1DayIntervalUAS.setStatus('current')
pdnDslAtmBond1DayIntervalAtucRxCellLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond1DayIntervalAtucRxCellLoss.setStatus('current')
pdnDslAtmBond1DayIntervalAturRxCellLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 9, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBond1DayIntervalAturRxCellLoss.setStatus('current')
pdnDslAtmBondLinkTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10), )
if mibBuilder.loadTexts: pdnDslAtmBondLinkTable.setStatus('current')
pdnDslAtmBondLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1), ).setIndexNames((0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndex"), (0, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondDslIfIndex"))
if mibBuilder.loadTexts: pdnDslAtmBondLinkEntry.setStatus('current')
pdnDslAtmBondLinkAtucRxLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 1), PdnDslAtmBondLinkStatusAsmTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondLinkAtucRxLinkStatus.setStatus('current')
pdnDslAtmBondLinkAturRxLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 2), PdnDslAtmBondLinkStatusAsmTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondLinkAturRxLinkStatus.setStatus('current')
pdnDslAtmBondLinkAtucTxLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 3), PdnDslAtmBondLinkStatusAsmTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondLinkAtucTxLinkStatus.setStatus('current')
pdnDslAtmBondLinkAturTxLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 4), PdnDslAtmBondLinkStatusAsmTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondLinkAturTxLinkStatus.setStatus('current')
pdnDslAtmBondLinkAtucAsmRxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 5), PdnDslAtmBondAsmRxStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondLinkAtucAsmRxStatus.setStatus('current')
pdnDslAtmBondLinkAturAsmRxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 10, 1, 6), PdnDslAtmBondAsmRxStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondLinkAturAsmRxStatus.setStatus('current')
pdnDslAtmBondAlarmConfProfileTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11), )
if mibBuilder.loadTexts: pdnDslAtmBondAlarmConfProfileTable.setStatus('current')
pdnDslAtmBondAlarmConfProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1), ).setIndexNames((1, "PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfProfileName"))
if mibBuilder.loadTexts: pdnDslAtmBondAlarmConfProfileEntry.setStatus('current')
pdnDslAtmBondAlarmConfProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: pdnDslAtmBondAlarmConfProfileName.setStatus('current')
pdnDslAtmBondAlarmConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondAlarmConfRowStatus.setStatus('current')
pdnDslAtmBondAlarmConfNbrRefs = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnDslAtmBondAlarmConfNbrRefs.setStatus('current')
pdnDslAtmBondAlarmConfAtucThreshRateUp = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondAlarmConfAtucThreshRateUp.setStatus('current')
pdnDslAtmBondAlarmConfAturThreshRateUp = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondAlarmConfAturThreshRateUp.setStatus('current')
pdnDslAtmBondAlarmConfAtucThreshRateDown = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondAlarmConfAtucThreshRateDown.setStatus('current')
pdnDslAtmBondAlarmConfAturThreshRateDown = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 1, 11, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('bps').setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnDslAtmBondAlarmConfAturThreshRateDown.setStatus('current')
pdnDslAtmBondAtucRateChange = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 0, 1)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfCurrAtucNetDataRate"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfPrevAtucNetDataRate"))
if mibBuilder.loadTexts: pdnDslAtmBondAtucRateChange.setStatus('current')
pdnDslAtmBondAturRateChange = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 0, 2)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfCurrAturNetDataRate"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfPrevAturNetDataRate"))
if mibBuilder.loadTexts: pdnDslAtmBondAturRateChange.setStatus('current')
pdnDslAtmBondGroupStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 0, 3)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfGroupStatus"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfFailReason"))
if mibBuilder.loadTexts: pdnDslAtmBondGroupStatusChange.setStatus('current')
pdnDslAtmBondCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 1))
pdnDslAtmBondGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2))
pdnDslAtmBondMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 1, 1)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondMappingGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfAggDataRateGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfBondGroupStatusGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondNotificationsGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondMaxRateGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondMinRateGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondDiffDelayGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupStatusNotifyEnabledGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondIndexMappingGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondInvMappingGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondDateAndTimeGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondRunTimeGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondRxCellLossGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfFailReasonGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondFailCountGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondUASGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondTrafficCapGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslATmBondAsmRxStatusGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfProfileGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAtucThreshRateGroup"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAturThreshRateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondMIBCompliance = pdnDslAtmBondMIBCompliance.setStatus('current')
pdnDslAtmBondObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1))
pdnDslAtmBondAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 2))
pdnDslAtmBondNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 3))
pdnDslAtmBondGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 1)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondNextGroupIndex"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondNbrOfGroups"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupRowStatus"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupNbrRefs"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIfIndex"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondGroup = pdnDslAtmBondGroup.setStatus('current')
pdnDslAtmBondMaxRateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 2)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAtucMaxNetDataRate"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAturMaxNetDataRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondMaxRateGroup = pdnDslAtmBondMaxRateGroup.setStatus('current')
pdnDslAtmBondMinRateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 3)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAtucMinNetDataRate"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAturMinNetDataRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondMinRateGroup = pdnDslAtmBondMinRateGroup.setStatus('current')
pdnDslAtmBondDiffDelayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 4)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAtucDiffDelay"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAturDiffDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondDiffDelayGroup = pdnDslAtmBondDiffDelayGroup.setStatus('current')
pdnDslAtmBondGroupStatusNotifyEnabledGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 5)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupStatusNotifyEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondGroupStatusNotifyEnabledGroup = pdnDslAtmBondGroupStatusNotifyEnabledGroup.setStatus('current')
pdnDslAtmBondMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 6)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondMappingRowStatus"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondMappingGroupIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondMappingGroup = pdnDslAtmBondMappingGroup.setStatus('current')
pdnDslAtmBondIndexMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 7)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupIndexMappingIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondIndexMappingGroup = pdnDslAtmBondIndexMappingGroup.setStatus('current')
pdnDslAtmBondInvMappingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 8)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondInvMappingBearerNbr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondInvMappingGroup = pdnDslAtmBondInvMappingGroup.setStatus('current')
pdnDslAtmBondPerfAggDataRateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 9)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfCurrAtucNetDataRate"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfCurrAturNetDataRate"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfPrevAtucNetDataRate"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfPrevAturNetDataRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondPerfAggDataRateGroup = pdnDslAtmBondPerfAggDataRateGroup.setStatus('current')
pdnDslAtmBondPerfBondGroupStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 10)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfGroupStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondPerfBondGroupStatusGroup = pdnDslAtmBondPerfBondGroupStatusGroup.setStatus('current')
pdnDslAtmBondDateAndTimeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 11)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalStartDateAndTime"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalStartDateAndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondDateAndTimeGroup = pdnDslAtmBondDateAndTimeGroup.setStatus('current')
pdnDslAtmBondRunTimeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 12)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfRunTime"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalRunTime"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalRunTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondRunTimeGroup = pdnDslAtmBondRunTimeGroup.setStatus('current')
pdnDslAtmBondRxCellLossGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 13)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfAtucRxCellLoss"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfAturRxCellLoss"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalAtucRxCellLoss"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalAturRxCellLoss"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalAtucRxCellLoss"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalAturRxCellLoss"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondRxCellLossGroup = pdnDslAtmBondRxCellLossGroup.setStatus('current')
pdnDslAtmBondPerfFailReasonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 14)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfFailReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondPerfFailReasonGroup = pdnDslAtmBondPerfFailReasonGroup.setStatus('current')
pdnDslAtmBondFailCountGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 15)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfFailCount"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalFailCount"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalFailCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondFailCountGroup = pdnDslAtmBondFailCountGroup.setStatus('current')
pdnDslAtmBondUASGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 16)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondPerfUAS"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond15MinIntervalUAS"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBond1DayIntervalUAS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondUASGroup = pdnDslAtmBondUASGroup.setStatus('current')
pdnDslAtmBondTrafficCapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 17)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAtucRxLinkStatus"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAturRxLinkStatus"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAtucTxLinkStatus"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAturTxLinkStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondTrafficCapGroup = pdnDslAtmBondTrafficCapGroup.setStatus('current')
pdnDslATmBondAsmRxStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 18)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAtucAsmRxStatus"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondLinkAturAsmRxStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslATmBondAsmRxStatusGroup = pdnDslATmBondAsmRxStatusGroup.setStatus('current')
pdnDslAtmBondAlarmConfProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 19)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupAlarmConfProfileName"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfRowStatus"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfNbrRefs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondAlarmConfProfileGroup = pdnDslAtmBondAlarmConfProfileGroup.setStatus('current')
pdnDslAtmBondAlarmConfAtucThreshRateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 20)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAtucThreshRateUp"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAtucThreshRateDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondAlarmConfAtucThreshRateGroup = pdnDslAtmBondAlarmConfAtucThreshRateGroup.setStatus('current')
pdnDslAtmBondAlarmConfAturThreshRateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 1, 21)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAturThreshRateUp"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAlarmConfAturThreshRateDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondAlarmConfAturThreshRateGroup = pdnDslAtmBondAlarmConfAturThreshRateGroup.setStatus('current')
pdnDslAtmBondNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 33, 3, 2, 3, 1)).setObjects(("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAtucRateChange"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondAturRateChange"), ("PDN-DSL-ATM-BOND-MIB", "pdnDslAtmBondGroupStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDslAtmBondNotificationsGroup = pdnDslAtmBondNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-DSL-ATM-BOND-MIB", pdnDslAtmBondPerfPrevAturNetDataRate=pdnDslAtmBondPerfPrevAturNetDataRate, pdnDslAtmBondPerfGroupStatus=pdnDslAtmBondPerfGroupStatus, pdnDslAtmBondGroupAtucMinNetDataRate=pdnDslAtmBondGroupAtucMinNetDataRate, pdnDslAtmBondAlarmConfRowStatus=pdnDslAtmBondAlarmConfRowStatus, pdnDslAtmBondPerfFailReason=pdnDslAtmBondPerfFailReason, pdnDslAtmBondMIBCompliance=pdnDslAtmBondMIBCompliance, pdnDslAtmBondGroupTable=pdnDslAtmBondGroupTable, pdnDslAtmBondConformance=pdnDslAtmBondConformance, pdnDslAtmBondGroupAturDiffDelay=pdnDslAtmBondGroupAturDiffDelay, pdnDslAtmBondDslIfIndex=pdnDslAtmBondDslIfIndex, pdnDslAtmBondBearerNbr=pdnDslAtmBondBearerNbr, pdnDslAtmBondGroupRowStatus=pdnDslAtmBondGroupRowStatus, PdnDslAtmBondGroupStatusTC=PdnDslAtmBondGroupStatusTC, pdnDslAtmBondPerfAtucRxCellLoss=pdnDslAtmBondPerfAtucRxCellLoss, pdnDslAtmBond15MinIntervalUAS=pdnDslAtmBond15MinIntervalUAS, PdnDslAtmBondGroupIdentityTC=PdnDslAtmBondGroupIdentityTC, pdnDslAtmBondMappingRowStatus=pdnDslAtmBondMappingRowStatus, pdnDslAtmBond15MinIntervalFailCount=pdnDslAtmBond15MinIntervalFailCount, pdnDslAtmBond15MinIntervalRunTime=pdnDslAtmBond15MinIntervalRunTime, pdnDslAtmBondMinRateGroup=pdnDslAtmBondMinRateGroup, pdnDslAtmBond1DayIntervalAturRxCellLoss=pdnDslAtmBond1DayIntervalAturRxCellLoss, pdnDslAtmBondAlarmConfAturThreshRateDown=pdnDslAtmBondAlarmConfAturThreshRateDown, PdnDslAtmBondAsmRxStatusTC=PdnDslAtmBondAsmRxStatusTC, pdnDslAtmBond15MinIntervalAtucRxCellLoss=pdnDslAtmBond15MinIntervalAtucRxCellLoss, pdnDslAtmBondAFNs=pdnDslAtmBondAFNs, pdnDslAtmBondGroupStatusChange=pdnDslAtmBondGroupStatusChange, pdnDslAtmBondMIB=pdnDslAtmBondMIB, pdnDslAtmBondLinkAtucTxLinkStatus=pdnDslAtmBondLinkAtucTxLinkStatus, pdnDslAtmBondGroupInvMappingTable=pdnDslAtmBondGroupInvMappingTable, PdnDslAtmBondLinkStatusAsmTC=PdnDslAtmBondLinkStatusAsmTC, pdnDslAtmBond15MinIntervalAturRxCellLoss=pdnDslAtmBond15MinIntervalAturRxCellLoss, PdnDslAtmBondGroupIndexTC=PdnDslAtmBondGroupIndexTC, pdnDslAtmBondAlarmConfProfileName=pdnDslAtmBondAlarmConfProfileName, pdnDslAtmBondRunTimeGroup=pdnDslAtmBondRunTimeGroup, pdnDslAtmBondLinkAturRxLinkStatus=pdnDslAtmBondLinkAturRxLinkStatus, pdnDslAtmBondObjGroups=pdnDslAtmBondObjGroups, pdnDslAtmBondGroupStatusNotifyEnabledGroup=pdnDslAtmBondGroupStatusNotifyEnabledGroup, PdnDslAtmBondGroupDataRateTC=PdnDslAtmBondGroupDataRateTC, pdnDslAtmBondInvMappingGroup=pdnDslAtmBondInvMappingGroup, pdnDslAtmBondAlarmConfNbrRefs=pdnDslAtmBondAlarmConfNbrRefs, pdnDslAtmBondAlarmConfAturThreshRateUp=pdnDslAtmBondAlarmConfAturThreshRateUp, pdnDslAtmBondMappingGroup=pdnDslAtmBondMappingGroup, pdnDslAtmBond15MinIntervalStartDateAndTime=pdnDslAtmBond15MinIntervalStartDateAndTime, pdnDslAtmBondAlarmConfAturThreshRateGroup=pdnDslAtmBondAlarmConfAturThreshRateGroup, pdnDslAtmBondDiffDelayGroup=pdnDslAtmBondDiffDelayGroup, pdnDslAtmBondPerfEntry=pdnDslAtmBondPerfEntry, pdnDslAtmBondPerfCurrAtucNetDataRate=pdnDslAtmBondPerfCurrAtucNetDataRate, pdnDslAtmBondPerfAggDataRateGroup=pdnDslAtmBondPerfAggDataRateGroup, pdnDslAtmBondPerfCurrAturNetDataRate=pdnDslAtmBondPerfCurrAturNetDataRate, pdnDslAtmBondGroups=pdnDslAtmBondGroups, pdnDslAtmBondRxCellLossGroup=pdnDslAtmBondRxCellLossGroup, PdnDslAtmBondGroupFailReasonTC=PdnDslAtmBondGroupFailReasonTC, pdnDslAtmBondGroupIndexMappingEntry=pdnDslAtmBondGroupIndexMappingEntry, pdnDslAtmBondGroupAlarmConfProfileName=pdnDslAtmBondGroupAlarmConfProfileName, pdnDslAtmBondAlarmConfAtucThreshRateDown=pdnDslAtmBondAlarmConfAtucThreshRateDown, pdnDslAtmBondGroupIndexMappingIndex=pdnDslAtmBondGroupIndexMappingIndex, pdnDslAtmBondGroupNbrRefs=pdnDslAtmBondGroupNbrRefs, pdnDslAtmBond1DayIntervalNumber=pdnDslAtmBond1DayIntervalNumber, pdnDslAtmBond1DayIntervalAtucRxCellLoss=pdnDslAtmBond1DayIntervalAtucRxCellLoss, pdnDslAtmBond1DayIntervalStartDateAndTime=pdnDslAtmBond1DayIntervalStartDateAndTime, pdnDslAtmBondAlarmConfProfileGroup=pdnDslAtmBondAlarmConfProfileGroup, pdnDslAtmBondPerfFailCount=pdnDslAtmBondPerfFailCount, pdnDslAtmBondAlarmConfAtucThreshRateUp=pdnDslAtmBondAlarmConfAtucThreshRateUp, pdnDslAtmBondGroupID=pdnDslAtmBondGroupID, pdnDslAtmBond1DayIntervalFailCount=pdnDslAtmBond1DayIntervalFailCount, PYSNMP_MODULE_ID=pdnDslAtmBondMIB, pdnDslAtmBondObjects=pdnDslAtmBondObjects, pdnDslAtmBond15MinIntervalTable=pdnDslAtmBond15MinIntervalTable, pdnDslAtmBondMappingTable=pdnDslAtmBondMappingTable, pdnDslAtmBondPerfTable=pdnDslAtmBondPerfTable, pdnDslAtmBondLinkTable=pdnDslAtmBondLinkTable, pdnDslAtmBondTrafficCapGroup=pdnDslAtmBondTrafficCapGroup, pdnDslAtmBondPerfPrevAtucNetDataRate=pdnDslAtmBondPerfPrevAtucNetDataRate, pdnDslAtmBond1DayIntervalRunTime=pdnDslAtmBond1DayIntervalRunTime, pdnDslAtmBondLinkEntry=pdnDslAtmBondLinkEntry, PdnDslAtmBondGroupBearerNumberTC=PdnDslAtmBondGroupBearerNumberTC, pdnDslAtmBondPerfUAS=pdnDslAtmBondPerfUAS, pdnDslAtmBondFailCountGroup=pdnDslAtmBondFailCountGroup, pdnDslAtmBondLinkAtucAsmRxStatus=pdnDslAtmBondLinkAtucAsmRxStatus, pdnDslAtmBondGroupEntry=pdnDslAtmBondGroupEntry, pdnDslAtmBondMappingGroupIndex=pdnDslAtmBondMappingGroupIndex, pdnDslAtmBondLinkAturAsmRxStatus=pdnDslAtmBondLinkAturAsmRxStatus, pdnDslAtmBondAtucRateChange=pdnDslAtmBondAtucRateChange, pdnDslAtmBondNbrOfGroups=pdnDslAtmBondNbrOfGroups, pdnDslAtmBondGroupIfIndex=pdnDslAtmBondGroupIfIndex, pdnDslAtmBondMappingEntry=pdnDslAtmBondMappingEntry, pdnDslAtmBond1DayIntervalTable=pdnDslAtmBond1DayIntervalTable, pdnDslAtmBondGroupStatusNotifyEnabled=pdnDslAtmBondGroupStatusNotifyEnabled, pdnDslAtmBond15MinIntervalNumber=pdnDslAtmBond15MinIntervalNumber, pdnDslAtmBondPerfBondGroupStatusGroup=pdnDslAtmBondPerfBondGroupStatusGroup, pdnDslAtmBondGroup=pdnDslAtmBondGroup, pdnDslAtmBondNotifications=pdnDslAtmBondNotifications, pdnDslAtmBondLinkAtucRxLinkStatus=pdnDslAtmBondLinkAtucRxLinkStatus, pdnDslAtmBondGroupAtucMaxNetDataRate=pdnDslAtmBondGroupAtucMaxNetDataRate, pdnDslAtmBondNotificationsGroup=pdnDslAtmBondNotificationsGroup, pdnDslAtmBond1DayIntervalEntry=pdnDslAtmBond1DayIntervalEntry, pdnDslAtmBondInvMappingBearerNbr=pdnDslAtmBondInvMappingBearerNbr, pdnDslAtmBondGroupAtucDiffDelay=pdnDslAtmBondGroupAtucDiffDelay, pdnDslAtmBond1DayIntervalUAS=pdnDslAtmBond1DayIntervalUAS, pdnDslAtmBondAturRateChange=pdnDslAtmBondAturRateChange, PdnDslAtmBondGroupDiffDelayTolTC=PdnDslAtmBondGroupDiffDelayTolTC, pdnDslAtmBondGroupIndex=pdnDslAtmBondGroupIndex, pdnDslAtmBondLinkAturTxLinkStatus=pdnDslAtmBondLinkAturTxLinkStatus, pdnDslAtmBondAfnGroups=pdnDslAtmBondAfnGroups, pdnDslAtmBondGroupIndexMappingTable=pdnDslAtmBondGroupIndexMappingTable, pdnDslAtmBondPerfFailReasonGroup=pdnDslAtmBondPerfFailReasonGroup, pdnDslAtmBondGroupInvMappingEntry=pdnDslAtmBondGroupInvMappingEntry, pdnDslAtmBond15MinIntervalEntry=pdnDslAtmBond15MinIntervalEntry, pdnDslAtmBondDateAndTimeGroup=pdnDslAtmBondDateAndTimeGroup, pdnDslAtmBondAlarmConfAtucThreshRateGroup=pdnDslAtmBondAlarmConfAtucThreshRateGroup, pdnDslAtmBondUASGroup=pdnDslAtmBondUASGroup, pdnDslAtmBondCompliances=pdnDslAtmBondCompliances, pdnDslAtmBondGroupAturMaxNetDataRate=pdnDslAtmBondGroupAturMaxNetDataRate, pdnDslAtmBondNextGroupIndex=pdnDslAtmBondNextGroupIndex, pdnDslAtmBondNtfyGroups=pdnDslAtmBondNtfyGroups, pdnDslAtmBondGroupAturMinNetDataRate=pdnDslAtmBondGroupAturMinNetDataRate, pdnDslATmBondAsmRxStatusGroup=pdnDslATmBondAsmRxStatusGroup, pdnDslAtmBondAlarmConfProfileTable=pdnDslAtmBondAlarmConfProfileTable, pdnDslAtmBondIndexMappingGroup=pdnDslAtmBondIndexMappingGroup, pdnDslAtmBondAlarmConfProfileEntry=pdnDslAtmBondAlarmConfProfileEntry, pdnDslAtmBondPerfAturRxCellLoss=pdnDslAtmBondPerfAturRxCellLoss, pdnDslAtmBondMaxRateGroup=pdnDslAtmBondMaxRateGroup, pdnDslAtmBondPerfRunTime=pdnDslAtmBondPerfRunTime)
