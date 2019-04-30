#
# PySNMP MIB module HH3C-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-BLG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:12:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Gauge32, IpAddress, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Counter64, iso, Counter32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Gauge32", "IpAddress", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Counter64", "iso", "Counter32", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cBlg = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 108))
hh3cBlg.setRevisions(('2009-09-15 11:11',))
if mibBuilder.loadTexts: hh3cBlg.setLastUpdated('200909151111Z')
if mibBuilder.loadTexts: hh3cBlg.setOrganization('H3C Technologies Co., Ltd.')
class CounterClear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

hh3cBlgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1))
hh3cBlgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1), )
if mibBuilder.loadTexts: hh3cBlgStatsTable.setStatus('current')
hh3cBlgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1), ).setIndexNames((0, "HH3C-BLG-MIB", "hh3cBlgIndex"))
if mibBuilder.loadTexts: hh3cBlgStatsEntry.setStatus('current')
hh3cBlgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hh3cBlgIndex.setStatus('current')
hh3cBlgGroupTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBlgGroupTxPacketCount.setStatus('current')
hh3cBlgGroupRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBlgGroupRxPacketCount.setStatus('current')
hh3cBlgGroupTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBlgGroupTxByteCount.setStatus('current')
hh3cBlgGroupRxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cBlgGroupRxByteCount.setStatus('current')
hh3cBlgGroupCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 108, 1, 1, 1, 6), CounterClear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cBlgGroupCountClear.setStatus('current')
mibBuilder.exportSymbols("HH3C-BLG-MIB", hh3cBlgGroupTxByteCount=hh3cBlgGroupTxByteCount, hh3cBlg=hh3cBlg, hh3cBlgGroupTxPacketCount=hh3cBlgGroupTxPacketCount, hh3cBlgIndex=hh3cBlgIndex, PYSNMP_MODULE_ID=hh3cBlg, hh3cBlgGroupRxByteCount=hh3cBlgGroupRxByteCount, hh3cBlgObjects=hh3cBlgObjects, CounterClear=CounterClear, hh3cBlgGroupRxPacketCount=hh3cBlgGroupRxPacketCount, hh3cBlgStatsTable=hh3cBlgStatsTable, hh3cBlgStatsEntry=hh3cBlgStatsEntry, hh3cBlgGroupCountClear=hh3cBlgGroupCountClear)
