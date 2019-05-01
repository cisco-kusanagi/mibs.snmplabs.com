#
# PySNMP MIB module GDCSC613-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GDCSC613-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:19:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
SCinstance, = mibBuilder.importSymbols("GDCMACRO-MIB", "SCinstance")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, enterprises, TimeTicks, Counter32, ModuleIdentity, ObjectIdentity, Unsigned32, MibIdentifier, Integer32, Gauge32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "enterprises", "TimeTicks", "Counter32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Integer32", "Gauge32", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gdc = MibIdentifier((1, 3, 6, 1, 4, 1, 498))
bql2 = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12))
bql613 = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 1))
bql613MIBVersion = MibScalar((1, 3, 6, 1, 4, 1, 498, 12, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613MIBVersion.setStatus('mandatory')
if mibBuilder.loadTexts: bql613MIBVersion.setDescription('The version number of the MIB, to allow products to know which MIB is being supported. The version number will be x.yzT where x is a major revision (1-9), y is a minor revision(0-9), z is a typo revision (0-9) and T indicates the MIB is still a test revision(A-Z). When a release is complete no T should exist.')
bql613WhatAreYouTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 1, 2), )
if mibBuilder.loadTexts: bql613WhatAreYouTable.setStatus('mandatory')
if mibBuilder.loadTexts: bql613WhatAreYouTable.setDescription('The GDC SC613 What Are You Table.')
bql613WhatAreYouEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 1, 2, 1), ).setIndexNames((0, "GDCSC613-MIB", "bql613WhatAreYouIndex"))
if mibBuilder.loadTexts: bql613WhatAreYouEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bql613WhatAreYouEntry.setDescription('An entry in the GDC SC613 What Are You table.')
bql613WhatAreYouIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 2, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613WhatAreYouIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bql613WhatAreYouIndex.setDescription('This object is the identifier of the SC613 What Are You table.')
bql613CodeRev = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613CodeRev.setStatus('mandatory')
if mibBuilder.loadTexts: bql613CodeRev.setDescription('This function returns the firmware code level. Example A- ,B- ')
bql613AlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613AlarmStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bql613AlarmStatus.setDescription('The current alarms of the unit without the alarm masks.')
bql613ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 1, 3), )
if mibBuilder.loadTexts: bql613ConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: bql613ConfigTable.setDescription('The GDC SC613.')
bql613ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1), ).setIndexNames((0, "GDCSC613-MIB", "bql613ConfigIndex"))
if mibBuilder.loadTexts: bql613ConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bql613ConfigEntry.setDescription('A listing of GDC 2B1Q SC613 options.')
bql613ConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613ConfigIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bql613ConfigIndex.setDescription('A unique index for the Configuration Table.')
bql613TestPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pattern2047", 1), ("pattern511", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613TestPattern.setStatus('mandatory')
if mibBuilder.loadTexts: bql613TestPattern.setDescription('Object to select loop and channel test pattern for SC613.')
bql613RLTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noTimeout", 1), ("timeoutAfter10Min", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613RLTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: bql613RLTimeout.setDescription('Object to select remote loop time out.')
bql613MasterTXClkSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("internal", 1), ("external", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613MasterTXClkSrc.setStatus('mandatory')
if mibBuilder.loadTexts: bql613MasterTXClkSrc.setDescription('Object to option the Loop master transmit clock source.')
bql613DTEDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(9, 10))).clone(namedValues=NamedValues(("kBps64000", 9), ("kBps128000", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613DTEDataRate.setStatus('mandatory')
if mibBuilder.loadTexts: bql613DTEDataRate.setDescription('Object to option a SC613 Loop interface to a K bit per second rate.')
bql613RespRdl = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613RespRdl.setStatus('mandatory')
if mibBuilder.loadTexts: bql613RespRdl.setDescription('Object to option V54 Response RDL to enable or disable.')
bql613DiagnosticTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 1, 4), )
if mibBuilder.loadTexts: bql613DiagnosticTable.setStatus('mandatory')
if mibBuilder.loadTexts: bql613DiagnosticTable.setDescription('The GDC SC613 diagnostics table.')
bql613DiagnosticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1), ).setIndexNames((0, "GDCSC613-MIB", "bql613DiagnosticIndex"))
if mibBuilder.loadTexts: bql613DiagnosticEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bql613DiagnosticEntry.setDescription('A listing of GDC SC613 diagnostic tests')
bql613DiagnosticIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613DiagnosticIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bql613DiagnosticIndex.setDescription('A unique index for the Diagnostic Table.')
bql613DiagnosticTest = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613DiagnosticTest.setStatus('mandatory')
if mibBuilder.loadTexts: bql613DiagnosticTest.setDescription('This function selects or reads the test. 0 = no test currently operating 1 = remote loopback test 2 = channel loopback test 4 = data loopback test 8 = selftest 16 = line loopback test 32 = terminate test All other values are test combinations such as 9 = selftest and remote loopback.')
bql613DiagnosticActive = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notActive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613DiagnosticActive.setStatus('mandatory')
if mibBuilder.loadTexts: bql613DiagnosticActive.setDescription('This function represents the test condition.')
bql613DiagnosticResults = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16383))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613DiagnosticResults.setStatus('mandatory')
if mibBuilder.loadTexts: bql613DiagnosticResults.setDescription('This function reads the self test results in bit errors.')
bql613DiagnosticErrorCount = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613DiagnosticErrorCount.setStatus('mandatory')
if mibBuilder.loadTexts: bql613DiagnosticErrorCount.setDescription('This function resets the selftest error count for a SC613.')
bql613Alarm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7))
bql613AlarmData = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1))
bql613NoResponseAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 1))
bql613DiagRxErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 2))
bql613PowerUpAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 3))
bql613Lp2B1QOutofSyncAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 4))
bql613LpTxClockOutOfTolerance = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 5))
bql613LpExtTxClkAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 6))
bql613LpSealingCurrentNoContinuityAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 7))
bql613LpMajorBERAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 8))
bql613LpMinorBERAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 9))
bql613AlarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 7, 2), )
if mibBuilder.loadTexts: bql613AlarmConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: bql613AlarmConfigTable.setDescription('The bql613AlarmConfigTable contains entries that configure alarm reporting. The structure of the table is such that alarm configuration is supported on a unit and interface basis, and then on an alarm type basis within the interface. For simplicity sake alarms, be they unit or interface related, are represented in one table.')
bql613AlarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 7, 2, 1), ).setIndexNames((0, "GDCSC613-MIB", "bql613AlarmConfigIndex"), (0, "GDCSC613-MIB", "bql613AlarmConfigIdentifier"))
if mibBuilder.loadTexts: bql613AlarmConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bql613AlarmConfigEntry.setDescription('An entry in the bql613AlarmConfigTable table.')
bql613AlarmConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 7, 2, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613AlarmConfigIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bql613AlarmConfigIndex.setDescription('The index value which uniquely identifies the interface to which this entry is applicable.')
bql613AlarmConfigIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 7, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613AlarmConfigIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: bql613AlarmConfigIdentifier.setDescription('The unique alarm identifier assigned to this alarm type. The format of this identifier is an OBJECT IDENTIFIER that has the following format: {iso(1) org(3) dod(6) internet(1) private(4) enterprises(1) gdc(498) xxx(x) alarm(z) yyy(y) where xxx(x) is the administratively assigned family object identifier (z) is the object identifier for alarms in the family defined MIB and yyy(y) is the administratively assigned alarm type identifier for this alarm.')
bql613AlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("thres10E03", 1), ("thres10E04", 2), ("thres10E05", 3), ("thres10E06", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613AlarmThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: bql613AlarmThreshold.setDescription('This function sets/reads the Major or Minor BER alarm threshold criteria.')
bql613ControlTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 1, 6), )
if mibBuilder.loadTexts: bql613ControlTable.setStatus('mandatory')
if mibBuilder.loadTexts: bql613ControlTable.setDescription('The GDC SC613 Control Table.')
bql613ControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1), ).setIndexNames((0, "GDCSC613-MIB", "bql613ControlIndex"))
if mibBuilder.loadTexts: bql613ControlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bql613ControlEntry.setDescription('An entry in the GDC SC613 Control table.')
bql613ControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613ControlIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bql613ControlIndex.setDescription('This object is the identifier of the SC613 Control table.')
bql613SoftReset = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613SoftReset.setStatus('mandatory')
if mibBuilder.loadTexts: bql613SoftReset.setDescription('Forces a soft reset on the network element. The reset selection is write only. The normal selection is read only.')
bql613EraseConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("erase", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613EraseConfig.setStatus('mandatory')
if mibBuilder.loadTexts: bql613EraseConfig.setDescription('Forces an erase of the stored configuration in the network element. The erase selection is write only. The normal selection is read only.')
bql613FrontPanel = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613FrontPanel.setStatus('mandatory')
if mibBuilder.loadTexts: bql613FrontPanel.setDescription('Object used to enable or disable the units front panel switches.')
bql613LEDStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613LEDStatus.setStatus('mandatory')
if mibBuilder.loadTexts: bql613LEDStatus.setDescription('The GDC SC613 front panel LED Status. A value of 1 means on, 0 is off. byte 1 bit 7 (1.7) - not used 1.6 - test mode 1.5 - alarm on 1.4 - loop 1 line loopback 1.3 - loop 1 send data transitions 1.2 - loop 1 receive data transitions 1.1 - loop 1 request to send 1.0 - loop 1 data carrier on 2.7 - not used 2.6 - not used 2.5 - not used 2.4 - loop 2 line loopback 2.3 - loop 2 send data transitions 2.2 - loop 2 receive data transitions 2.1 - loop 2 request to send 2.0 - loop 2 data carrier on 3.7 - not used 3.6 - not used 3.5 - not used 3.4 - loop 3 line loopback 3.3 - loop 3 send data transitions 3.2 - loop 3 receive data transitions 3.1 - loop 3 request to send 3.0 - loop 3 data carrier on')
bql613CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 1, 7), )
if mibBuilder.loadTexts: bql613CurrentTable.setStatus('mandatory')
if mibBuilder.loadTexts: bql613CurrentTable.setDescription('The SC613 Current table.')
bql613CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 1, 7, 1), ).setIndexNames((0, "GDCSC613-MIB", "bql613CurrentIndex"))
if mibBuilder.loadTexts: bql613CurrentEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bql613CurrentEntry.setDescription('An entry in the SC613 Current table.')
bql613CurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 7, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613CurrentIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bql613CurrentIndex.setDescription('The index value which uniquely identifies the SC613 interface to which this entry is applicable.')
bql613CurrentStats = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613CurrentStats.setStatus('mandatory')
if mibBuilder.loadTexts: bql613CurrentStats.setDescription('The number of Errored Seconds, Severely Errored Seconds & Unavailable Errored Seconds encountered by an ISDN interface in the current 15 minute interval.')
bql613IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 1, 8), )
if mibBuilder.loadTexts: bql613IntervalTable.setStatus('mandatory')
if mibBuilder.loadTexts: bql613IntervalTable.setDescription('The SC613 Interval table.')
bql613IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 1, 8, 1), ).setIndexNames((0, "GDCSC613-MIB", "bql613IntervalIndex"), (0, "GDCSC613-MIB", "bql613IntervalNumber"))
if mibBuilder.loadTexts: bql613IntervalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bql613IntervalEntry.setDescription('An entry in the SC613 Interval table.')
bql613IntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 8, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613IntervalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bql613IntervalIndex.setDescription('The index value which uniquely identifies the ISDN interface to which this entry is applicable.')
bql613IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613IntervalNumber.setStatus('mandatory')
if mibBuilder.loadTexts: bql613IntervalNumber.setDescription('A number between 1 and 96, where 1 is the most recently completed 15 minute interval and 96 is the least recently completed 15 minute inter- val (assuming that all 96 intervals are valid).')
bql613IntervalStats = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 8, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613IntervalStats.setStatus('mandatory')
if mibBuilder.loadTexts: bql613IntervalStats.setDescription('The number of Errored Seconds, Severely Errored Seconds and Unavailable Errored Seconds encountered by a DS1 interface in one of the previous 96, individual 15 minute, intervals.')
bql613TotalTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 1, 9), )
if mibBuilder.loadTexts: bql613TotalTable.setStatus('mandatory')
if mibBuilder.loadTexts: bql613TotalTable.setDescription('The SC613 Total table. 24 hour interval.')
bql613TotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 1, 9, 1), ).setIndexNames((0, "GDCSC613-MIB", "bql613TotalIndex"))
if mibBuilder.loadTexts: bql613TotalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bql613TotalEntry.setDescription('An entry in the SC613 Total table.')
bql613TotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 9, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613TotalIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bql613TotalIndex.setDescription('The index value which uniquely identifies the ISDN interface to which this entry is applicable.')
bql613TotalStats = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 9, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613TotalStats.setStatus('mandatory')
if mibBuilder.loadTexts: bql613TotalStats.setDescription('The number of Errored Seconds,Severely Errored Seconds & Unavailable Errored Seconds encountered by an ISDN interface in the previous 24 hour interval.')
bql613IntervalMaintenanceTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 1, 10), )
if mibBuilder.loadTexts: bql613IntervalMaintenanceTable.setStatus('mandatory')
if mibBuilder.loadTexts: bql613IntervalMaintenanceTable.setDescription('The SC613 Loop Interval Maintenance table. ')
bql613IntervalMaintenanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1), ).setIndexNames((0, "GDCSC613-MIB", "bql613IntervalMaintenanceIndex"))
if mibBuilder.loadTexts: bql613IntervalMaintenanceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: bql613IntervalMaintenanceEntry.setDescription('The SC613 Interval Maintenance table entry. ')
bql613IntervalMaintenanceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613IntervalMaintenanceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: bql613IntervalMaintenanceIndex.setDescription('The index value which uniquely identifies the interface to which this entry is applicable. This has the form of a SCinstance which defines the slot, line, drop, and interface, where is can be 1, 2, or 3.')
bql613ResetIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("norm", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613ResetIntervals.setStatus('mandatory')
if mibBuilder.loadTexts: bql613ResetIntervals.setDescription(' This variable is used to reset Loop performance intervals. When it is set to reset, the Loop performance tables are reset to zero.')
bql613NumberofValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bql613NumberofValidIntervals.setStatus('mandatory')
if mibBuilder.loadTexts: bql613NumberofValidIntervals.setDescription(' This variable is used to read the number of intervals collected. Each interval is an increment of 15 minutes.')
bql613ResetMajorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("norm", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613ResetMajorAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: bql613ResetMajorAlarm.setDescription(' This variable is used to reset alarm per Loop basis.')
bql613ResetMinorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("norm", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bql613ResetMinorAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: bql613ResetMinorAlarm.setDescription(' This variable is used to reset alarm per Loop basis.')
mibBuilder.exportSymbols("GDCSC613-MIB", bql613CurrentTable=bql613CurrentTable, bql613PowerUpAlm=bql613PowerUpAlm, bql613LpTxClockOutOfTolerance=bql613LpTxClockOutOfTolerance, bql613AlarmConfigTable=bql613AlarmConfigTable, bql613Alarm=bql613Alarm, bql613AlarmConfigEntry=bql613AlarmConfigEntry, bql613MasterTXClkSrc=bql613MasterTXClkSrc, bql613CurrentIndex=bql613CurrentIndex, bql613ResetMajorAlarm=bql613ResetMajorAlarm, bql613AlarmData=bql613AlarmData, bql613IntervalEntry=bql613IntervalEntry, bql613ControlTable=bql613ControlTable, bql613CurrentEntry=bql613CurrentEntry, bql613WhatAreYouEntry=bql613WhatAreYouEntry, bql613DiagRxErrAlm=bql613DiagRxErrAlm, bql613ConfigTable=bql613ConfigTable, bql613CodeRev=bql613CodeRev, bql613DiagnosticIndex=bql613DiagnosticIndex, bql613IntervalIndex=bql613IntervalIndex, bql613AlarmStatus=bql613AlarmStatus, bql613IntervalNumber=bql613IntervalNumber, bql613IntervalMaintenanceTable=bql613IntervalMaintenanceTable, bql613DiagnosticTest=bql613DiagnosticTest, bql613TotalTable=bql613TotalTable, bql613IntervalMaintenanceEntry=bql613IntervalMaintenanceEntry, bql613RespRdl=bql613RespRdl, bql613IntervalStats=bql613IntervalStats, bql613LEDStatus=bql613LEDStatus, bql613ResetMinorAlarm=bql613ResetMinorAlarm, bql613IntervalMaintenanceIndex=bql613IntervalMaintenanceIndex, bql613=bql613, bql613EraseConfig=bql613EraseConfig, bql613Lp2B1QOutofSyncAlm=bql613Lp2B1QOutofSyncAlm, bql613TotalStats=bql613TotalStats, bql613TotalIndex=bql613TotalIndex, bql613NumberofValidIntervals=bql613NumberofValidIntervals, bql613WhatAreYouTable=bql613WhatAreYouTable, bql2=bql2, bql613LpExtTxClkAlm=bql613LpExtTxClkAlm, bql613ControlIndex=bql613ControlIndex, bql613TestPattern=bql613TestPattern, bql613DiagnosticActive=bql613DiagnosticActive, bql613LpMajorBERAlm=bql613LpMajorBERAlm, bql613LpSealingCurrentNoContinuityAlm=bql613LpSealingCurrentNoContinuityAlm, bql613MIBVersion=bql613MIBVersion, bql613DiagnosticErrorCount=bql613DiagnosticErrorCount, bql613FrontPanel=bql613FrontPanel, gdc=gdc, bql613DiagnosticResults=bql613DiagnosticResults, bql613RLTimeout=bql613RLTimeout, bql613DTEDataRate=bql613DTEDataRate, bql613LpMinorBERAlm=bql613LpMinorBERAlm, bql613IntervalTable=bql613IntervalTable, bql613AlarmConfigIdentifier=bql613AlarmConfigIdentifier, bql613WhatAreYouIndex=bql613WhatAreYouIndex, bql613DiagnosticEntry=bql613DiagnosticEntry, bql613DiagnosticTable=bql613DiagnosticTable, bql613AlarmThreshold=bql613AlarmThreshold, bql613AlarmConfigIndex=bql613AlarmConfigIndex, bql613ConfigEntry=bql613ConfigEntry, bql613ResetIntervals=bql613ResetIntervals, bql613ConfigIndex=bql613ConfigIndex, bql613SoftReset=bql613SoftReset, bql613NoResponseAlm=bql613NoResponseAlm, bql613TotalEntry=bql613TotalEntry, bql613CurrentStats=bql613CurrentStats, bql613ControlEntry=bql613ControlEntry)