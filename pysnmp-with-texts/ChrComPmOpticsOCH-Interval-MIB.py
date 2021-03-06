#
# PySNMP MIB module ChrComPmOpticsOCH-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmOpticsOCH-Interval-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:35:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmOptics, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmOptics")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, Counter32, TimeTicks, Counter64, Unsigned32, Bits, MibIdentifier, ModuleIdentity, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Counter32", "TimeTicks", "Counter64", "Unsigned32", "Bits", "MibIdentifier", "ModuleIdentity", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComPmOpticsOCH_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14), ).setLabel("chrComPmOpticsOCH-IntervalTable")
if mibBuilder.loadTexts: chrComPmOpticsOCH_IntervalTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsOCH_IntervalTable.setDescription('')
chrComPmOpticsOCH_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1), ).setLabel("chrComPmOpticsOCH-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmOpticsOCH-Interval-MIB", "chrComPmOpticsIntervalNumber"))
if mibBuilder.loadTexts: chrComPmOpticsOCH_IntervalEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsOCH_IntervalEntry.setDescription('')
chrComPmOpticsIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsIntervalNumber.setDescription('')
chrComPmOpticsSuspectedIntrvl = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setDescription('a flag marking the validity of the entry data')
chrComPmOpticsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setDescription('measurment duration, in 0.01 seconds')
chrComPmOpticsSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setDescription('invalid for first version. indicates how many all-zero periods have passed.')
chrComPmOpticsORS_R = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setLabel("chrComPmOpticsORS-R").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsORS_R.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsORS_R.setDescription('')
chrComPmOpticsSES_R = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setLabel("chrComPmOpticsSES-R").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSES_R.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSES_R.setDescription('')
chrComPmOpticsUAS_R = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setLabel("chrComPmOpticsUAS-R").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsUAS_R.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsUAS_R.setDescription('')
chrComPmOpticsORS_S = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setLabel("chrComPmOpticsORS-S").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsORS_S.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsORS_S.setDescription('')
chrComPmOpticsSES_S = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setLabel("chrComPmOpticsSES-S").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSES_S.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSES_S.setDescription('')
chrComPmOpticsUAS_S = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setLabel("chrComPmOpticsUAS-S").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsUAS_S.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsUAS_S.setDescription('')
chrComPmOpticsMean_R = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setLabel("chrComPmOpticsMean-R").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMean_R.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMean_R.setDescription('')
chrComPmOpticsMax_R = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setLabel("chrComPmOpticsMax-R").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMax_R.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMax_R.setDescription('')
chrComPmOpticsMin_R = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setLabel("chrComPmOpticsMin-R").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMin_R.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMin_R.setDescription('')
chrComPmOpticsSD_R = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setLabel("chrComPmOpticsSD-R").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSD_R.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSD_R.setDescription('')
chrComPmOpticsMean_S = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setLabel("chrComPmOpticsMean-S").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMean_S.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMean_S.setDescription('')
chrComPmOpticsMax_S = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setLabel("chrComPmOpticsMax-S").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMax_S.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMax_S.setDescription('')
chrComPmOpticsMin_S = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 17), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setLabel("chrComPmOpticsMin-S").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMin_S.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMin_S.setDescription('')
chrComPmOpticsSD_S = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 14, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setLabel("chrComPmOpticsSD-S").setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSD_S.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSD_S.setDescription('')
mibBuilder.exportSymbols("ChrComPmOpticsOCH-Interval-MIB", chrComPmOpticsSuspectedIntrvl=chrComPmOpticsSuspectedIntrvl, chrComPmOpticsMin_R=chrComPmOpticsMin_R, chrComPmOpticsSuppressedIntrvls=chrComPmOpticsSuppressedIntrvls, chrComPmOpticsOCH_IntervalEntry=chrComPmOpticsOCH_IntervalEntry, chrComPmOpticsIntervalNumber=chrComPmOpticsIntervalNumber, chrComPmOpticsMin_S=chrComPmOpticsMin_S, chrComPmOpticsMax_R=chrComPmOpticsMax_R, chrComPmOpticsUAS_R=chrComPmOpticsUAS_R, chrComPmOpticsORS_S=chrComPmOpticsORS_S, chrComPmOpticsORS_R=chrComPmOpticsORS_R, chrComPmOpticsSES_R=chrComPmOpticsSES_R, chrComPmOpticsSD_R=chrComPmOpticsSD_R, chrComPmOpticsOCH_IntervalTable=chrComPmOpticsOCH_IntervalTable, chrComPmOpticsElapsedTime=chrComPmOpticsElapsedTime, chrComPmOpticsSES_S=chrComPmOpticsSES_S, chrComPmOpticsUAS_S=chrComPmOpticsUAS_S, chrComPmOpticsMean_R=chrComPmOpticsMean_R, chrComPmOpticsMax_S=chrComPmOpticsMax_S, chrComPmOpticsSD_S=chrComPmOpticsSD_S, chrComPmOpticsMean_S=chrComPmOpticsMean_S)
