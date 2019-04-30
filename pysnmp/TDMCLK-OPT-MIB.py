#
# PySNMP MIB module TDMCLK-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TDMCLK-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, ModuleIdentity, ObjectIdentity, TimeTicks, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Unsigned32, NotificationType, Bits, Counter32, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Unsigned32", "NotificationType", "Bits", "Counter32", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500CfgGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatOtherStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2))
cdx6500STTdmClkGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13))
class DisplayString(OctetString):
    pass

cdx6500TdmClkTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 24), )
if mibBuilder.loadTexts: cdx6500TdmClkTable.setStatus('mandatory')
cdx6500TdmClkCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 24, 1), ).setIndexNames((0, "TDMCLK-OPT-MIB", "cdx6500TdmClkEntryNumber"))
if mibBuilder.loadTexts: cdx6500TdmClkCfgEntry.setStatus('mandatory')
cdx6500TdmClkEntryNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 24, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TdmClkEntryNumber.setStatus('mandatory')
cdx6500TdmClkPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 24, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500TdmClkPriority.setStatus('mandatory')
tdmClkStatus = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdmClkStatus.setStatus('optional')
tdmClkRegisteredTDMTable = MibTable((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 2), )
if mibBuilder.loadTexts: tdmClkRegisteredTDMTable.setStatus('mandatory')
tdmClkRegisteredTDMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 2, 1), ).setIndexNames((0, "TDMCLK-OPT-MIB", "cdx6500TdmClkEntryNumber"))
if mibBuilder.loadTexts: tdmClkRegisteredTDMEntry.setStatus('mandatory')
tdmClkRegisteredTDMEntryNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdmClkRegisteredTDMEntryNumber.setStatus('mandatory')
tdmClkRegisteredTDM = MibTableColumn((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 13, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdmClkRegisteredTDM.setStatus('optional')
mibBuilder.exportSymbols("TDMCLK-OPT-MIB", cdx6500Statistics=cdx6500Statistics, cdx6500TdmClkPriority=cdx6500TdmClkPriority, tdmClkStatus=tdmClkStatus, codex=codex, cdx6500CfgGeneralGroup=cdx6500CfgGeneralGroup, tdmClkRegisteredTDMTable=tdmClkRegisteredTDMTable, DisplayString=DisplayString, cdx6500TdmClkTable=cdx6500TdmClkTable, cdx6500StatOtherStatsGroup=cdx6500StatOtherStatsGroup, cdx6500TdmClkEntryNumber=cdx6500TdmClkEntryNumber, cdxProductSpecific=cdxProductSpecific, cdx6500TdmClkCfgEntry=cdx6500TdmClkCfgEntry, cdx6500STTdmClkGroup=cdx6500STTdmClkGroup, cdx6500=cdx6500, cdx6500Configuration=cdx6500Configuration, tdmClkRegisteredTDMEntryNumber=tdmClkRegisteredTDMEntryNumber, tdmClkRegisteredTDMEntry=tdmClkRegisteredTDMEntry, tdmClkRegisteredTDM=tdmClkRegisteredTDM)
