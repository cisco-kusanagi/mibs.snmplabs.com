#
# PySNMP MIB module CISCO-DMN-DSG-REMINDER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-REMINDER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, TimeTicks, Counter64, Unsigned32, ModuleIdentity, MibIdentifier, Bits, NotificationType, iso, Counter32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Bits", "NotificationType", "iso", "Counter32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoDSGReminder = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30))
ciscoDSGReminder.setRevisions(('2010-08-30 11:00', '2010-06-17 06:00', '2010-04-12 06:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGReminder.setRevisionsDescriptions(('V01.00.02 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.01 2010-06-17 The enum option for reminderTimerFrequency is corrected.', 'V01.00.00 2010-04-12 Initial revision.',))
if mibBuilder.loadTexts: ciscoDSGReminder.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGReminder.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGReminder.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGReminder.setDescription('Cisco DSG Reminder Timer MIB.')
reminderTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2))
reminderTimerTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1), )
if mibBuilder.loadTexts: reminderTimerTable.setStatus('current')
if mibBuilder.loadTexts: reminderTimerTable.setDescription('Reminder Timer table.')
reminderTimerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-REMINDER-MIB", "reminderTimerID"))
if mibBuilder.loadTexts: reminderTimerEntry.setStatus('current')
if mibBuilder.loadTexts: reminderTimerEntry.setDescription('Entry for Reminder Timer Table.')
reminderTimerID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50)))
if mibBuilder.loadTexts: reminderTimerID.setStatus('current')
if mibBuilder.loadTexts: reminderTimerID.setDescription('Reminder Timer table Index.')
reminderTimerChType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tv", 1), ("radio", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerChType.setStatus('current')
if mibBuilder.loadTexts: reminderTimerChType.setDescription('Channel type.')
reminderTimerChNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerChNum.setStatus('current')
if mibBuilder.loadTexts: reminderTimerChNum.setDescription('Actual channel number.')
reminderTimerChName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerChName.setStatus('current')
if mibBuilder.loadTexts: reminderTimerChName.setDescription('Name of channel for which timer has been set.')
reminderTimerEvtName = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerEvtName.setStatus('current')
if mibBuilder.loadTexts: reminderTimerEvtName.setDescription('Name of the event for which timer has been set.')
reminderTimerDay = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerDay.setStatus('current')
if mibBuilder.loadTexts: reminderTimerDay.setDescription('On the day to be reminded.')
reminderTimerStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerStartTime.setStatus('current')
if mibBuilder.loadTexts: reminderTimerStartTime.setDescription('Timer start time. Format is yyyy-mm-dd hh:mm:ss')
reminderTimerEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerEndTime.setStatus('current')
if mibBuilder.loadTexts: reminderTimerEndTime.setDescription('Timer end time. Format is yyyy-mm-dd hh:mm:ss')
reminderTimerEvtParentalRating = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerEvtParentalRating.setStatus('current')
if mibBuilder.loadTexts: reminderTimerEvtParentalRating.setDescription('Parental rating of the event to be reminded.')
reminderTimerFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("once", 1), ("daily", 2), ("weekly", 3), ("weekDays", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerFrequency.setStatus('current')
if mibBuilder.loadTexts: reminderTimerFrequency.setDescription('Frequency of timer.')
reminderTimerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 30, 2, 1, 1, 11), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reminderTimerRowStatus.setStatus('current')
if mibBuilder.loadTexts: reminderTimerRowStatus.setDescription(' Status of the row.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-REMINDER-MIB", reminderTimerFrequency=reminderTimerFrequency, ciscoDSGReminder=ciscoDSGReminder, reminderTimerID=reminderTimerID, reminderTimerTable=reminderTimerTable, reminderTimerEntry=reminderTimerEntry, reminderTimerChNum=reminderTimerChNum, reminderTimerRowStatus=reminderTimerRowStatus, reminderTimerEvtParentalRating=reminderTimerEvtParentalRating, reminderTable=reminderTable, reminderTimerChType=reminderTimerChType, reminderTimerStartTime=reminderTimerStartTime, reminderTimerEndTime=reminderTimerEndTime, reminderTimerDay=reminderTimerDay, reminderTimerChName=reminderTimerChName, PYSNMP_MODULE_ID=ciscoDSGReminder, reminderTimerEvtName=reminderTimerEvtName)
