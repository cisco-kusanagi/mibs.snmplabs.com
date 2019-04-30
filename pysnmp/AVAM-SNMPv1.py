#
# PySNMP MIB module AVAM-SNMPv1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAM-SNMPv1
# Produced by pysmi-0.3.4 at Mon Apr 29 17:16:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
DateAndTime, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "DateAndTime")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, NotificationType, iso, MibIdentifier, Bits, Counter64, Gauge32, Counter32, ObjectIdentity, ModuleIdentity, enterprises, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "NotificationType", "iso", "MibIdentifier", "Bits", "Counter64", "Gauge32", "Counter32", "ObjectIdentity", "ModuleIdentity", "enterprises", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
availant = MibIdentifier((1, 3, 6, 1, 4, 1, 5910))
avProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 5910, 1))
avamMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 5910, 1, 3))
avamVisObj = MibIdentifier((1, 3, 6, 1, 4, 1, 5910, 1, 3, 1))
avamNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 5910, 1, 3, 2))
avVersionString = MibScalar((1, 3, 6, 1, 4, 1, 5910, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avVersionString.setStatus('mandatory')
avEventDateTime = MibScalar((1, 3, 6, 1, 4, 1, 5910, 1, 3, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEventDateTime.setStatus('mandatory')
avEventAgent = MibScalar((1, 3, 6, 1, 4, 1, 5910, 1, 3, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEventAgent.setStatus('mandatory')
avHostURL = MibScalar((1, 3, 6, 1, 4, 1, 5910, 1, 3, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avHostURL.setStatus('mandatory')
avEventNotify = NotificationType((1, 3, 6, 1, 4, 1, 5910, 1, 3) + (0,1)).setObjects(("AVAM-SNMPv1", "avEventDateTime"), ("AVAM-SNMPv1", "avEventAgent"), ("AVAM-SNMPv1", "avHostURL"))
mibBuilder.exportSymbols("AVAM-SNMPv1", avamNotify=avamNotify, availant=availant, avamMIB=avamMIB, avHostURL=avHostURL, avVersionString=avVersionString, avEventNotify=avEventNotify, avEventDateTime=avEventDateTime, avamVisObj=avamVisObj, avEventAgent=avEventAgent, avProducts=avProducts)
