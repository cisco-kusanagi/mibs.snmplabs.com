#
# PySNMP MIB module ASCEND-HDSL2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-HDSL2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
wanTypeHdsl2, = mibBuilder.importSymbols("ASCEND-WAN-MIB", "wanTypeHdsl2")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Counter64, ModuleIdentity, Unsigned32, Integer32, NotificationType, Gauge32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Counter64", "ModuleIdentity", "Unsigned32", "Integer32", "NotificationType", "Gauge32", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hdsl2LineStatusTable = MibTable((1, 3, 6, 1, 4, 1, 529, 4, 12, 1), )
if mibBuilder.loadTexts: hdsl2LineStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2LineStatusTable.setDescription('HDSL2 status parameters.')
hdsl2LineStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1), ).setIndexNames((0, "ASCEND-HDSL2-MIB", "hdsl2StatusIfEntryIndex"))
if mibBuilder.loadTexts: hdsl2LineStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2LineStatusEntry.setDescription('A interface status entry containing objects to describe the interface.')
hdsl2StatusIfEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusIfEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusIfEntryIndex.setDescription('Interface group index assigned to this port.')
hdsl2StatusShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusShelfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusShelfIndex.setDescription("TNT's HDSL2 modules Shelf ID.")
hdsl2StatusSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusSlotIndex.setDescription("TNT's HDSL2 modules Slot ID.")
hdsl2StatusLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusLineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusLineIndex.setDescription('HDSL2 modules line ID.')
hdsl2StatusUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("coe", 2), ("cpe", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusUnitType.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusUnitType.setDescription('Unit type defines if the unit is operating either as a Central Office Equipment (COE) or Customer Premiss equipment (CPE).')
hdsl2StatusLineState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("other", 1), ("configure", 2), ("deactivate", 3), ("deactive-lost", 4), ("start-up", 5), ("pend-port-up", 6), ("up", 7), ("pend-deactivate", 8), ("out-of-service", 9), ("analog-loopback", 10), ("digital-loopback", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusLineState.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusLineState.setDescription('Interface state describes the current ports operating state. States are: Config, Pend Down, Up, Down, Start-up, or N/A.')
hdsl2StatusOpRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1552000))).clone(namedValues=NamedValues(("m1552000", 1552000)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2StatusOpRate.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusOpRate.setDescription('The current symetrical operation rate')
hdsl2StatusVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusVendorId.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusVendorId.setDescription('Vendor identification.')
hdsl2StatusMajorFirmWareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusMajorFirmWareVer.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusMajorFirmWareVer.setDescription('Major firmware version.')
hdsl2StatusMinorFirmWareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusMinorFirmWareVer.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusMinorFirmWareVer.setDescription('Minor firmware version.')
hdsl2StatusHardWareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatusHardWareVer.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatusHardWareVer.setDescription('Hardware version.')
hdsl2LineStatisticTable = MibTable((1, 3, 6, 1, 4, 1, 529, 4, 12, 2), )
if mibBuilder.loadTexts: hdsl2LineStatisticTable.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2LineStatisticTable.setDescription('HDSL2 statistical parameters.')
hdsl2LineStatisticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1), ).setIndexNames((0, "ASCEND-HDSL2-MIB", "hdsl2StatIfEntryIndex"))
if mibBuilder.loadTexts: hdsl2LineStatisticEntry.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2LineStatisticEntry.setDescription('A interface statistical entry containing objects to describe the interface.')
hdsl2StatIfEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatIfEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatIfEntryIndex.setDescription('The interface groups interface index is used to index into this table.')
hdsl2StatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatShelfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatShelfIndex.setDescription('HDSL2 modules Shelf ID.')
hdsl2StatSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatSlotIndex.setDescription('HDSL2 modules Slot ID.')
hdsl2StatLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatLineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatLineIndex.setDescription('HDSL2 modules interface ID.')
hdsl2StatConnUpDays = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatConnUpDays.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatConnUpDays.setDescription('Connection up day count.')
hdsl2StatConnUpHours = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatConnUpHours.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatConnUpHours.setDescription('Connection Up 24 hour count.')
hdsl2StatConnUpMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatConnUpMinutes.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatConnUpMinutes.setDescription('Connection up minute count.')
hdsl2StatRxSignalPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatRxSignalPresent.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatRxSignalPresent.setDescription('Receive signal present detection.')
hdsl2StatLineQualityDb = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatLineQualityDb.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatLineQualityDb.setDescription('Lines noise margin. Reliable data will transfer with a reading of ??? or greater.')
hdsl2StatUpDwnCntr = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatUpDwnCntr.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatUpDwnCntr.setDescription('Line Up Down counter value displays the number of times the interface transitions from a down to up state.')
hdsl2StatLineSelfTest = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 1, 2, 3))).clone(namedValues=NamedValues(("other", 4), ("selfTestFailed", 1), ("localLoopBackFailed", 2), ("passed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatLineSelfTest.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatLineSelfTest.setDescription('Line hardware self test results (Passed or Failed).')
hdsl2StatTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatTxPower.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatTxPower.setDescription('Lines transmit power.')
hdsl2StatFramerCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatFramerCrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatFramerCrcErrors.setDescription('Lines framer CRC errors.')
hdsl2StatFramerSyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatFramerSyncStatus.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatFramerSyncStatus.setDescription('Lines framer sync status .')
hdsl2StatFramerLosdCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatFramerLosdCnt.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatFramerLosdCnt.setDescription('Lines framer ???.')
hdsl2StatFramerSegaCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatFramerSegaCnt.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatFramerSegaCnt.setDescription('Lines framer ???.')
hdsl2StatFramerSegdCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatFramerSegdCnt.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatFramerSegdCnt.setDescription('Lines framer ???.')
hdsl2StatFramerRxHecErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatFramerRxHecErrors.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatFramerRxHecErrors.setDescription('Lines framer ???.')
hdsl2StatBertTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("one-minute", 1), ("two-minutes", 2), ("three-minutes", 3), ("four-minutes", 4), ("five-minutes", 5), ("ten-minutes", 6), ("fifteen-minutes", 7), ("twenty-minutes", 8), ("thirty-minutes", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2StatBertTimer.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatBertTimer.setDescription('BER test duration configuration. The BER test lasts for the duration of this timer.')
hdsl2StatBertEna = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hdsl2StatBertEna.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatBertEna.setDescription('Enable/disable of the BER test. If nodes are connected, then the BER test is ran between the units. If this node is not connected to a remote node, then the interface is placed into analog loopback and the BER test is started.')
hdsl2StatBertState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("stopped", 2), ("start-up", 3), ("waiting", 4), ("pend-active", 5), ("bert-los", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatBertState.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatBertState.setDescription("BER test states. When this node is not connected to another node, the test is disabled. When two nodes are connected then the BER test waits for the other node to start it's BER test and then starts collecting bit errors immediately.")
hdsl2StatBertErrorCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 12, 2, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hdsl2StatBertErrorCounter.setStatus('mandatory')
if mibBuilder.loadTexts: hdsl2StatBertErrorCounter.setDescription('BER test bit error counter.')
mibBuilder.exportSymbols("ASCEND-HDSL2-MIB", hdsl2StatConnUpDays=hdsl2StatConnUpDays, hdsl2StatUpDwnCntr=hdsl2StatUpDwnCntr, hdsl2StatusLineIndex=hdsl2StatusLineIndex, hdsl2LineStatusEntry=hdsl2LineStatusEntry, hdsl2StatBertErrorCounter=hdsl2StatBertErrorCounter, hdsl2LineStatisticTable=hdsl2LineStatisticTable, hdsl2StatLineQualityDb=hdsl2StatLineQualityDb, hdsl2StatusHardWareVer=hdsl2StatusHardWareVer, hdsl2LineStatisticEntry=hdsl2LineStatisticEntry, hdsl2StatusSlotIndex=hdsl2StatusSlotIndex, hdsl2StatTxPower=hdsl2StatTxPower, hdsl2StatFramerSyncStatus=hdsl2StatFramerSyncStatus, hdsl2StatShelfIndex=hdsl2StatShelfIndex, hdsl2StatLineIndex=hdsl2StatLineIndex, hdsl2StatFramerSegdCnt=hdsl2StatFramerSegdCnt, hdsl2StatBertTimer=hdsl2StatBertTimer, hdsl2StatusUnitType=hdsl2StatusUnitType, hdsl2StatBertEna=hdsl2StatBertEna, hdsl2StatusOpRate=hdsl2StatusOpRate, hdsl2StatConnUpMinutes=hdsl2StatConnUpMinutes, hdsl2StatusLineState=hdsl2StatusLineState, hdsl2StatusMajorFirmWareVer=hdsl2StatusMajorFirmWareVer, hdsl2StatusVendorId=hdsl2StatusVendorId, hdsl2StatFramerLosdCnt=hdsl2StatFramerLosdCnt, hdsl2StatFramerRxHecErrors=hdsl2StatFramerRxHecErrors, hdsl2StatusShelfIndex=hdsl2StatusShelfIndex, hdsl2StatSlotIndex=hdsl2StatSlotIndex, hdsl2LineStatusTable=hdsl2LineStatusTable, hdsl2StatusMinorFirmWareVer=hdsl2StatusMinorFirmWareVer, hdsl2StatusIfEntryIndex=hdsl2StatusIfEntryIndex, hdsl2StatFramerSegaCnt=hdsl2StatFramerSegaCnt, hdsl2StatIfEntryIndex=hdsl2StatIfEntryIndex, hdsl2StatRxSignalPresent=hdsl2StatRxSignalPresent, hdsl2StatLineSelfTest=hdsl2StatLineSelfTest, hdsl2StatBertState=hdsl2StatBertState, hdsl2StatFramerCrcErrors=hdsl2StatFramerCrcErrors, hdsl2StatConnUpHours=hdsl2StatConnUpHours)
