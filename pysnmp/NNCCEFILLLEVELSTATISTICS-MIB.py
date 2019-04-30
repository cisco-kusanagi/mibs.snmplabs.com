#
# PySNMP MIB module NNCCEFILLLEVELSTATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCCEFILLLEVELSTATISTICS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nncExtensions, = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncExtensions")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Gauge32, Counter64, Integer32, ObjectIdentity, Unsigned32, IpAddress, TimeTicks, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Counter64", "Integer32", "ObjectIdentity", "Unsigned32", "IpAddress", "TimeTicks", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nncCEFillLevelStatistics = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 47))
if mibBuilder.loadTexts: nncCEFillLevelStatistics.setLastUpdated('9708271200Z')
if mibBuilder.loadTexts: nncCEFillLevelStatistics.setOrganization('Newbridge Networks Corporation')
nncCEFillLevelStatisticsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 47, 1))
nncCEFillLevelStatisticsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 47, 2))
nncCEFillLevelStatisticsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 47, 3))
nncCEFillLevelStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1), )
if mibBuilder.loadTexts: nncCEFillLevelStatisticsTable.setStatus('current')
nncCEFillLevelStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: nncCEFillLevelStatisticsEntry.setStatus('current')
nncCEMinFillLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncCEMinFillLevel.setStatus('current')
nncCEMaxFillLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 47, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncCEMaxFillLevel.setStatus('current')
nncCERawFillLevelStatisticsGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 47, 2, 1)).setObjects(("NNCCEFILLLEVELSTATISTICS-MIB", "nncCEMinFillLevel"), ("NNCCEFILLLEVELSTATISTICS-MIB", "nncCEMaxFillLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncCERawFillLevelStatisticsGroups = nncCERawFillLevelStatisticsGroups.setStatus('current')
nncCEFillLevelStatisticsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 123, 3, 47, 3, 1)).setObjects(("NNCCEFILLLEVELSTATISTICS-MIB", "nncCERawFillLevelStatisticsGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncCEFillLevelStatisticsCompliance = nncCEFillLevelStatisticsCompliance.setStatus('current')
mibBuilder.exportSymbols("NNCCEFILLLEVELSTATISTICS-MIB", PYSNMP_MODULE_ID=nncCEFillLevelStatistics, nncCEFillLevelStatistics=nncCEFillLevelStatistics, nncCEFillLevelStatisticsGroups=nncCEFillLevelStatisticsGroups, nncCEFillLevelStatisticsTable=nncCEFillLevelStatisticsTable, nncCERawFillLevelStatisticsGroups=nncCERawFillLevelStatisticsGroups, nncCEFillLevelStatisticsObjects=nncCEFillLevelStatisticsObjects, nncCEMaxFillLevel=nncCEMaxFillLevel, nncCEMinFillLevel=nncCEMinFillLevel, nncCEFillLevelStatisticsCompliances=nncCEFillLevelStatisticsCompliances, nncCEFillLevelStatisticsCompliance=nncCEFillLevelStatisticsCompliance, nncCEFillLevelStatisticsEntry=nncCEFillLevelStatisticsEntry)
