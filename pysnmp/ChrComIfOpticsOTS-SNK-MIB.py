#
# PySNMP MIB module ChrComIfOpticsOTS-SNK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComIfOpticsOTS-SNK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
chrComIfOptics, = mibBuilder.importSymbols("Chromatis-MIB", "chrComIfOptics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, IpAddress, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter32, Bits, Counter64, ModuleIdentity, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "IpAddress", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter32", "Bits", "Counter64", "ModuleIdentity", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComIfOpticsOTS_SNKTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1), ).setLabel("chrComIfOpticsOTS-SNKTable")
if mibBuilder.loadTexts: chrComIfOpticsOTS_SNKTable.setStatus('current')
chrComIfOpticsOTS_SNKEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1), ).setLabel("chrComIfOpticsOTS-SNKEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComIfOpticsOTS_SNKEntry.setStatus('current')
chrComIfOpticsOtsSnkInPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-501, 300))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComIfOpticsOtsSnkInPower.setStatus('current')
chrComIfOpticsOtsSnkLOOPThr = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-501, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComIfOpticsOtsSnkLOOPThr.setStatus('current')
chrComIfOpticsAlarmVector = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComIfOpticsAlarmVector.setStatus('current')
chrComIfOpticsAlarmSeverityProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComIfOpticsAlarmSeverityProfileIndex.setStatus('current')
mibBuilder.exportSymbols("ChrComIfOpticsOTS-SNK-MIB", chrComIfOpticsOtsSnkInPower=chrComIfOpticsOtsSnkInPower, chrComIfOpticsOtsSnkLOOPThr=chrComIfOpticsOtsSnkLOOPThr, chrComIfOpticsOTS_SNKTable=chrComIfOpticsOTS_SNKTable, chrComIfOpticsOTS_SNKEntry=chrComIfOpticsOTS_SNKEntry, chrComIfOpticsAlarmVector=chrComIfOpticsAlarmVector, chrComIfOpticsAlarmSeverityProfileIndex=chrComIfOpticsAlarmSeverityProfileIndex)
