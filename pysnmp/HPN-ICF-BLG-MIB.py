#
# PySNMP MIB module HPN-ICF-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-BLG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:25:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Counter64, Unsigned32, ObjectIdentity, NotificationType, MibIdentifier, ModuleIdentity, IpAddress, Integer32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Counter64", "Unsigned32", "ObjectIdentity", "NotificationType", "MibIdentifier", "ModuleIdentity", "IpAddress", "Integer32", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfBlg = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108))
hpnicfBlg.setRevisions(('2009-09-15 11:11',))
if mibBuilder.loadTexts: hpnicfBlg.setLastUpdated('200909151111Z')
if mibBuilder.loadTexts: hpnicfBlg.setOrganization('')
class CounterClear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

hpnicfBlgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1))
hpnicfBlgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1), )
if mibBuilder.loadTexts: hpnicfBlgStatsTable.setStatus('current')
hpnicfBlgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-BLG-MIB", "hpnicfBlgIndex"))
if mibBuilder.loadTexts: hpnicfBlgStatsEntry.setStatus('current')
hpnicfBlgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfBlgIndex.setStatus('current')
hpnicfBlgGroupTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupTxPacketCount.setStatus('current')
hpnicfBlgGroupRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupRxPacketCount.setStatus('current')
hpnicfBlgGroupTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupTxByteCount.setStatus('current')
hpnicfBlgGroupRxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupRxByteCount.setStatus('current')
hpnicfBlgGroupCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 6), CounterClear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfBlgGroupCountClear.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-BLG-MIB", hpnicfBlgStatsTable=hpnicfBlgStatsTable, hpnicfBlgGroupTxPacketCount=hpnicfBlgGroupTxPacketCount, hpnicfBlgGroupRxPacketCount=hpnicfBlgGroupRxPacketCount, hpnicfBlg=hpnicfBlg, hpnicfBlgStatsEntry=hpnicfBlgStatsEntry, hpnicfBlgIndex=hpnicfBlgIndex, hpnicfBlgGroupRxByteCount=hpnicfBlgGroupRxByteCount, hpnicfBlgGroupCountClear=hpnicfBlgGroupCountClear, CounterClear=CounterClear, hpnicfBlgObjects=hpnicfBlgObjects, PYSNMP_MODULE_ID=hpnicfBlg, hpnicfBlgGroupTxByteCount=hpnicfBlgGroupTxByteCount)
