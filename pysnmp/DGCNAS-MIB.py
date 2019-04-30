#
# PySNMP MIB module DGCNAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGCNAS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Gauge32, enterprises, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, MibIdentifier, IpAddress, iso, Unsigned32, TimeTicks, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Gauge32", "enterprises", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "MibIdentifier", "IpAddress", "iso", "Unsigned32", "TimeTicks", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dataGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 106))
dgEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 106, 3))
dgNasEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 106, 3, 3))
dgNasEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 106, 3, 3, 1))
dgNasEventLogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 0), ("debug", 1), ("info", 2), ("warning", 3), ("error", 4), ("critical", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dgNasEventLogSeverity.setStatus('mandatory')
dgNasEventLogSource = MibScalar((1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dgNasEventLogSource.setStatus('mandatory')
dgNasEventLogDescription = MibScalar((1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dgNasEventLogDescription.setStatus('mandatory')
dgNasEventLogSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dgNasEventLogSerialNumber.setStatus('mandatory')
dgNasEventLogSystemType = MibScalar((1, 3, 6, 1, 4, 1, 106, 3, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dgNasEventLogSystemType.setStatus('mandatory')
dgTrapNasEventLogNotification = NotificationType((1, 3, 6, 1, 4, 1, 106) + (0,4)).setObjects(("DGCNAS-MIB", "dgNasEventLogSeverity"), ("DGCNAS-MIB", "dgNasEventLogSource"), ("DGCNAS-MIB", "dgNasEventLogDescription"), ("DGCNAS-MIB", "dgNasEventLogSerialNumber"), ("DGCNAS-MIB", "dgNasEventLogSystemType"))
mibBuilder.exportSymbols("DGCNAS-MIB", dgNasEventLog=dgNasEventLog, dgNasEvent=dgNasEvent, dataGeneral=dataGeneral, dgTrapNasEventLogNotification=dgTrapNasEventLogNotification, dgNasEventLogSystemType=dgNasEventLogSystemType, dgNasEventLogSeverity=dgNasEventLogSeverity, dgNasEventLogSource=dgNasEventLogSource, dgNasEventLogSerialNumber=dgNasEventLogSerialNumber, dgEvent=dgEvent, dgNasEventLogDescription=dgNasEventLogDescription)
