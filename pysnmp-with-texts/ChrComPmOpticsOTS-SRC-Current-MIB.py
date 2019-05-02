#
# PySNMP MIB module ChrComPmOpticsOTS-SRC-Current-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmOpticsOTS-SRC-Current-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:35:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmOptics, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmOptics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, Bits, NotificationType, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, MibIdentifier, ObjectIdentity, Counter32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Bits", "NotificationType", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "MibIdentifier", "ObjectIdentity", "Counter32", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmOpticsOTS_SRC_CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4), ).setLabel("chrComPmOpticsOTS-SRC-CurrentTable")
if mibBuilder.loadTexts: chrComPmOpticsOTS_SRC_CurrentTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsOTS_SRC_CurrentTable.setDescription('')
chrComPmOpticsOTS_SRC_CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1), ).setLabel("chrComPmOpticsOTS-SRC-CurrentEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComPmOpticsOTS_SRC_CurrentEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsOTS_SRC_CurrentEntry.setDescription('')
chrComPmOpticsSuspectedIntrvl = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setDescription('a flag marking the validity of the entry data')
chrComPmOpticsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setDescription('measurment duration, in 0.01 seconds')
chrComPmOpticsSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setDescription('invalid for first version. indicates how many all-zero periods have passed.')
chrComPmOpticsORS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsORS.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsORS.setDescription('')
chrComPmOpticsSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSES.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSES.setDescription('')
chrComPmOpticsUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsUAS.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsUAS.setDescription('')
chrComPmOpticsMean = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMean.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMean.setDescription('')
chrComPmOpticsMax = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMax.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMax.setDescription('')
chrComPmOpticsMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMin.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMin.setDescription('')
chrComPmOpticsSD = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSD.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSD.setDescription('')
chrComPmOpticsThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmOpticsThresholdProfIndex.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsThresholdProfIndex.setDescription('')
chrComPmOpticsResetCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 4, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmOpticsResetCountersAction.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsResetCountersAction.setDescription('')
mibBuilder.exportSymbols("ChrComPmOpticsOTS-SRC-Current-MIB", chrComPmOpticsSD=chrComPmOpticsSD, chrComPmOpticsORS=chrComPmOpticsORS, chrComPmOpticsMean=chrComPmOpticsMean, chrComPmOpticsOTS_SRC_CurrentTable=chrComPmOpticsOTS_SRC_CurrentTable, chrComPmOpticsResetCountersAction=chrComPmOpticsResetCountersAction, chrComPmOpticsMin=chrComPmOpticsMin, chrComPmOpticsElapsedTime=chrComPmOpticsElapsedTime, chrComPmOpticsMax=chrComPmOpticsMax, chrComPmOpticsUAS=chrComPmOpticsUAS, chrComPmOpticsThresholdProfIndex=chrComPmOpticsThresholdProfIndex, chrComPmOpticsSuppressedIntrvls=chrComPmOpticsSuppressedIntrvls, chrComPmOpticsSES=chrComPmOpticsSES, chrComPmOpticsOTS_SRC_CurrentEntry=chrComPmOpticsOTS_SRC_CurrentEntry, chrComPmOpticsSuspectedIntrvl=chrComPmOpticsSuspectedIntrvl)
