#
# PySNMP MIB module HM2-PLATFORM-TIMERANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-TIMERANGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hm2PlatformMibs, = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, IpAddress, ObjectIdentity, ModuleIdentity, Bits, Unsigned32, iso, Counter32, Gauge32, Counter64, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Bits", "Unsigned32", "iso", "Counter32", "Gauge32", "Counter64", "TimeTicks", "NotificationType")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
hm2PlatformTimeRange = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 53))
hm2PlatformTimeRange.setRevisions(('2011-01-26 00:00',))
if mibBuilder.loadTexts: hm2PlatformTimeRange.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: hm2PlatformTimeRange.setOrganization('Hirschmann Automation and Control GmbH')
hm2AgentTimeRangeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 53, 1))
class Hm2AgentTimeRangeAbsoluteDateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class Hm2AgentTimeRangePeriodicTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

hm2AgentTimeRangeIndexNextFree = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentTimeRangeIndexNextFree.setStatus('current')
hm2AgentTimeRangeAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 248), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentTimeRangeAdminMode.setStatus('current')
hm2AgentTimeRangeTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2), )
if mibBuilder.loadTexts: hm2AgentTimeRangeTable.setStatus('current')
hm2AgentTimeRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1), ).setIndexNames((0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangeIndex"))
if mibBuilder.loadTexts: hm2AgentTimeRangeEntry.setStatus('current')
hm2AgentTimeRangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hm2AgentTimeRangeIndex.setStatus('current')
hm2AgentTimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangeName.setStatus('current')
hm2AgentTimeRangeOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("active", 0), ("inactive", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentTimeRangeOperState.setStatus('current')
hm2AgentTimeRangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangeStatus.setStatus('current')
hm2AgentTimeRangeAbsoluteTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3), )
if mibBuilder.loadTexts: hm2AgentTimeRangeAbsoluteTable.setStatus('current')
hm2AgentTimeRangeAbsoluteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1), ).setIndexNames((0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangeIndex"), (0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangeAbsoluteEntryIndex"))
if mibBuilder.loadTexts: hm2AgentTimeRangeAbsoluteEntry.setStatus('current')
hm2AgentTimeRangeAbsoluteEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)))
if mibBuilder.loadTexts: hm2AgentTimeRangeAbsoluteEntryIndex.setStatus('current')
hm2AgentTimeRangeAbsoluteStartDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1, 2), Hm2AgentTimeRangeAbsoluteDateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangeAbsoluteStartDateAndTime.setStatus('current')
hm2AgentTimeRangeAbsoluteEndDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1, 3), Hm2AgentTimeRangeAbsoluteDateAndTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangeAbsoluteEndDateAndTime.setStatus('current')
hm2AgentTimeRangeAbsoluteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangeAbsoluteStatus.setStatus('current')
hm2AgentTimeRangePeriodicTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4), )
if mibBuilder.loadTexts: hm2AgentTimeRangePeriodicTable.setStatus('current')
hm2AgentTimeRangePeriodicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1), ).setIndexNames((0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangeIndex"), (0, "HM2-PLATFORM-TIMERANGE-MIB", "hm2AgentTimeRangePeriodicEntryIndex"))
if mibBuilder.loadTexts: hm2AgentTimeRangePeriodicEntry.setStatus('current')
hm2AgentTimeRangePeriodicEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)))
if mibBuilder.loadTexts: hm2AgentTimeRangePeriodicEntryIndex.setStatus('current')
hm2AgentTimeRangePeriodicStartDay = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 2), Bits().clone(namedValues=NamedValues(("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangePeriodicStartDay.setStatus('current')
hm2AgentTimeRangePeriodicStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 3), Hm2AgentTimeRangePeriodicTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangePeriodicStartTime.setStatus('current')
hm2AgentTimeRangePeriodicEndDay = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 4), Bits().clone(namedValues=NamedValues(("sunday", 1), ("monday", 2), ("tuesday", 3), ("wednesday", 4), ("thursday", 5), ("friday", 6), ("saturday", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangePeriodicEndDay.setStatus('current')
hm2AgentTimeRangePeriodicEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 5), Hm2AgentTimeRangePeriodicTime()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangePeriodicEndTime.setStatus('current')
hm2AgentTimeRangePeriodicStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 53, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hm2AgentTimeRangePeriodicStatus.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-TIMERANGE-MIB", hm2AgentTimeRangePeriodicStartDay=hm2AgentTimeRangePeriodicStartDay, hm2AgentTimeRangePeriodicStatus=hm2AgentTimeRangePeriodicStatus, hm2AgentTimeRangePeriodicEntryIndex=hm2AgentTimeRangePeriodicEntryIndex, hm2AgentTimeRangeName=hm2AgentTimeRangeName, hm2AgentTimeRangeAbsoluteEntryIndex=hm2AgentTimeRangeAbsoluteEntryIndex, hm2AgentTimeRangeGroup=hm2AgentTimeRangeGroup, Hm2AgentTimeRangeAbsoluteDateAndTime=Hm2AgentTimeRangeAbsoluteDateAndTime, hm2AgentTimeRangeIndexNextFree=hm2AgentTimeRangeIndexNextFree, hm2AgentTimeRangePeriodicTable=hm2AgentTimeRangePeriodicTable, hm2AgentTimeRangeEntry=hm2AgentTimeRangeEntry, hm2AgentTimeRangePeriodicEntry=hm2AgentTimeRangePeriodicEntry, hm2PlatformTimeRange=hm2PlatformTimeRange, hm2AgentTimeRangePeriodicStartTime=hm2AgentTimeRangePeriodicStartTime, hm2AgentTimeRangeAbsoluteEntry=hm2AgentTimeRangeAbsoluteEntry, hm2AgentTimeRangeTable=hm2AgentTimeRangeTable, hm2AgentTimeRangeIndex=hm2AgentTimeRangeIndex, hm2AgentTimeRangeAbsoluteTable=hm2AgentTimeRangeAbsoluteTable, hm2AgentTimeRangeOperState=hm2AgentTimeRangeOperState, hm2AgentTimeRangeAdminMode=hm2AgentTimeRangeAdminMode, hm2AgentTimeRangePeriodicEndTime=hm2AgentTimeRangePeriodicEndTime, hm2AgentTimeRangeAbsoluteStartDateAndTime=hm2AgentTimeRangeAbsoluteStartDateAndTime, hm2AgentTimeRangeAbsoluteEndDateAndTime=hm2AgentTimeRangeAbsoluteEndDateAndTime, hm2AgentTimeRangePeriodicEndDay=hm2AgentTimeRangePeriodicEndDay, Hm2AgentTimeRangePeriodicTime=Hm2AgentTimeRangePeriodicTime, PYSNMP_MODULE_ID=hm2PlatformTimeRange, hm2AgentTimeRangeStatus=hm2AgentTimeRangeStatus, hm2AgentTimeRangeAbsoluteStatus=hm2AgentTimeRangeAbsoluteStatus)
