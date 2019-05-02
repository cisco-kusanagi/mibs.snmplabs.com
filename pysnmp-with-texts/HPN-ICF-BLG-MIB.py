#
# PySNMP MIB module HPN-ICF-BLG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-BLG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:37:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, Counter64, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, NotificationType, MibIdentifier, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Counter64", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "NotificationType", "MibIdentifier", "iso", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfBlg = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108))
hpnicfBlg.setRevisions(('2009-09-15 11:11',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfBlg.setRevisionsDescriptions(('The initial version of this MIB.',))
if mibBuilder.loadTexts: hpnicfBlg.setLastUpdated('200909151111Z')
if mibBuilder.loadTexts: hpnicfBlg.setOrganization('')
if mibBuilder.loadTexts: hpnicfBlg.setContactInfo('')
if mibBuilder.loadTexts: hpnicfBlg.setDescription('This MIB module defines a set of basic objects for configuring switches and routers to set/get balance group information.')
class CounterClear(TextualConvention, Integer32):
    description = "Cleared: reset the value of the group's counter. Nouse: 'nouse' will be returned when getting."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cleared", 1), ("nouse", 2))

hpnicfBlgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1))
hpnicfBlgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1), )
if mibBuilder.loadTexts: hpnicfBlgStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfBlgStatsTable.setDescription('This table contains the statistics information about balance groups.')
hpnicfBlgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-BLG-MIB", "hpnicfBlgIndex"))
if mibBuilder.loadTexts: hpnicfBlgStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfBlgStatsEntry.setDescription('This list contains statistics information.')
hpnicfBlgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfBlgIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfBlgIndex.setDescription('The index of the balance group.')
hpnicfBlgGroupTxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupTxPacketCount.setStatus('current')
if mibBuilder.loadTexts: hpnicfBlgGroupTxPacketCount.setDescription('When retrieved, this object returns the count of packets the balance group has sent.')
hpnicfBlgGroupRxPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupRxPacketCount.setStatus('current')
if mibBuilder.loadTexts: hpnicfBlgGroupRxPacketCount.setDescription('When retrieved, this object returns the count of packets the balance group has received.')
hpnicfBlgGroupTxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupTxByteCount.setStatus('current')
if mibBuilder.loadTexts: hpnicfBlgGroupTxByteCount.setDescription('When retrieved, this object returns the count of bytes the balance group has sent.')
hpnicfBlgGroupRxByteCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfBlgGroupRxByteCount.setStatus('current')
if mibBuilder.loadTexts: hpnicfBlgGroupRxByteCount.setDescription('When retrieved, this object returns the count of bytes the balance group has received.')
hpnicfBlgGroupCountClear = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 108, 1, 1, 1, 6), CounterClear()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfBlgGroupCountClear.setStatus('current')
if mibBuilder.loadTexts: hpnicfBlgGroupCountClear.setDescription('This object is used to reset the counter of the balance group. Read operation is meaningless.')
mibBuilder.exportSymbols("HPN-ICF-BLG-MIB", hpnicfBlgObjects=hpnicfBlgObjects, PYSNMP_MODULE_ID=hpnicfBlg, hpnicfBlgIndex=hpnicfBlgIndex, hpnicfBlgGroupTxPacketCount=hpnicfBlgGroupTxPacketCount, CounterClear=CounterClear, hpnicfBlgStatsEntry=hpnicfBlgStatsEntry, hpnicfBlgGroupTxByteCount=hpnicfBlgGroupTxByteCount, hpnicfBlgGroupRxPacketCount=hpnicfBlgGroupRxPacketCount, hpnicfBlgStatsTable=hpnicfBlgStatsTable, hpnicfBlgGroupRxByteCount=hpnicfBlgGroupRxByteCount, hpnicfBlg=hpnicfBlg, hpnicfBlgGroupCountClear=hpnicfBlgGroupCountClear)
