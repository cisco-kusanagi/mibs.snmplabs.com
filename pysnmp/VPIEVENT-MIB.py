#
# PySNMP MIB module VPIEVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPIEVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, ObjectIdentity, MibIdentifier, Integer32, iso, NotificationType, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, IpAddress, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32", "iso", "NotificationType", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "IpAddress", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
software, voiceprint = mibBuilder.importSymbols("VPI-MIB", "software", "voiceprint")
eventcenter = MibIdentifier((1, 3, 6, 1, 4, 1, 15191, 1, 1))
applicationId = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationId.setStatus('mandatory')
applicationName = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: applicationName.setStatus('mandatory')
processName = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: processName.setStatus('mandatory')
logEventType = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logEventType.setStatus('mandatory')
logEventName = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logEventName.setStatus('mandatory')
logEventMessage = MibScalar((1, 3, 6, 1, 4, 1, 15191, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: logEventMessage.setStatus('mandatory')
eventNotif = NotificationType((1, 3, 6, 1, 4, 1, 15191) + (0,0)).setObjects(("VPIEVENT-MIB", "applicationId"), ("VPIEVENT-MIB", "applicationName"), ("VPIEVENT-MIB", "processName"), ("VPIEVENT-MIB", "logEventType"), ("VPIEVENT-MIB", "logEventName"), ("VPIEVENT-MIB", "logEventMessage"))
mibBuilder.exportSymbols("VPIEVENT-MIB", logEventType=logEventType, eventNotif=eventNotif, logEventMessage=logEventMessage, eventcenter=eventcenter, applicationName=applicationName, applicationId=applicationId, processName=processName, logEventName=logEventName)
