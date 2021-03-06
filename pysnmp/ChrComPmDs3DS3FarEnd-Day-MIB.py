#
# PySNMP MIB module ChrComPmDs3DS3FarEnd-Day-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmDs3DS3FarEnd-Day-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmDs3, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmDs3")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, TimeTicks, Counter64, NotificationType, Bits, ModuleIdentity, Gauge32, IpAddress, iso, MibIdentifier, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "TimeTicks", "Counter64", "NotificationType", "Bits", "ModuleIdentity", "Gauge32", "IpAddress", "iso", "MibIdentifier", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmDs3DS3FarEnd_DayTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14), ).setLabel("chrComPmDs3DS3FarEnd-DayTable")
if mibBuilder.loadTexts: chrComPmDs3DS3FarEnd_DayTable.setStatus('current')
chrComPmDs3DS3FarEnd_DayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1), ).setLabel("chrComPmDs3DS3FarEnd-DayEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmDs3DS3FarEnd-Day-MIB", "chrComPmDs3DayNumber"))
if mibBuilder.loadTexts: chrComPmDs3DS3FarEnd_DayEntry.setStatus('current')
chrComPmDs3DayNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3DayNumber.setStatus('current')
chrComPmDs3SuspectedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuspectedInterval.setStatus('current')
chrComPmDs3ElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ElapsedTime.setStatus('current')
chrComPmDs3SuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SuppressedIntrvls.setStatus('current')
chrComPmDs3CCV = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CCV.setStatus('current')
chrComPmDs3CES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CES.setStatus('current')
chrComPmDs3CSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3CSES.setStatus('current')
chrComPmDs3SAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3SAS.setStatus('current')
chrComPmDs3UASCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3UASCP.setStatus('current')
chrComPmDs3ESPLCP = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmDs3ESPLCP.setStatus('current')
chrComPmDs3ThresholdProfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmDs3ThresholdProfIndex.setStatus('current')
chrComPmDs3ResetPmCountersAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 3, 14, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComPmDs3ResetPmCountersAction.setStatus('current')
mibBuilder.exportSymbols("ChrComPmDs3DS3FarEnd-Day-MIB", chrComPmDs3DS3FarEnd_DayEntry=chrComPmDs3DS3FarEnd_DayEntry, chrComPmDs3SuppressedIntrvls=chrComPmDs3SuppressedIntrvls, chrComPmDs3CCV=chrComPmDs3CCV, chrComPmDs3CES=chrComPmDs3CES, chrComPmDs3ResetPmCountersAction=chrComPmDs3ResetPmCountersAction, chrComPmDs3DayNumber=chrComPmDs3DayNumber, chrComPmDs3UASCP=chrComPmDs3UASCP, chrComPmDs3ThresholdProfIndex=chrComPmDs3ThresholdProfIndex, chrComPmDs3DS3FarEnd_DayTable=chrComPmDs3DS3FarEnd_DayTable, chrComPmDs3ElapsedTime=chrComPmDs3ElapsedTime, chrComPmDs3SuspectedInterval=chrComPmDs3SuspectedInterval, chrComPmDs3CSES=chrComPmDs3CSES, chrComPmDs3ESPLCP=chrComPmDs3ESPLCP, chrComPmDs3SAS=chrComPmDs3SAS)
