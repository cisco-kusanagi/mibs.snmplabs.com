#
# PySNMP MIB module XYLAN-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-DS1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:44:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, NotificationType, IpAddress, Unsigned32, ModuleIdentity, MibIdentifier, Integer32, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "NotificationType", "IpAddress", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Integer32", "Bits", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xylanPportArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanPportArch")
dsx1Port = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 11, 1))
dsx1PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1), )
if mibBuilder.loadTexts: dsx1PortConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortConfigTable.setDescription('A table of Dsx1 physical layer status and parameter information.')
dsx1PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1), ).setIndexNames((0, "XYLAN-DS1-MIB", "dsx1PortConfigSlotIndex"), (0, "XYLAN-DS1-MIB", "dsx1PortConfigPortIndex"))
if mibBuilder.loadTexts: dsx1PortConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortConfigEntry.setDescription('An entry in the table, containing information about the physical layer of a Dsx1 interface.')
dsx1PortConfigSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortConfigSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortConfigSlotIndex.setDescription('A unique value which identifies this HSM board slot.')
dsx1PortConfigPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortConfigPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortConfigPortIndex.setDescription('A unique value which identifies this port.')
dsx1PortConfigIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t1", 1), ("e1", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortConfigIfType.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortConfigIfType.setDescription('The type of interface.')
dsx1PortFdlRole = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1PortFdlRole.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortFdlRole.setDescription('Indicates Facility Data Link port role of this port. If the port role is network and fdlMode is set to AT&T 54016, then this port periodically sends AT&T performance requests to CI.')
dsx1PortNfasAlign = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1PortNfasAlign.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortNfasAlign.setDescription('This object indicates if framing criterion is based on bit 2 of Time Slot 0 NOT-FAS. This object only applies to E1.')
dsx1PortConfigYelAlarmDetectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1PortConfigYelAlarmDetectEnable.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortConfigYelAlarmDetectEnable.setDescription('This object indicates whether Yellow Alarm should be detected.')
dsx1PortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2), )
if mibBuilder.loadTexts: dsx1PortStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsTable.setDescription('A table of Dsx1 physical port statistics.')
dsx1PortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1), ).setIndexNames((0, "XYLAN-DS1-MIB", "dsx1PortStatsSlotIndex"), (0, "XYLAN-DS1-MIB", "dsx1PortStatsPortIndex"))
if mibBuilder.loadTexts: dsx1PortStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsEntry.setDescription('An entry in the table, containing information about the physical port statistics of a Dsx1 interface.')
dsx1PortStatsSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsSlotIndex.setDescription('A unique value which identifies this HSM board slot.')
dsx1PortStatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsPortIndex.setDescription('A unique value which identifies this port.')
dsx1PortStatsLossOfSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsLossOfSignal.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsLossOfSignal.setDescription('Total number of Loss of Signals that have been detected on this port.')
dsx1PortStatsOutOfFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsOutOfFrame.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsOutOfFrame.setDescription('Total number of Out of Frames that have been detected on this port.')
dsx1PortStatsRedAlarmEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsRedAlarmEvent.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsRedAlarmEvent.setDescription('Total number of Red Alarm events that have been detected on this port.')
dsx1PortStatsYellowAlarmEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsYellowAlarmEvent.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsYellowAlarmEvent.setDescription('Total number of Yellow Alarm events that have been detected on this port. This object applies to T1 port only.')
dsx1PortStatsSquelchAlarmEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsSquelchAlarmEvent.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsSquelchAlarmEvent.setDescription('Total number of Squelch Alarm events that have been detected on this port.')
dsx1PortStatsBipolarVioEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsBipolarVioEvent.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsBipolarVioEvent.setDescription('Total number of Bipolar Violation events that have been detected on this port.')
dsx1PortStatsAISEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsAISEvent.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsAISEvent.setDescription('Total number of AIS events that have been detected on this port.')
dsx1PortStatsCrcErrorEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsCrcErrorEvent.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsCrcErrorEvent.setDescription('Total number of ESF CRC-6 Error events for T1 or CRC-4 Error Events for E1 that have been detected on this port.')
dsx1PortStatsOutOfSubMultiFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsOutOfSubMultiFrame.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsOutOfSubMultiFrame.setDescription('Total number of out of sub-multiframe events that have been detected on this port. This object only applies to E1 port.')
dsx1PortStatsOutOfTs16MultiFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsOutOfTs16MultiFrame.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsOutOfTs16MultiFrame.setDescription('Total number of out of TS 16 multiframe events that have been detected on this port. This object only applies to E1 port.')
dsx1PortStatsRemFrameAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsRemFrameAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsRemFrameAlarm.setDescription('Total number of Remote Frame Alarm events that have been detected on this port. This object only applies to E1 port.')
dsx1PortStatsRemMultiFrameAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsRemMultiFrameAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsRemMultiFrameAlarm.setDescription('Total number of Remote MultifFame Alarm events that have been detected on this port. This object only applies to E1 port.')
dsx1PortStatsFarEndBlkError = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsFarEndBlkError.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsFarEndBlkError.setDescription('Total number of Far End Block Error events that have been detected on this port. This object only applies to E1 port.')
dsx1PortStatsFramingBitError = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsFramingBitError.setStatus('mandatory')
if mibBuilder.loadTexts: dsx1PortStatsFramingBitError.setDescription('Total number of Framing Bit Error events that have been detected on this port.')
mibBuilder.exportSymbols("XYLAN-DS1-MIB", dsx1PortStatsRedAlarmEvent=dsx1PortStatsRedAlarmEvent, dsx1PortStatsLossOfSignal=dsx1PortStatsLossOfSignal, dsx1PortConfigTable=dsx1PortConfigTable, dsx1PortStatsOutOfTs16MultiFrame=dsx1PortStatsOutOfTs16MultiFrame, dsx1PortConfigSlotIndex=dsx1PortConfigSlotIndex, dsx1PortConfigPortIndex=dsx1PortConfigPortIndex, dsx1PortStatsSquelchAlarmEvent=dsx1PortStatsSquelchAlarmEvent, dsx1PortStatsTable=dsx1PortStatsTable, dsx1PortConfigEntry=dsx1PortConfigEntry, dsx1PortStatsCrcErrorEvent=dsx1PortStatsCrcErrorEvent, dsx1PortConfigYelAlarmDetectEnable=dsx1PortConfigYelAlarmDetectEnable, dsx1PortStatsRemFrameAlarm=dsx1PortStatsRemFrameAlarm, dsx1PortStatsRemMultiFrameAlarm=dsx1PortStatsRemMultiFrameAlarm, dsx1PortFdlRole=dsx1PortFdlRole, dsx1PortStatsOutOfSubMultiFrame=dsx1PortStatsOutOfSubMultiFrame, dsx1PortStatsBipolarVioEvent=dsx1PortStatsBipolarVioEvent, dsx1PortStatsEntry=dsx1PortStatsEntry, dsx1PortStatsAISEvent=dsx1PortStatsAISEvent, dsx1PortStatsOutOfFrame=dsx1PortStatsOutOfFrame, dsx1PortStatsSlotIndex=dsx1PortStatsSlotIndex, dsx1PortConfigIfType=dsx1PortConfigIfType, dsx1PortStatsYellowAlarmEvent=dsx1PortStatsYellowAlarmEvent, dsx1PortStatsFarEndBlkError=dsx1PortStatsFarEndBlkError, dsx1PortNfasAlign=dsx1PortNfasAlign, dsx1PortStatsPortIndex=dsx1PortStatsPortIndex, dsx1PortStatsFramingBitError=dsx1PortStatsFramingBitError, dsx1Port=dsx1Port)
