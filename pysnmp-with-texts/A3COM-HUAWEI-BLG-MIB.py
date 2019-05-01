#
# PySNMP MIB module A3COM-HUAWEI-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-BLG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:03:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, TimeTicks, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, IpAddress, ModuleIdentity, Unsigned32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "TimeTicks", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "IpAddress", "ModuleIdentity", "Unsigned32", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cBlg = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108))
h3cBlg.setRevisions(('2009-09-15 11:11',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cBlg.setRevisionsDescriptions(('The initial version of this MIB.',))
if mibBuilder.loadTexts: h3cBlg.setLastUpdated('200909151111Z')
if mibBuilder.loadTexts: h3cBlg.setOrganization('H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cBlg.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cBlg.setDescription('This MIB module defines a set of basic objects for configuring switches and routers to set/get balance group information.')
class CounterClear(TextualConvention, Integer32):
    description = "Cleared: reset the value of the group's counter. Nouse: 'nouse' will be returned when getting."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

h3cBlgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1))
h3cBlgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1), )
if mibBuilder.loadTexts: h3cBlgStatsTable.setStatus('current')
if mibBuilder.loadTexts: h3cBlgStatsTable.setDescription('This table contains the statistics information about balance groups.')
h3cBlgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-BLG-MIB", "h3cBlgIndex"))
if mibBuilder.loadTexts: h3cBlgStatsEntry.setStatus('current')
if mibBuilder.loadTexts: h3cBlgStatsEntry.setDescription('This list contains statistics information.')
h3cBlgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cBlgIndex.setStatus('current')
if mibBuilder.loadTexts: h3cBlgIndex.setDescription('The index of the balance group.')
h3cBlgGroupTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupTxPacketCount.setStatus('current')
if mibBuilder.loadTexts: h3cBlgGroupTxPacketCount.setDescription('When retrieved, this object returns the count of packets the balance group has sent.')
h3cBlgGroupRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupRxPacketCount.setStatus('current')
if mibBuilder.loadTexts: h3cBlgGroupRxPacketCount.setDescription('When retrieved, this object returns the count of packets the balance group has received.')
h3cBlgGroupTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupTxByteCount.setStatus('current')
if mibBuilder.loadTexts: h3cBlgGroupTxByteCount.setDescription('When retrieved, this object returns the count of bytes the balance group has sent.')
h3cBlgGroupRxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupRxByteCount.setStatus('current')
if mibBuilder.loadTexts: h3cBlgGroupRxByteCount.setDescription('When retrieved, this object returns the count of bytes the balance group has received.')
h3cBlgGroupCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 6), CounterClear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBlgGroupCountClear.setStatus('current')
if mibBuilder.loadTexts: h3cBlgGroupCountClear.setDescription('This object is used to reset the counter of the balance group. Read operation is meaningless.')
mibBuilder.exportSymbols("A3COM-HUAWEI-BLG-MIB", h3cBlgGroupRxByteCount=h3cBlgGroupRxByteCount, h3cBlgObjects=h3cBlgObjects, h3cBlgIndex=h3cBlgIndex, h3cBlgStatsEntry=h3cBlgStatsEntry, PYSNMP_MODULE_ID=h3cBlg, h3cBlgStatsTable=h3cBlgStatsTable, h3cBlgGroupRxPacketCount=h3cBlgGroupRxPacketCount, h3cBlgGroupTxPacketCount=h3cBlgGroupTxPacketCount, h3cBlgGroupTxByteCount=h3cBlgGroupTxByteCount, h3cBlgGroupCountClear=h3cBlgGroupCountClear, CounterClear=CounterClear, h3cBlg=h3cBlg)
