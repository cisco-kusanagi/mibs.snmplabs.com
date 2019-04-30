#
# PySNMP MIB module PAIRGAIN-SDSLCELL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-SDSLCELL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pgainSDSLCell, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainSDSLCell")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, TimeTicks, ModuleIdentity, IpAddress, Bits, iso, Unsigned32, Counter64, NotificationType, MibIdentifier, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "IpAddress", "Bits", "iso", "Unsigned32", "Counter64", "NotificationType", "MibIdentifier", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, RowStatus, TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TimeStamp", "DisplayString", "TextualConvention")
class PgSdslcellLineProfileType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class PgSdslcellAlarmProfileType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

pgsdslCellMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 14, 1))
if mibBuilder.loadTexts: pgsdslCellMIB.setLastUpdated('0003170000Z')
if mibBuilder.loadTexts: pgsdslCellMIB.setOrganization('PairGain Technologies Inc.')
pgsdslCellMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1))
pgSdslCellLineTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 1), )
if mibBuilder.loadTexts: pgSdslCellLineTable.setStatus('current')
pgSdslCellLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgSdslCellLineEntry.setStatus('current')
pgSdslCellLineProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 1, 1, 1), PgSdslcellLineProfileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellLineProfile.setStatus('current')
pgSdslCellAlarmProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 1, 1, 2), PgSdslcellAlarmProfileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellAlarmProfile.setStatus('current')
pgSdslCellPhysTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2), )
if mibBuilder.loadTexts: pgSdslCellPhysTable.setStatus('current')
pgSdslCellPhysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgSdslCellPhysEntry.setStatus('current')
pgSdslCellInvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellInvSerialNumber.setStatus('current')
pgSdslCellInvVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellInvVendorID.setStatus('current')
pgSdslCellInvVersionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellInvVersionNumber.setStatus('current')
pgSdslCellCurrSnrMgn = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 310))).setUnits('tenth dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellCurrSnrMgn.setStatus('current')
pgSdslCellCurrAtn = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 630))).setUnits('tenth dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellCurrAtn.setStatus('current')
pgSdslCellCurrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("hand", 3), ("test", 4), ("fail", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellCurrStatus.setStatus('current')
pgSdslCellLineProfileIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellLineProfileIndexNext.setStatus('current')
pgSdslCellLineProfileTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4), )
if mibBuilder.loadTexts: pgSdslCellLineProfileTable.setStatus('current')
pgSdslCellLineProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1), ).setIndexNames((0, "PAIRGAIN-SDSLCELL-MIB", "pgSdslCellLineProfileIndex"))
if mibBuilder.loadTexts: pgSdslCellLineProfileEntry.setStatus('current')
pgSdslCellLineProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 1), PgSdslcellLineProfileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellLineProfileIndex.setStatus('current')
pgSdslCellLineProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellLineProfileRowStatus.setStatus('current')
pgSdslCellLineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("twoB1Q", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellLineCode.setStatus('current')
pgSdslCellLineRateMode = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("autoBaud", 2), ("autoConex", 3), ("fixed", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellLineRateMode.setStatus('current')
pgSdslCellLineRate = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 2320))).setUnits('kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellLineRate.setStatus('current')
pgSdslCellLineTermType = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("co", 1), ("rt", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellLineTermType.setStatus('current')
pgSdslCellLineProfileInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notused", 1), ("inuse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellLineProfileInUse.setStatus('current')
pgSdslCellAlarmProfileIndexNext = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellAlarmProfileIndexNext.setStatus('current')
pgSdslCellAlarmProfileTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6), )
if mibBuilder.loadTexts: pgSdslCellAlarmProfileTable.setStatus('current')
pgSdslCellAlarmProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1), ).setIndexNames((0, "PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmProfileIndex"))
if mibBuilder.loadTexts: pgSdslCellAlarmProfileEntry.setStatus('current')
pgSdslCellAlarmProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 1), PgSdslcellAlarmProfileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellAlarmProfileIndex.setStatus('current')
pgSdslCellAlarmProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellAlarmProfileRowStatus.setStatus('current')
pgSdslCellThresh15MinLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellThresh15MinLOSS.setStatus('current')
pgSdslCellThresh15MinLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellThresh15MinLOCD.setStatus('current')
pgSdslCellThresh15MinSLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellThresh15MinSLOCD.setStatus('current')
pgSdslCellThreshSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellThreshSNR.setStatus('current')
pgSdslCellAlarmProfileInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notused", 1), ("inuse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellAlarmProfileInUse.setStatus('current')
pgSdslCellPerfCurrTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7), )
if mibBuilder.loadTexts: pgSdslCellPerfCurrTable.setStatus('current')
pgSdslCellPerfCurrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgSdslCellPerfCurrEntry.setStatus('current')
pgSdslCellPerfCurrLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerfCurrLOSS.setStatus('current')
pgSdslCellPerfCurrLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerfCurrLOCD.setStatus('current')
pgSdslCellPerfCurrSLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerfCurrSLOCD.setStatus('current')
pgSdslCellClearStats = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellClearStats.setStatus('current')
pgSdslCellStatsLastCleared = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 7, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellStatsLastCleared.setStatus('current')
pgSdslCellPerfCurr15MinTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8), )
if mibBuilder.loadTexts: pgSdslCellPerfCurr15MinTable.setStatus('current')
pgSdslCellPerfCurr15MinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgSdslCellPerfCurr15MinEntry.setStatus('current')
pgSdslCellPerfCurr15MinLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerfCurr15MinLOSS.setStatus('current')
pgSdslCellPerfCurr15MinLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerfCurr15MinLOCD.setStatus('current')
pgSdslCellPerfCurr15MinSLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerfCurr15MinSLOCD.setStatus('current')
pgSdslCellClearHistory = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgSdslCellClearHistory.setStatus('current')
pgSdslCellHistoryLastCleared = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 8, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellHistoryLastCleared.setStatus('current')
pgSdslCellPerf15MinIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9), )
if mibBuilder.loadTexts: pgSdslCellPerf15MinIntervalTable.setStatus('current')
pgSdslCellPerf15MinIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PAIRGAIN-SDSLCELL-MIB", "pgSdslCellPerf15MinIntervalIndex"))
if mibBuilder.loadTexts: pgSdslCellPerf15MinIntervalEntry.setStatus('current')
pgSdslCellPerf15MinIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerf15MinIntervalIndex.setStatus('current')
pgSdslCellPerf15MinIntervalLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerf15MinIntervalLOSS.setStatus('current')
pgSdslCellPerf15MinIntervalLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerf15MinIntervalLOCD.setStatus('current')
pgSdslCellPerf15MinIntervalSLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 9, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerf15MinIntervalSLOCD.setStatus('current')
pgSdslCellPerfCurr24hTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10), )
if mibBuilder.loadTexts: pgSdslCellPerfCurr24hTable.setStatus('current')
pgSdslCellPerfCurr24hEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgSdslCellPerfCurr24hEntry.setStatus('current')
pgSdslCellPerfCurr24hLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerfCurr24hLOSS.setStatus('current')
pgSdslCellPerfCurr24hLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerfCurr24hLOCD.setStatus('current')
pgSdslCellPerfCurr24hSLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 10, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerfCurr24hSLOCD.setStatus('current')
pgSdslCellPerf24hIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11), )
if mibBuilder.loadTexts: pgSdslCellPerf24hIntervalTable.setStatus('current')
pgSdslCellPerf24hIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PAIRGAIN-SDSLCELL-MIB", "pgSdslCellPerf24hIntervalIndex"))
if mibBuilder.loadTexts: pgSdslCellPerf24hIntervalEntry.setStatus('current')
pgSdslCellPerf24hIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerf24hIntervalIndex.setStatus('current')
pgSdslCellPerf24hIntervalLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerf24hIntervalLOSS.setStatus('current')
pgSdslCellPerf24hIntervalLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerf24hIntervalLOCD.setStatus('current')
pgSdslCellPerf24hIntervalSLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 11, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellPerf24hIntervalSLOCD.setStatus('current')
pgSdslCellAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12), )
if mibBuilder.loadTexts: pgSdslCellAlarmTable.setStatus('current')
pgSdslCellAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pgSdslCellAlarmEntry.setStatus('current')
pgSdslCellCrossThreshLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellCrossThreshLOSS.setStatus('current')
pgSdslCellCrossThreshLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellCrossThreshLOCD.setStatus('current')
pgSdslCellCrossThreshSLOCD = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellCrossThreshSLOCD.setStatus('current')
pgSdslCellCrossThreshSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellCrossThreshSNR.setStatus('current')
pgSdslCellHardwareCause = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ok", 1), ("xcvrfail", 2), ("otherfail", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellHardwareCause.setStatus('current')
pgSdslCellAlarmLastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 1, 12, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgSdslCellAlarmLastChanged.setStatus('current')
pgSdslCellTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2))
pgSdslCellTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0))
pgSdslCellThreshLOSSTrap = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellCrossThreshLOSS"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
if mibBuilder.loadTexts: pgSdslCellThreshLOSSTrap.setStatus('current')
pgSdslCellThreshLOCDTrap = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellCrossThreshLOCD"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
if mibBuilder.loadTexts: pgSdslCellThreshLOCDTrap.setStatus('current')
pgSdslCellThreshSLOCDTrap = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellCrossThreshSLOCD"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
if mibBuilder.loadTexts: pgSdslCellThreshSLOCDTrap.setStatus('current')
pgSdslCellThreshSNRTrap = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellCrossThreshSNR"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
if mibBuilder.loadTexts: pgSdslCellThreshSNRTrap.setStatus('current')
pgSdslCellHardwareFaultTrap = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 14, 1, 2, 0, 5)).setObjects(("IF-MIB", "ifIndex"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellHardwareCause"), ("PAIRGAIN-SDSLCELL-MIB", "pgSdslCellAlarmLastChanged"))
if mibBuilder.loadTexts: pgSdslCellHardwareFaultTrap.setStatus('current')
mibBuilder.exportSymbols("PAIRGAIN-SDSLCELL-MIB", pgsdslCellMIB=pgsdslCellMIB, pgSdslCellLineProfileRowStatus=pgSdslCellLineProfileRowStatus, pgSdslCellCrossThreshSLOCD=pgSdslCellCrossThreshSLOCD, pgSdslCellThreshLOSSTrap=pgSdslCellThreshLOSSTrap, pgSdslCellCrossThreshSNR=pgSdslCellCrossThreshSNR, pgSdslCellCrossThreshLOSS=pgSdslCellCrossThreshLOSS, pgSdslCellAlarmProfileIndexNext=pgSdslCellAlarmProfileIndexNext, pgSdslCellPerfCurrLOCD=pgSdslCellPerfCurrLOCD, pgSdslCellPhysEntry=pgSdslCellPhysEntry, pgSdslCellHardwareCause=pgSdslCellHardwareCause, pgSdslCellPerfCurr15MinLOCD=pgSdslCellPerfCurr15MinLOCD, pgSdslCellAlarmProfileIndex=pgSdslCellAlarmProfileIndex, pgSdslCellAlarmProfileEntry=pgSdslCellAlarmProfileEntry, pgSdslCellLineProfileIndexNext=pgSdslCellLineProfileIndexNext, pgSdslCellPerfCurr15MinTable=pgSdslCellPerfCurr15MinTable, pgSdslCellCurrStatus=pgSdslCellCurrStatus, pgSdslCellLineProfileInUse=pgSdslCellLineProfileInUse, pgSdslCellCurrAtn=pgSdslCellCurrAtn, pgSdslCellPerfCurr24hSLOCD=pgSdslCellPerfCurr24hSLOCD, pgsdslCellMibObjects=pgsdslCellMibObjects, pgSdslCellPerf24hIntervalTable=pgSdslCellPerf24hIntervalTable, pgSdslCellAlarmTable=pgSdslCellAlarmTable, pgSdslCellHardwareFaultTrap=pgSdslCellHardwareFaultTrap, pgSdslCellPerf15MinIntervalLOSS=pgSdslCellPerf15MinIntervalLOSS, pgSdslCellPerfCurr15MinLOSS=pgSdslCellPerfCurr15MinLOSS, pgSdslCellLineTable=pgSdslCellLineTable, pgSdslCellThreshLOCDTrap=pgSdslCellThreshLOCDTrap, pgSdslCellThreshSNRTrap=pgSdslCellThreshSNRTrap, pgSdslCellPerfCurrSLOCD=pgSdslCellPerfCurrSLOCD, pgSdslCellThreshSNR=pgSdslCellThreshSNR, pgSdslCellAlarmProfileInUse=pgSdslCellAlarmProfileInUse, pgSdslCellLineRate=pgSdslCellLineRate, pgSdslCellPerf15MinIntervalTable=pgSdslCellPerf15MinIntervalTable, pgSdslCellPerfCurr15MinSLOCD=pgSdslCellPerfCurr15MinSLOCD, PgSdslcellLineProfileType=PgSdslcellLineProfileType, pgSdslCellLineProfile=pgSdslCellLineProfile, pgSdslCellPerf15MinIntervalLOCD=pgSdslCellPerf15MinIntervalLOCD, pgSdslCellLineTermType=pgSdslCellLineTermType, pgSdslCellPerf24hIntervalLOCD=pgSdslCellPerf24hIntervalLOCD, pgSdslCellLineProfileTable=pgSdslCellLineProfileTable, pgSdslCellPerf24hIntervalEntry=pgSdslCellPerf24hIntervalEntry, PgSdslcellAlarmProfileType=PgSdslcellAlarmProfileType, PYSNMP_MODULE_ID=pgsdslCellMIB, pgSdslCellPerf15MinIntervalEntry=pgSdslCellPerf15MinIntervalEntry, pgSdslCellInvVersionNumber=pgSdslCellInvVersionNumber, pgSdslCellThreshSLOCDTrap=pgSdslCellThreshSLOCDTrap, pgSdslCellStatsLastCleared=pgSdslCellStatsLastCleared, pgSdslCellPerfCurr24hLOSS=pgSdslCellPerfCurr24hLOSS, pgSdslCellPhysTable=pgSdslCellPhysTable, pgSdslCellHistoryLastCleared=pgSdslCellHistoryLastCleared, pgSdslCellPerf15MinIntervalSLOCD=pgSdslCellPerf15MinIntervalSLOCD, pgSdslCellPerf15MinIntervalIndex=pgSdslCellPerf15MinIntervalIndex, pgSdslCellClearStats=pgSdslCellClearStats, pgSdslCellPerf24hIntervalLOSS=pgSdslCellPerf24hIntervalLOSS, pgSdslCellPerf24hIntervalSLOCD=pgSdslCellPerf24hIntervalSLOCD, pgSdslCellPerfCurr24hLOCD=pgSdslCellPerfCurr24hLOCD, pgSdslCellPerfCurrTable=pgSdslCellPerfCurrTable, pgSdslCellLineCode=pgSdslCellLineCode, pgSdslCellPerf24hIntervalIndex=pgSdslCellPerf24hIntervalIndex, pgSdslCellInvVendorID=pgSdslCellInvVendorID, pgSdslCellAlarmProfileRowStatus=pgSdslCellAlarmProfileRowStatus, pgSdslCellTrap=pgSdslCellTrap, pgSdslCellLineProfileIndex=pgSdslCellLineProfileIndex, pgSdslCellPerfCurrLOSS=pgSdslCellPerfCurrLOSS, pgSdslCellInvSerialNumber=pgSdslCellInvSerialNumber, pgSdslCellLineRateMode=pgSdslCellLineRateMode, pgSdslCellPerfCurr24hTable=pgSdslCellPerfCurr24hTable, pgSdslCellCrossThreshLOCD=pgSdslCellCrossThreshLOCD, pgSdslCellLineEntry=pgSdslCellLineEntry, pgSdslCellThresh15MinSLOCD=pgSdslCellThresh15MinSLOCD, pgSdslCellPerfCurr15MinEntry=pgSdslCellPerfCurr15MinEntry, pgSdslCellClearHistory=pgSdslCellClearHistory, pgSdslCellPerfCurr24hEntry=pgSdslCellPerfCurr24hEntry, pgSdslCellThresh15MinLOCD=pgSdslCellThresh15MinLOCD, pgSdslCellAlarmLastChanged=pgSdslCellAlarmLastChanged, pgSdslCellAlarmProfile=pgSdslCellAlarmProfile, pgSdslCellPerfCurrEntry=pgSdslCellPerfCurrEntry, pgSdslCellCurrSnrMgn=pgSdslCellCurrSnrMgn, pgSdslCellAlarmProfileTable=pgSdslCellAlarmProfileTable, pgSdslCellLineProfileEntry=pgSdslCellLineProfileEntry, pgSdslCellAlarmEntry=pgSdslCellAlarmEntry, pgSdslCellTraps=pgSdslCellTraps, pgSdslCellThresh15MinLOSS=pgSdslCellThresh15MinLOSS)