#
# PySNMP MIB module SM7-10MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SM7-10MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:59:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, Counter32, Gauge32, Unsigned32, TimeTicks, iso, IpAddress, Bits, Integer32, NotificationType, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "Counter32", "Gauge32", "Unsigned32", "TimeTicks", "iso", "IpAddress", "Bits", "Integer32", "NotificationType", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
symbios = MibIdentifier((1, 3, 6, 1, 4, 1, 1123))
wichita = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 1))
ftcollins = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 2))
cosprings = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 3))
sm7_10 = MibIdentifier((1, 3, 6, 1, 4, 1, 1123, 1, 204)).setLabel("sm7-10")
infoTable = MibTable((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1), )
if mibBuilder.loadTexts: infoTable.setStatus('mandatory')
infoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1), ).setIndexNames((0, "SM7-10MIB", "deviceHostIP"))
if mibBuilder.loadTexts: infoEntry.setStatus('mandatory')
deviceHostIP = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHostIP.setStatus('mandatory')
deviceHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceHostName.setStatus('mandatory')
deviceUserLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceUserLabel.setStatus('mandatory')
deviceErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceErrorCode.setStatus('mandatory')
eventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTime.setStatus('mandatory')
trapDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 69))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDescription.setStatus('mandatory')
componentType = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 59))).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentType.setStatus('mandatory')
componentLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readonly")
if mibBuilder.loadTexts: componentLocation.setStatus('mandatory')
storageArrayCritical = NotificationType((1, 3, 6, 1, 4, 1, 1123, 1, 204) + (0,1)).setObjects(("SM7-10MIB", "deviceHostIP"), ("SM7-10MIB", "deviceHostName"), ("SM7-10MIB", "deviceUserLabel"), ("SM7-10MIB", "deviceErrorCode"), ("SM7-10MIB", "eventTime"), ("SM7-10MIB", "trapDescription"), ("SM7-10MIB", "componentType"), ("SM7-10MIB", "componentLocation"))
mibBuilder.exportSymbols("SM7-10MIB", cosprings=cosprings, sm7_10=sm7_10, infoEntry=infoEntry, storageArrayCritical=storageArrayCritical, deviceHostIP=deviceHostIP, symbios=symbios, deviceHostName=deviceHostName, wichita=wichita, deviceUserLabel=deviceUserLabel, deviceErrorCode=deviceErrorCode, trapDescription=trapDescription, eventTime=eventTime, ftcollins=ftcollins, infoTable=infoTable, componentLocation=componentLocation, componentType=componentType)