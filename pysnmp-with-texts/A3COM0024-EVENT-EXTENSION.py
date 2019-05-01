#
# PySNMP MIB module A3COM0024-EVENT-EXTENSION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0024-EVENT-EXTENSION
# Produced by pysmi-0.3.4 at Wed May  1 11:08:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
eventExtensions, = mibBuilder.importSymbols("A3COM0027-RMON-EXTENSIONS", "eventExtensions")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
DisplayString, eventIndex, eventDescription = mibBuilder.importSymbols("RMON-MIB", "DisplayString", "eventIndex", "eventDescription")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, Bits, ModuleIdentity, ObjectIdentity, Gauge32, Counter32, iso, IpAddress, NotificationType, TimeTicks, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Bits", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Counter32", "iso", "IpAddress", "NotificationType", "TimeTicks", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extEventTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 25, 4, 1), )
if mibBuilder.loadTexts: extEventTable.setStatus('mandatory')
if mibBuilder.loadTexts: extEventTable.setDescription('A list of events to be generated.')
extEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 25, 4, 1, 1), ).setIndexNames((0, "RMON-MIB", "eventIndex"))
if mibBuilder.loadTexts: extEventEntry.setStatus('mandatory')
if mibBuilder.loadTexts: extEventEntry.setDescription('A set of parameters that describe an event to be generated when certain conditions are met.')
eventAction = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 4, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventAction.setStatus('mandatory')
if mibBuilder.loadTexts: eventAction.setDescription('')
mibBuilder.exportSymbols("A3COM0024-EVENT-EXTENSION", extEventTable=extEventTable, eventAction=eventAction, extEventEntry=extEventEntry)
