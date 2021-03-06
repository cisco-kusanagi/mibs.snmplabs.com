#
# PySNMP MIB module NNCBELLCOREGR820DS1STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCBELLCOREGR820DS1STATISTICS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nncExtensions, = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncExtensions")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, IpAddress, ObjectIdentity, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, iso, Counter64, Integer32, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "IpAddress", "ObjectIdentity", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "iso", "Counter64", "Integer32", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nncBellcoreGR820Ds1Statistics = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 70))
if mibBuilder.loadTexts: nncBellcoreGR820Ds1Statistics.setLastUpdated('9902151200Z')
if mibBuilder.loadTexts: nncBellcoreGR820Ds1Statistics.setOrganization('Newbridge Networks Corporation')
nncBellcoreGR820Ds1StatisticsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 70, 1))
nncBellcoreGR820Ds1StatisticsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 70, 2))
nncBellcoreGR820Ds1StatisticsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 70, 3))
nncBellcoreGR820Ds1CurrStatsTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1), )
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrStatsTable.setStatus('current')
nncBellcoreGR820Ds1CurrStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrStatsEntry.setStatus('current')
nncBellcoreGR820Ds1CurrLineCV = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrLineCV.setStatus('current')
nncBellcoreGR820Ds1CurrLineES = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrLineES.setStatus('current')
nncBellcoreGR820Ds1CurrLineLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrLineLOSS.setStatus('current')
nncBellcoreGR820Ds1CurrPathCV = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrPathCV.setStatus('current')
nncBellcoreGR820Ds1CurrPathES = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrPathES.setStatus('current')
nncBellcoreGR820Ds1CurrPathSES = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrPathSES.setStatus('current')
nncBellcoreGR820Ds1CurrPathAISS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrPathAISS.setStatus('current')
nncBellcoreGR820Ds1CurrPathCSS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrPathCSS.setStatus('current')
nncBellcoreGR820Ds1CurrPathUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrPathUAS.setStatus('current')
nncBellcoreGR820Ds1CurrPathSAS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrPathSAS.setStatus('current')
nncBellcoreGR820Ds1CurrPathFC = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1CurrPathFC.setStatus('current')
nncBellcoreGR820Ds1IntervalStatsTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2), )
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalStatsTable.setStatus('current')
nncBellcoreGR820Ds1IntervalStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalIndex"))
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalStatsEntry.setStatus('current')
nncBellcoreGR820Ds1IntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalIndex.setStatus('current')
nncBellcoreGR820Ds1IntervalLineCV = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalLineCV.setStatus('current')
nncBellcoreGR820Ds1IntervalLineES = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalLineES.setStatus('current')
nncBellcoreGR820Ds1IntervalLineLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalLineLOSS.setStatus('current')
nncBellcoreGR820Ds1IntervalPathCV = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalPathCV.setStatus('current')
nncBellcoreGR820Ds1IntervalPathES = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalPathES.setStatus('current')
nncBellcoreGR820Ds1IntervalPathSES = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalPathSES.setStatus('current')
nncBellcoreGR820Ds1IntervalPathAISS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalPathAISS.setStatus('current')
nncBellcoreGR820Ds1IntervalPathCSS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalPathCSS.setStatus('current')
nncBellcoreGR820Ds1IntervalPathUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalPathUAS.setStatus('current')
nncBellcoreGR820Ds1IntervalPathSAS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalPathSAS.setStatus('current')
nncBellcoreGR820Ds1IntervalPathFC = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1IntervalPathFC.setStatus('current')
nncBellcoreGR820Ds1TotalStatsTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3), )
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalStatsTable.setStatus('current')
nncBellcoreGR820Ds1TotalStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalStatsEntry.setStatus('current')
nncBellcoreGR820Ds1TotalLineCV = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalLineCV.setStatus('current')
nncBellcoreGR820Ds1TotalLineES = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalLineES.setStatus('current')
nncBellcoreGR820Ds1TotalLineLOSS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalLineLOSS.setStatus('current')
nncBellcoreGR820Ds1TotalPathCV = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalPathCV.setStatus('current')
nncBellcoreGR820Ds1TotalPathES = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalPathES.setStatus('current')
nncBellcoreGR820Ds1TotalPathSES = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalPathSES.setStatus('current')
nncBellcoreGR820Ds1TotalPathAISS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalPathAISS.setStatus('current')
nncBellcoreGR820Ds1TotalPathCSS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalPathCSS.setStatus('current')
nncBellcoreGR820Ds1TotalPathUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalPathUAS.setStatus('current')
nncBellcoreGR820Ds1TotalPathSAS = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalPathSAS.setStatus('current')
nncBellcoreGR820Ds1TotalPathFC = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 70, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncBellcoreGR820Ds1TotalPathFC.setStatus('current')
nncBellcoreGR820Ds1CurrStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 70, 2, 1)).setObjects(("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrLineCV"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrLineES"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrLineLOSS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathCV"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathES"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathSES"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathAISS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathCSS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathUAS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathSAS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrPathFC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncBellcoreGR820Ds1CurrStatsGroup = nncBellcoreGR820Ds1CurrStatsGroup.setStatus('current')
nncBellcoreGR820Ds1IntervalStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 70, 2, 2)).setObjects(("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalIndex"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalLineCV"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalLineES"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalLineLOSS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathCV"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathES"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathSES"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathAISS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathCSS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathUAS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathSAS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalPathFC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncBellcoreGR820Ds1IntervalStatsGroup = nncBellcoreGR820Ds1IntervalStatsGroup.setStatus('current')
nncBellcoreGR820Ds1TotalStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 123, 3, 70, 2, 3)).setObjects(("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalLineCV"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalLineES"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalLineLOSS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathCV"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathES"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathSES"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathAISS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathCSS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathUAS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathSAS"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalPathFC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncBellcoreGR820Ds1TotalStatsGroup = nncBellcoreGR820Ds1TotalStatsGroup.setStatus('current')
nncBellcoreGR820Ds1StatisticsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 123, 3, 70, 3, 1)).setObjects(("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1CurrStatsGroup"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1IntervalStatsGroup"), ("NNCBELLCOREGR820DS1STATISTICS-MIB", "nncBellcoreGR820Ds1TotalStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nncBellcoreGR820Ds1StatisticsCompliance = nncBellcoreGR820Ds1StatisticsCompliance.setStatus('current')
mibBuilder.exportSymbols("NNCBELLCOREGR820DS1STATISTICS-MIB", nncBellcoreGR820Ds1TotalPathSAS=nncBellcoreGR820Ds1TotalPathSAS, nncBellcoreGR820Ds1TotalStatsEntry=nncBellcoreGR820Ds1TotalStatsEntry, nncBellcoreGR820Ds1TotalStatsGroup=nncBellcoreGR820Ds1TotalStatsGroup, nncBellcoreGR820Ds1CurrLineLOSS=nncBellcoreGR820Ds1CurrLineLOSS, nncBellcoreGR820Ds1CurrStatsGroup=nncBellcoreGR820Ds1CurrStatsGroup, nncBellcoreGR820Ds1IntervalPathCSS=nncBellcoreGR820Ds1IntervalPathCSS, nncBellcoreGR820Ds1IntervalPathFC=nncBellcoreGR820Ds1IntervalPathFC, nncBellcoreGR820Ds1TotalLineES=nncBellcoreGR820Ds1TotalLineES, nncBellcoreGR820Ds1TotalPathSES=nncBellcoreGR820Ds1TotalPathSES, nncBellcoreGR820Ds1CurrPathES=nncBellcoreGR820Ds1CurrPathES, nncBellcoreGR820Ds1TotalPathES=nncBellcoreGR820Ds1TotalPathES, nncBellcoreGR820Ds1CurrLineES=nncBellcoreGR820Ds1CurrLineES, nncBellcoreGR820Ds1CurrStatsTable=nncBellcoreGR820Ds1CurrStatsTable, nncBellcoreGR820Ds1CurrStatsEntry=nncBellcoreGR820Ds1CurrStatsEntry, nncBellcoreGR820Ds1TotalPathAISS=nncBellcoreGR820Ds1TotalPathAISS, nncBellcoreGR820Ds1CurrPathSAS=nncBellcoreGR820Ds1CurrPathSAS, nncBellcoreGR820Ds1IntervalPathUAS=nncBellcoreGR820Ds1IntervalPathUAS, nncBellcoreGR820Ds1IntervalStatsGroup=nncBellcoreGR820Ds1IntervalStatsGroup, nncBellcoreGR820Ds1CurrPathSES=nncBellcoreGR820Ds1CurrPathSES, nncBellcoreGR820Ds1IntervalPathSAS=nncBellcoreGR820Ds1IntervalPathSAS, nncBellcoreGR820Ds1Statistics=nncBellcoreGR820Ds1Statistics, nncBellcoreGR820Ds1StatisticsObjects=nncBellcoreGR820Ds1StatisticsObjects, nncBellcoreGR820Ds1CurrPathCV=nncBellcoreGR820Ds1CurrPathCV, nncBellcoreGR820Ds1TotalLineLOSS=nncBellcoreGR820Ds1TotalLineLOSS, nncBellcoreGR820Ds1IntervalStatsEntry=nncBellcoreGR820Ds1IntervalStatsEntry, nncBellcoreGR820Ds1TotalLineCV=nncBellcoreGR820Ds1TotalLineCV, nncBellcoreGR820Ds1TotalStatsTable=nncBellcoreGR820Ds1TotalStatsTable, nncBellcoreGR820Ds1IntervalIndex=nncBellcoreGR820Ds1IntervalIndex, PYSNMP_MODULE_ID=nncBellcoreGR820Ds1Statistics, nncBellcoreGR820Ds1CurrLineCV=nncBellcoreGR820Ds1CurrLineCV, nncBellcoreGR820Ds1CurrPathAISS=nncBellcoreGR820Ds1CurrPathAISS, nncBellcoreGR820Ds1TotalPathUAS=nncBellcoreGR820Ds1TotalPathUAS, nncBellcoreGR820Ds1TotalPathCSS=nncBellcoreGR820Ds1TotalPathCSS, nncBellcoreGR820Ds1CurrPathFC=nncBellcoreGR820Ds1CurrPathFC, nncBellcoreGR820Ds1IntervalPathSES=nncBellcoreGR820Ds1IntervalPathSES, nncBellcoreGR820Ds1StatisticsGroups=nncBellcoreGR820Ds1StatisticsGroups, nncBellcoreGR820Ds1IntervalStatsTable=nncBellcoreGR820Ds1IntervalStatsTable, nncBellcoreGR820Ds1TotalPathFC=nncBellcoreGR820Ds1TotalPathFC, nncBellcoreGR820Ds1TotalPathCV=nncBellcoreGR820Ds1TotalPathCV, nncBellcoreGR820Ds1IntervalLineES=nncBellcoreGR820Ds1IntervalLineES, nncBellcoreGR820Ds1IntervalPathCV=nncBellcoreGR820Ds1IntervalPathCV, nncBellcoreGR820Ds1StatisticsCompliances=nncBellcoreGR820Ds1StatisticsCompliances, nncBellcoreGR820Ds1IntervalPathES=nncBellcoreGR820Ds1IntervalPathES, nncBellcoreGR820Ds1IntervalLineCV=nncBellcoreGR820Ds1IntervalLineCV, nncBellcoreGR820Ds1CurrPathCSS=nncBellcoreGR820Ds1CurrPathCSS, nncBellcoreGR820Ds1IntervalLineLOSS=nncBellcoreGR820Ds1IntervalLineLOSS, nncBellcoreGR820Ds1CurrPathUAS=nncBellcoreGR820Ds1CurrPathUAS, nncBellcoreGR820Ds1IntervalPathAISS=nncBellcoreGR820Ds1IntervalPathAISS, nncBellcoreGR820Ds1StatisticsCompliance=nncBellcoreGR820Ds1StatisticsCompliance)
