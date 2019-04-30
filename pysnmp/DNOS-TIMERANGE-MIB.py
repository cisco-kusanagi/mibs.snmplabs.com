#
# PySNMP MIB module DNOS-TIMERANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-TIMERANGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:37:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, NotificationType, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter64, Gauge32, Counter32, Integer32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "NotificationType", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter64", "Gauge32", "Counter32", "Integer32", "IpAddress", "iso")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
fastPathTimeRange = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53))
fastPathTimeRange.setRevisions(('2011-01-26 00:00', '2009-09-24 00:00',))
if mibBuilder.loadTexts: fastPathTimeRange.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathTimeRange.setOrganization('Dell, Inc.')
fastPathTimeRangeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1))
class TimeRangeAbsoluteDateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TimeRangePeriodicTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class TimeRangePeriodicDate(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

timeRangeAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timeRangeAdminMode.setStatus('current')
timeRangeIndexNextFree = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRangeIndexNextFree.setStatus('current')
timeRangeTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3), )
if mibBuilder.loadTexts: timeRangeTable.setStatus('current')
timeRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1), ).setIndexNames((0, "DNOS-TIMERANGE-MIB", "timeRangeIndex"))
if mibBuilder.loadTexts: timeRangeEntry.setStatus('current')
timeRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: timeRangeIndex.setStatus('current')
timeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeName.setStatus('current')
timeRangeOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("active", 0), ("inactive", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeRangeOperState.setStatus('current')
timeRangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeStatus.setStatus('current')
timeRangeAbsoluteEntryTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4), )
if mibBuilder.loadTexts: timeRangeAbsoluteEntryTable.setStatus('current')
timeRangeAbsoluteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1), ).setIndexNames((0, "DNOS-TIMERANGE-MIB", "timeRangeIndex"), (0, "DNOS-TIMERANGE-MIB", "timeRangeAbsoluteEntryIndex"))
if mibBuilder.loadTexts: timeRangeAbsoluteEntry.setStatus('current')
timeRangeAbsoluteEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)))
if mibBuilder.loadTexts: timeRangeAbsoluteEntryIndex.setStatus('current')
timeRangeAbsoluteStartDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1, 2), TimeRangeAbsoluteDateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeAbsoluteStartDateAndTime.setStatus('current')
timeRangeAbsoluteEndDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1, 3), TimeRangeAbsoluteDateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeAbsoluteEndDateAndTime.setStatus('current')
timeRangeAbsoluteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangeAbsoluteStatus.setStatus('current')
timeRangePeriodicEntryTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5), )
if mibBuilder.loadTexts: timeRangePeriodicEntryTable.setStatus('current')
timeRangePeriodicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1), ).setIndexNames((0, "DNOS-TIMERANGE-MIB", "timeRangeIndex"), (0, "DNOS-TIMERANGE-MIB", "timeRangePeriodicEntryIndex"))
if mibBuilder.loadTexts: timeRangePeriodicEntry.setStatus('current')
timeRangePeriodicEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)))
if mibBuilder.loadTexts: timeRangePeriodicEntryIndex.setStatus('current')
timeRangePeriodicFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicFrequency.setStatus('current')
timeRangePeriodicPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicPattern.setStatus('current')
timeRangePeriodicDayMask = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicDayMask.setStatus('current')
timeRangePeriodicStartDate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 5), TimeRangePeriodicDate()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStartDate.setStatus('current')
timeRangePeriodicStartDay = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 6), Bits().clone(namedValues=NamedValues(("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStartDay.setStatus('current')
timeRangePeriodicStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 7), TimeRangePeriodicTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStartTime.setStatus('current')
timeRangePeriodicEndDate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 8), TimeRangePeriodicDate()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicEndDate.setStatus('current')
timeRangePeriodicEndDay = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 9), Bits().clone(namedValues=NamedValues(("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicEndDay.setStatus('current')
timeRangePeriodicEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 10), TimeRangePeriodicTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicEndTime.setStatus('current')
timeRangePeriodicStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 53, 1, 5, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timeRangePeriodicStatus.setStatus('current')
mibBuilder.exportSymbols("DNOS-TIMERANGE-MIB", timeRangeAbsoluteEntryTable=timeRangeAbsoluteEntryTable, timeRangePeriodicEntryTable=timeRangePeriodicEntryTable, timeRangePeriodicEndDay=timeRangePeriodicEndDay, PYSNMP_MODULE_ID=fastPathTimeRange, timeRangePeriodicStartDate=timeRangePeriodicStartDate, timeRangeName=timeRangeName, timeRangePeriodicFrequency=timeRangePeriodicFrequency, timeRangeAbsoluteEntry=timeRangeAbsoluteEntry, timeRangePeriodicEntry=timeRangePeriodicEntry, TimeRangeAbsoluteDateAndTime=TimeRangeAbsoluteDateAndTime, timeRangePeriodicPattern=timeRangePeriodicPattern, timeRangeStatus=timeRangeStatus, timeRangeAbsoluteStatus=timeRangeAbsoluteStatus, fastPathTimeRangeGroup=fastPathTimeRangeGroup, timeRangePeriodicStartTime=timeRangePeriodicStartTime, timeRangeAbsoluteStartDateAndTime=timeRangeAbsoluteStartDateAndTime, timeRangeOperState=timeRangeOperState, timeRangePeriodicEndTime=timeRangePeriodicEndTime, timeRangePeriodicStatus=timeRangePeriodicStatus, timeRangeIndexNextFree=timeRangeIndexNextFree, timeRangeIndex=timeRangeIndex, fastPathTimeRange=fastPathTimeRange, timeRangeTable=timeRangeTable, timeRangePeriodicEndDate=timeRangePeriodicEndDate, timeRangeAdminMode=timeRangeAdminMode, timeRangeEntry=timeRangeEntry, TimeRangePeriodicDate=TimeRangePeriodicDate, timeRangePeriodicStartDay=timeRangePeriodicStartDay, TimeRangePeriodicTime=TimeRangePeriodicTime, timeRangeAbsoluteEndDateAndTime=timeRangeAbsoluteEndDateAndTime, timeRangePeriodicDayMask=timeRangePeriodicDayMask, timeRangePeriodicEntryIndex=timeRangePeriodicEntryIndex, timeRangeAbsoluteEntryIndex=timeRangeAbsoluteEntryIndex)
