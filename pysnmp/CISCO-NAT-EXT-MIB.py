#
# PySNMP MIB module CISCO-NAT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NAT-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Unsigned32, Gauge32, TimeTicks, IpAddress, MibIdentifier, Bits, Integer32, iso, Counter32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Gauge32", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "Integer32", "iso", "Counter32", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoNATExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 532))
ciscoNATExtMIB.setRevisions(('2006-06-05 00:00',))
if mibBuilder.loadTexts: ciscoNATExtMIB.setLastUpdated('200606050000Z')
if mibBuilder.loadTexts: ciscoNATExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoNatExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 0))
ciscoNatExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 1))
ciscoNatExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2))
cneAddrTranslationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1), )
if mibBuilder.loadTexts: cneAddrTranslationStatsTable.setStatus('current')
cneAddrTranslationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cneAddrTranslationStatsEntry.setStatus('current')
cneAddrTranslationNumActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 1), Gauge32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumActive.setStatus('current')
cneAddrTranslationNumPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 2), Unsigned32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumPeak.setStatus('current')
cneAddrTranslation1min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 3), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation1min.setStatus('current')
cneAddrTranslation5min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 4), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation5min.setStatus('current')
ciscoNatExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1))
ciscoNatExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2))
ciscoNatExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1, 1)).setObjects(("CISCO-NAT-EXT-MIB", "ciscoNatExtAddrTransStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtMIBCompliance = ciscoNatExtMIBCompliance.setStatus('current')
ciscoNatExtAddrTransStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2, 1)).setObjects(("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumActive"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumPeak"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation1min"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtAddrTransStatsGroup = ciscoNatExtAddrTransStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NAT-EXT-MIB", ciscoNatExtAddrTransStatsGroup=ciscoNatExtAddrTransStatsGroup, cneAddrTranslationStatsEntry=cneAddrTranslationStatsEntry, ciscoNatExtMIBObjects=ciscoNatExtMIBObjects, PYSNMP_MODULE_ID=ciscoNATExtMIB, cneAddrTranslation5min=cneAddrTranslation5min, cneAddrTranslationNumPeak=cneAddrTranslationNumPeak, ciscoNATExtMIB=ciscoNATExtMIB, ciscoNatExtMIBCompliance=ciscoNatExtMIBCompliance, ciscoNatExtMIBConformance=ciscoNatExtMIBConformance, ciscoNatExtMIBNotifs=ciscoNatExtMIBNotifs, cneAddrTranslationNumActive=cneAddrTranslationNumActive, cneAddrTranslation1min=cneAddrTranslation1min, cneAddrTranslationStatsTable=cneAddrTranslationStatsTable, ciscoNatExtMIBGroups=ciscoNatExtMIBGroups, ciscoNatExtMIBCompliances=ciscoNatExtMIBCompliances)
