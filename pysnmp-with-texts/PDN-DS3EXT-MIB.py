#
# PySNMP MIB module PDN-DS3EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DS3EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dsx3TotalEntry, dsx3IntervalEntry, dsx3CurrentEntry = mibBuilder.importSymbols("DS3-MIB", "dsx3TotalEntry", "dsx3IntervalEntry", "dsx3CurrentEntry")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
PerfCurrentCount, PerfTotalCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfTotalCount", "PerfIntervalCount")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, Counter32, Gauge32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Integer32, Counter64, Bits, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Counter32", "Gauge32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Integer32", "Counter64", "Bits", "IpAddress", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
pdnDs3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14))
pdnDs3MIB.setRevisions(('1902-07-10 00:00', '1902-07-05 00:00', '1900-05-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pdnDs3MIB.setRevisionsDescriptions(('M. Mohankumar Changed the index of devDs3FreeRunTable to Augment dsx3TotalEntry.', 'M. Mohankumar Added devDs3FreeRunTable that has the free running counters for physical performance stats.', 'J. Strain o add devDs3ConfigTimingMarkerCode o augment the DS3/E3 Near End Group o to add EB,ES,SES,PlcpSEFS for current o , interval and total tables o Initial Release',))
if mibBuilder.loadTexts: pdnDs3MIB.setLastUpdated('0207050000Z')
if mibBuilder.loadTexts: pdnDs3MIB.setOrganization('Paradyne Networks MIB Working Group')
if mibBuilder.loadTexts: pdnDs3MIB.setContactInfo('Paradyne Networks 331 Newman Springs Road Red Bank, NJ 07701 www.paradyne.com General Comments to: mibwg_team@eng.paradyne.com')
if mibBuilder.loadTexts: pdnDs3MIB.setDescription('This MIB Module extends the DS3-MIB defined in rfc2496')
devDs3Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1))
devDs3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1), )
if mibBuilder.loadTexts: devDs3ConfigTable.setStatus('current')
if mibBuilder.loadTexts: devDs3ConfigTable.setDescription('The Paradyne Ds3-MIB Table Augment.')
devDs3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1), ).setIndexNames((0, "PDN-DS3EXT-MIB", "devDs3ConfigIfIndex"))
if mibBuilder.loadTexts: devDs3ConfigEntry.setStatus('current')
if mibBuilder.loadTexts: devDs3ConfigEntry.setDescription('An entry in the Paradyne Ds3-MIB Table.')
devDs3ConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3ConfigIfIndex.setStatus('current')
if mibBuilder.loadTexts: devDs3ConfigIfIndex.setDescription('The index value which uniquely identifies the interface for which this entry contains information on interface tests. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex from the Interfaces table of MIB II (RFC 1213).')
devDs3ConfigFramingType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("direct", 1), ("plcp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDs3ConfigFramingType.setStatus('current')
if mibBuilder.loadTexts: devDs3ConfigFramingType.setDescription('The option provides the support for Direct Mapping or Physicial Layer Convergence Protocol (PLCP) mapping of ATM Cells into a Ds3 C-Bit Parity Format')
devDs3ConfigIgnoreCbit = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDs3ConfigIgnoreCbit.setStatus('current')
if mibBuilder.loadTexts: devDs3ConfigIgnoreCbit.setDescription('Since not all networks support the C-Bit, we allow the ability to disable the accumulation of C-Bit errors and the generation of C-Bit Alarms.')
devDs3ConfigTimingMarkerCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("traceable", 1), ("notTraceable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devDs3ConfigTimingMarkerCode.setStatus('current')
if mibBuilder.loadTexts: devDs3ConfigTimingMarkerCode.setDescription("The option supports the ability to send a 'Timing Marker' code to the far end.")
devDs3CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2), )
if mibBuilder.loadTexts: devDs3CurrentTable.setStatus('current')
if mibBuilder.loadTexts: devDs3CurrentTable.setDescription('The Paradyne Extension to the Near End Current Table of the DS3-MIB.')
devDs3CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1), )
dsx3CurrentEntry.registerAugmentions(("PDN-DS3EXT-MIB", "devDs3CurrentEntry"))
devDs3CurrentEntry.setIndexNames(*dsx3CurrentEntry.getIndexNames())
if mibBuilder.loadTexts: devDs3CurrentEntry.setStatus('current')
if mibBuilder.loadTexts: devDs3CurrentEntry.setDescription('An entry in the Paradyne Extension to the dsx3CurrentTable of the DS3-MIB.')
devDs3CurrentEB = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1, 1), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3CurrentEB.setStatus('current')
if mibBuilder.loadTexts: devDs3CurrentEB.setDescription('The counter associated with the number of Errored Blocks')
devDs3CurrentES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1, 2), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3CurrentES.setStatus('current')
if mibBuilder.loadTexts: devDs3CurrentES.setDescription('The counter associated with the number of Errored Seconds')
devDs3CurrentSES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1, 3), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3CurrentSES.setStatus('current')
if mibBuilder.loadTexts: devDs3CurrentSES.setDescription('The counter associated with the number of Severly Errored Seconds')
devDs3CurrentPlcpSEFS = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 2, 1, 4), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3CurrentPlcpSEFS.setStatus('current')
if mibBuilder.loadTexts: devDs3CurrentPlcpSEFS.setDescription('The counter associated with the number of PLCP Severely Errored Framing Seconds')
devDs3IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3), )
if mibBuilder.loadTexts: devDs3IntervalTable.setStatus('current')
if mibBuilder.loadTexts: devDs3IntervalTable.setDescription('The Paradyne Extension to the Near End Interval Table of the DS3-MIB.')
devDs3IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1), )
dsx3IntervalEntry.registerAugmentions(("PDN-DS3EXT-MIB", "devDs3IntervalEntry"))
devDs3IntervalEntry.setIndexNames(*dsx3IntervalEntry.getIndexNames())
if mibBuilder.loadTexts: devDs3IntervalEntry.setStatus('current')
if mibBuilder.loadTexts: devDs3IntervalEntry.setDescription('An entry in the Paradyne Extension to the dsx3IntervalTable of the DS3-MIB.')
devDs3IntervalEB = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3IntervalEB.setStatus('current')
if mibBuilder.loadTexts: devDs3IntervalEB.setDescription('The counter associated with the number of Errored Blocks')
devDs3IntervalES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1, 2), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3IntervalES.setStatus('current')
if mibBuilder.loadTexts: devDs3IntervalES.setDescription('The counter associated with the number of Errored Seconds')
devDs3IntervalSES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1, 3), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3IntervalSES.setStatus('current')
if mibBuilder.loadTexts: devDs3IntervalSES.setDescription('The counter associated with the number of Severly Errored Seconds')
devDs3IntervalPlcpSEFS = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 3, 1, 4), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3IntervalPlcpSEFS.setStatus('current')
if mibBuilder.loadTexts: devDs3IntervalPlcpSEFS.setDescription('The counter associated with the number of PLCP Severely Errored Framing Seconds')
devDs3TotalTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4), )
if mibBuilder.loadTexts: devDs3TotalTable.setStatus('current')
if mibBuilder.loadTexts: devDs3TotalTable.setDescription('The Paradyne Extension to the Near End Total Table of the DS3-MIB.')
devDs3TotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1), )
dsx3TotalEntry.registerAugmentions(("PDN-DS3EXT-MIB", "devDs3TotalEntry"))
devDs3TotalEntry.setIndexNames(*dsx3TotalEntry.getIndexNames())
if mibBuilder.loadTexts: devDs3TotalEntry.setStatus('current')
if mibBuilder.loadTexts: devDs3TotalEntry.setDescription('An entry in the Paradyne Extension to the dsx3TotalTable of the DS3-MIB.')
devDs3TotalEB = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1, 1), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3TotalEB.setStatus('current')
if mibBuilder.loadTexts: devDs3TotalEB.setDescription('The counter associated with the number of Errored Blocks')
devDs3TotalES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1, 2), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3TotalES.setStatus('current')
if mibBuilder.loadTexts: devDs3TotalES.setDescription('The counter associated with the number of Errored Seconds')
devDs3TotalSES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1, 3), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3TotalSES.setStatus('current')
if mibBuilder.loadTexts: devDs3TotalSES.setDescription('The counter associated with the number of Severly Errored Seconds')
devDs3TotalPlcpSEFS = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 4, 1, 4), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3TotalPlcpSEFS.setStatus('current')
if mibBuilder.loadTexts: devDs3TotalPlcpSEFS.setDescription('The counter associated with the number of PLCP Severely Errored Framing Seconds')
devDs3FreeRunTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5), )
if mibBuilder.loadTexts: devDs3FreeRunTable.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunTable.setDescription('The Paradyne Free Running Total of the performance stats.')
devDs3FreeRunEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1), )
dsx3TotalEntry.registerAugmentions(("PDN-DS3EXT-MIB", "devDs3FreeRunEntry"))
devDs3FreeRunEntry.setIndexNames(*dsx3TotalEntry.getIndexNames())
if mibBuilder.loadTexts: devDs3FreeRunEntry.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunEntry.setDescription('An entry in the Paradyne Free Running Total Table.')
devDs3FreeRunPES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 1), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunPES.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunPES.setDescription('The counter associated with the number of P bit Errored Seconds.')
devDs3FreeRunPSES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 2), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunPSES.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunPSES.setDescription('The counter associated with the number of P bit Severely Errored Seconds.')
devDs3FreeRunPSEFS = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 3), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunPSEFS.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunPSEFS.setDescription('The counter associated with the number of Severely Errored Frame Seconds.')
devDs3FreeRunUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 4), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunUAS.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunUAS.setDescription('The counter associated with the number of Unavailable Seconds.')
devDs3FreeRunLCV = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 5), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunLCV.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunLCV.setDescription('The counter associated with the number of Line Coding Violations.')
devDs3FreeRunPCV = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 6), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunPCV.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunPCV.setDescription('The counter associated with the number of P bit Coding Violations.')
devDs3FreeRunLES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 7), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunLES.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunLES.setDescription('The counter associated with the number of Line Erroed Seconds.')
devDs3FreeRunCCV = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 8), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunCCV.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunCCV.setDescription('The counter associated with the number of C bit Coding Violations.')
devDs3FreeRunCES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 9), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunCES.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunCES.setDescription('The counter associated with the number of C bit Errored Seconds.')
devDs3FreeRunCSES = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 14, 1, 5, 1, 10), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devDs3FreeRunCSES.setStatus('current')
if mibBuilder.loadTexts: devDs3FreeRunCSES.setDescription('The counter associated with the number of C bit Severly Errored Seconds.')
mibBuilder.exportSymbols("PDN-DS3EXT-MIB", devDs3ConfigFramingType=devDs3ConfigFramingType, devDs3TotalEntry=devDs3TotalEntry, devDs3ConfigTimingMarkerCode=devDs3ConfigTimingMarkerCode, devDs3FreeRunPSEFS=devDs3FreeRunPSEFS, devDs3IntervalES=devDs3IntervalES, devDs3CurrentEntry=devDs3CurrentEntry, devDs3CurrentSES=devDs3CurrentSES, devDs3FreeRunLES=devDs3FreeRunLES, devDs3FreeRunTable=devDs3FreeRunTable, devDs3FreeRunPCV=devDs3FreeRunPCV, devDs3TotalPlcpSEFS=devDs3TotalPlcpSEFS, devDs3FreeRunPES=devDs3FreeRunPES, devDs3ConfigIfIndex=devDs3ConfigIfIndex, devDs3CurrentTable=devDs3CurrentTable, devDs3TotalSES=devDs3TotalSES, devDs3CurrentES=devDs3CurrentES, devDs3IntervalTable=devDs3IntervalTable, devDs3FreeRunEntry=devDs3FreeRunEntry, devDs3FreeRunUAS=devDs3FreeRunUAS, devDs3TotalTable=devDs3TotalTable, devDs3FreeRunCSES=devDs3FreeRunCSES, devDs3TotalEB=devDs3TotalEB, devDs3IntervalSES=devDs3IntervalSES, devDs3IntervalPlcpSEFS=devDs3IntervalPlcpSEFS, devDs3FreeRunCCV=devDs3FreeRunCCV, devDs3FreeRunCES=devDs3FreeRunCES, devDs3CurrentEB=devDs3CurrentEB, pdnDs3MIB=pdnDs3MIB, devDs3ConfigEntry=devDs3ConfigEntry, PYSNMP_MODULE_ID=pdnDs3MIB, devDs3CurrentPlcpSEFS=devDs3CurrentPlcpSEFS, devDs3ConfigIgnoreCbit=devDs3ConfigIgnoreCbit, devDs3FreeRunPSES=devDs3FreeRunPSES, devDs3Objects=devDs3Objects, devDs3IntervalEB=devDs3IntervalEB, devDs3IntervalEntry=devDs3IntervalEntry, devDs3FreeRunLCV=devDs3FreeRunLCV, devDs3TotalES=devDs3TotalES, devDs3ConfigTable=devDs3ConfigTable)
