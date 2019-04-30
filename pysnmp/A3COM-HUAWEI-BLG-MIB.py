#
# PySNMP MIB module A3COM-HUAWEI-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-BLG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:49:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, ObjectIdentity, IpAddress, ModuleIdentity, Counter64, TimeTicks, iso, MibIdentifier, NotificationType, Integer32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter64", "TimeTicks", "iso", "MibIdentifier", "NotificationType", "Integer32", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cBlg = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108))
h3cBlg.setRevisions(('2009-09-15 11:11',))
if mibBuilder.loadTexts: h3cBlg.setLastUpdated('200909151111Z')
if mibBuilder.loadTexts: h3cBlg.setOrganization('H3C Technologies Co., Ltd.')
class CounterClear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

h3cBlgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1))
h3cBlgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1), )
if mibBuilder.loadTexts: h3cBlgStatsTable.setStatus('current')
h3cBlgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-BLG-MIB", "h3cBlgIndex"))
if mibBuilder.loadTexts: h3cBlgStatsEntry.setStatus('current')
h3cBlgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cBlgIndex.setStatus('current')
h3cBlgGroupTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupTxPacketCount.setStatus('current')
h3cBlgGroupRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupRxPacketCount.setStatus('current')
h3cBlgGroupTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupTxByteCount.setStatus('current')
h3cBlgGroupRxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cBlgGroupRxByteCount.setStatus('current')
h3cBlgGroupCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 108, 1, 1, 1, 6), CounterClear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cBlgGroupCountClear.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-BLG-MIB", h3cBlg=h3cBlg, h3cBlgObjects=h3cBlgObjects, h3cBlgStatsEntry=h3cBlgStatsEntry, h3cBlgGroupTxPacketCount=h3cBlgGroupTxPacketCount, h3cBlgGroupRxByteCount=h3cBlgGroupRxByteCount, PYSNMP_MODULE_ID=h3cBlg, CounterClear=CounterClear, h3cBlgGroupTxByteCount=h3cBlgGroupTxByteCount, h3cBlgIndex=h3cBlgIndex, h3cBlgStatsTable=h3cBlgStatsTable, h3cBlgGroupRxPacketCount=h3cBlgGroupRxPacketCount, h3cBlgGroupCountClear=h3cBlgGroupCountClear)
