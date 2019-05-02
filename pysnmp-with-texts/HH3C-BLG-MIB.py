#
# PySNMP MIB module HH3C-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-BLG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Unsigned32, TimeTicks, Integer32, IpAddress, Gauge32, Bits, MibIdentifier, ObjectIdentity, Counter64, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Integer32", "IpAddress", "Gauge32", "Bits", "MibIdentifier", "ObjectIdentity", "Counter64", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cBlg = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 108))
hh3cBlg.setRevisions(('2009-09-15 11:11',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cBlg.setRevisionsDescriptions(('The initial version of this MIB.',))
if mibBuilder.loadTexts: hh3cBlg.setLastUpdated('200909151111Z')
if mibBuilder.loadTexts: hh3cBlg.setOrganization('H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cBlg.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cBlg.setDescription('This MIB module defines a set of basic objects for configuring switches and routers to set/get balance group information.')
class CounterClear(TextualConvention, Integer32):
    description = "Cleared: reset the value of the group's counter. Nouse: 'nouse' will be returned when getting."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

hh3cBlgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1))
hh3cBlgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1), )
if mibBuilder.loadTexts: hh3cBlgStatsTable.setStatus('current')
if mibBuilder.loadTexts: hh3cBlgStatsTable.setDescription('This table contains the statistics information about balance groups.')
hh3cBlgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1), ).setIndexNames((0, "HH3C-BLG-MIB", "hh3cBlgIndex"))
if mibBuilder.loadTexts: hh3cBlgStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cBlgStatsEntry.setDescription('This list contains statistics information.')
hh3cBlgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cBlgIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cBlgIndex.setDescription('The index of the balance group.')
hh3cBlgGroupTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBlgGroupTxPacketCount.setStatus('current')
if mibBuilder.loadTexts: hh3cBlgGroupTxPacketCount.setDescription('When retrieved, this object returns the count of packets the balance group has sent.')
hh3cBlgGroupRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBlgGroupRxPacketCount.setStatus('current')
if mibBuilder.loadTexts: hh3cBlgGroupRxPacketCount.setDescription('When retrieved, this object returns the count of packets the balance group has received.')
hh3cBlgGroupTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBlgGroupTxByteCount.setStatus('current')
if mibBuilder.loadTexts: hh3cBlgGroupTxByteCount.setDescription('When retrieved, this object returns the count of bytes the balance group has sent.')
hh3cBlgGroupRxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBlgGroupRxByteCount.setStatus('current')
if mibBuilder.loadTexts: hh3cBlgGroupRxByteCount.setDescription('When retrieved, this object returns the count of bytes the balance group has received.')
hh3cBlgGroupCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 6), CounterClear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cBlgGroupCountClear.setStatus('current')
if mibBuilder.loadTexts: hh3cBlgGroupCountClear.setDescription('This object is used to reset the counter of the balance group. Read operation is meaningless.')
mibBuilder.exportSymbols("HH3C-BLG-MIB", PYSNMP_MODULE_ID=hh3cBlg, hh3cBlg=hh3cBlg, hh3cBlgIndex=hh3cBlgIndex, hh3cBlgGroupRxPacketCount=hh3cBlgGroupRxPacketCount, hh3cBlgObjects=hh3cBlgObjects, hh3cBlgGroupTxByteCount=hh3cBlgGroupTxByteCount, hh3cBlgGroupTxPacketCount=hh3cBlgGroupTxPacketCount, hh3cBlgStatsEntry=hh3cBlgStatsEntry, hh3cBlgGroupCountClear=hh3cBlgGroupCountClear, hh3cBlgGroupRxByteCount=hh3cBlgGroupRxByteCount, CounterClear=CounterClear, hh3cBlgStatsTable=hh3cBlgStatsTable)
