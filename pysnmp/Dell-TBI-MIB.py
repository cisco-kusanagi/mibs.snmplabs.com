#
# PySNMP MIB module Dell-TBI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-TBI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:42:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, TimeTicks, Counter64, Bits, Counter32, Unsigned32, MibIdentifier, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "TimeTicks", "Counter64", "Bits", "Counter32", "Unsigned32", "MibIdentifier", "Gauge32", "ModuleIdentity")
TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
rlTBIMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 145))
rlTBIMib.setRevisions(('2006-02-12 00:00',))
if mibBuilder.loadTexts: rlTBIMib.setLastUpdated('200604040000Z')
if mibBuilder.loadTexts: rlTBIMib.setOrganization('Dell')
rlTBITimeRangeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 145, 1), )
if mibBuilder.loadTexts: rlTBITimeRangeTable.setStatus('current')
rlTBITimeRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 145, 1, 1), ).setIndexNames((1, "Dell-TBI-MIB", "rlTBITimeRangeName"))
if mibBuilder.loadTexts: rlTBITimeRangeEntry.setStatus('current')
rlTBITimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlTBITimeRangeName.setStatus('current')
rlTBITimeRangeAbsoluteStart = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBITimeRangeAbsoluteStart.setStatus('current')
rlTBITimeRangeAbsoluteEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBITimeRangeAbsoluteEnd.setStatus('current')
rlTBITimeRangeActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTBITimeRangeActiveStatus.setStatus('current')
rlTBITimeRangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlTBITimeRangeRowStatus.setStatus('current')
class RlTBIWeekDayList(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("monday", 0), ("tuesday", 1), ("wednesday", 2), ("thursday", 3), ("friday", 4), ("saturday", 5), ("sunday", 6))

rlTBIPeriodicTable = MibTable((1, 3, 6, 1, 4, 1, 89, 145, 2), )
if mibBuilder.loadTexts: rlTBIPeriodicTable.setStatus('current')
rlTBIPeriodicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 145, 2, 1), ).setIndexNames((0, "Dell-TBI-MIB", "rlTBIPeriodicTimeRangeName"), (0, "Dell-TBI-MIB", "rlTBIPeriodicWeekDayList"), (0, "Dell-TBI-MIB", "rlTBIPeriodicStart"), (0, "Dell-TBI-MIB", "rlTBIPeriodicEnd"))
if mibBuilder.loadTexts: rlTBIPeriodicEntry.setStatus('current')
rlTBIPeriodicTimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlTBIPeriodicTimeRangeName.setStatus('current')
rlTBIPeriodicWeekDayList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 2), RlTBIWeekDayList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBIPeriodicWeekDayList.setStatus('current')
rlTBIPeriodicStart = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBIPeriodicStart.setStatus('current')
rlTBIPeriodicEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBIPeriodicEnd.setStatus('current')
rlTBIPeriodicRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlTBIPeriodicRowStatus.setStatus('current')
mibBuilder.exportSymbols("Dell-TBI-MIB", rlTBIPeriodicRowStatus=rlTBIPeriodicRowStatus, rlTBIPeriodicTimeRangeName=rlTBIPeriodicTimeRangeName, rlTBITimeRangeRowStatus=rlTBITimeRangeRowStatus, PYSNMP_MODULE_ID=rlTBIMib, rlTBIPeriodicEntry=rlTBIPeriodicEntry, rlTBITimeRangeAbsoluteEnd=rlTBITimeRangeAbsoluteEnd, rlTBIPeriodicTable=rlTBIPeriodicTable, rlTBITimeRangeTable=rlTBITimeRangeTable, rlTBITimeRangeAbsoluteStart=rlTBITimeRangeAbsoluteStart, rlTBITimeRangeActiveStatus=rlTBITimeRangeActiveStatus, rlTBITimeRangeName=rlTBITimeRangeName, rlTBIMib=rlTBIMib, rlTBIPeriodicStart=rlTBIPeriodicStart, rlTBITimeRangeEntry=rlTBITimeRangeEntry, rlTBIPeriodicEnd=rlTBIPeriodicEnd, rlTBIPeriodicWeekDayList=rlTBIPeriodicWeekDayList, RlTBIWeekDayList=RlTBIWeekDayList)
