#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-ATM-T1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-ATM-T1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, MibIdentifier, ObjectIdentity, TimeTicks, Counter64, NotificationType, Integer32, iso, Unsigned32, Bits, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Counter64", "NotificationType", "Integer32", "iso", "Unsigned32", "Bits", "Gauge32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonomaATM, = mibBuilder.importSymbols("SONOMASYSTEMS-SONOMA-MIB", "sonomaATM")
sonomaT1ATMAdapterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5))
atmDs1ConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1))
atmDs1StatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2))
atmDs1ConfPhyTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1), )
if mibBuilder.loadTexts: atmDs1ConfPhyTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1ConfPhyTable.setDescription('A table of physical layer configuration for the DS1 interface')
atmDs1ConfPhyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-ATM-T1-MIB", "atmDs1ConfPhysIndex"))
if mibBuilder.loadTexts: atmDs1ConfPhyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1ConfPhyEntry.setDescription('A entry in the table, containing information about the physical layer of a DS1 interface')
atmDs1ConfPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1ConfPhysIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1ConfPhysIndex.setDescription('The physical interface index.')
atmDs1ConfLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("payload", 2), ("line", 3), ("local", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDs1ConfLoopback.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1ConfLoopback.setDescription('This object is used to modify the state of internal loopback....')
atmDs1ConfTxClockSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("recovered", 2))).clone('internal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDs1ConfTxClockSelect.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1ConfTxClockSelect.setDescription('Configure the transmit clock.')
atmDs1ConfFillerCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unassigned", 1), ("idle", 2))).clone('unassigned')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDs1ConfFillerCells.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1ConfFillerCells.setDescription('This parameter indicates the type of filler cells to send when there are no data cells.')
atmDs1ConfLineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("short-haul-0-133-FT", 1), ("short-haul-133-266-FT", 2), ("short-haul-266-399-FT", 3), ("short-haul-399-533-FT", 4), ("short-haul-533-655-FT", 5), ("long-haul-0-0-dB", 6), ("long-haul-7-5-dB", 7), ("long-haul-15-0-dB", 8), ("long-haul-22-5-dB", 9))).clone('long-haul-0-0-dB')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDs1ConfLineBuildOut.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1ConfLineBuildOut.setDescription('This parameter indicates the value selected for the Line Build Out.')
atmDs1StatsTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1), )
if mibBuilder.loadTexts: atmDs1StatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsTable.setDescription('A table of physical layer statistics information for the DS1 interface')
atmDs1StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-ATM-T1-MIB", "atmDs1StatsPhysIndex"))
if mibBuilder.loadTexts: atmDs1StatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsEntry.setDescription('A entry in the table, containing information about the physical layer of a DS1 interface')
atmDs1StatsPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsPhysIndex.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsPhysIndex.setDescription('The physical interface index.')
atmDs1StatsNoSignals = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsNoSignals.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsNoSignals.setDescription('No signal error counter.')
atmDs1StatsAISDetects = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsAISDetects.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsAISDetects.setDescription('AIS Detect counter.')
atmDs1StatsYelAlarmCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsYelAlarmCount.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsYelAlarmCount.setDescription('A count of the number of Yellow Alarms.')
atmDs1StatsLCVErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsLCVErrors.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsLCVErrors.setDescription('LCV (Line Code Violation) error counter.')
atmDs1StatsPCVErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsPCVErrors.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsPCVErrors.setDescription('PCV (Path Code Violation) error counter.')
atmDs1StatsMOSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsMOSErrors.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsMOSErrors.setDescription('Multiframe out of sync error counter.')
atmDs1StatsSyncLossCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsSyncLossCount.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsSyncLossCount.setDescription('Sync Loss counter.')
atmDs1StatsHECErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsHECErrors.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsHECErrors.setDescription('HEC error counter.')
atmDs1StatsSignalLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsSignalLoss.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsSignalLoss.setDescription('Signal loss indication.')
atmDs1StatsAISDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsAISDetect.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsAISDetect.setDescription('AIS indication.')
atmDs1StatsYellowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsYellowAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsYellowAlarm.setDescription('Yellow Alarm indication.')
atmDs1StatsSyncLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsSyncLoss.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsSyncLoss.setDescription('Loss of sync indication.')
atmDs1StatsTxClockLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmDs1StatsTxClockLoss.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsTxClockLoss.setDescription('Loss of transmit clock indication.')
atmDs1StatsClearCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 5, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmDs1StatsClearCounters.setStatus('mandatory')
if mibBuilder.loadTexts: atmDs1StatsClearCounters.setDescription('Clear all counters in this group ONLY.')
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-ATM-T1-MIB", atmDs1ConfFillerCells=atmDs1ConfFillerCells, atmDs1ConfPhyEntry=atmDs1ConfPhyEntry, atmDs1StatsHECErrors=atmDs1StatsHECErrors, atmDs1StatsTable=atmDs1StatsTable, atmDs1StatsSyncLoss=atmDs1StatsSyncLoss, atmDs1ConfLineBuildOut=atmDs1ConfLineBuildOut, atmDs1ConfPhyTable=atmDs1ConfPhyTable, atmDs1StatsAISDetect=atmDs1StatsAISDetect, atmDs1ConfLoopback=atmDs1ConfLoopback, atmDs1StatsPhysIndex=atmDs1StatsPhysIndex, atmDs1StatsGroup=atmDs1StatsGroup, atmDs1StatsSyncLossCount=atmDs1StatsSyncLossCount, atmDs1StatsEntry=atmDs1StatsEntry, atmDs1StatsNoSignals=atmDs1StatsNoSignals, atmDs1StatsAISDetects=atmDs1StatsAISDetects, atmDs1StatsYellowAlarm=atmDs1StatsYellowAlarm, atmDs1ConfTxClockSelect=atmDs1ConfTxClockSelect, atmDs1StatsLCVErrors=atmDs1StatsLCVErrors, atmDs1StatsYelAlarmCount=atmDs1StatsYelAlarmCount, atmDs1StatsTxClockLoss=atmDs1StatsTxClockLoss, atmDs1ConfPhysIndex=atmDs1ConfPhysIndex, sonomaT1ATMAdapterGroup=sonomaT1ATMAdapterGroup, atmDs1StatsPCVErrors=atmDs1StatsPCVErrors, atmDs1StatsMOSErrors=atmDs1StatsMOSErrors, atmDs1StatsClearCounters=atmDs1StatsClearCounters, atmDs1ConfGroup=atmDs1ConfGroup, atmDs1StatsSignalLoss=atmDs1StatsSignalLoss)
