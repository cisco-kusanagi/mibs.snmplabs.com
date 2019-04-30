#
# PySNMP MIB module A3COM0024-EVENT-EXTENSION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0024-EVENT-EXTENSION
# Produced by pysmi-0.3.4 at Mon Apr 29 16:53:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
eventExtensions, = mibBuilder.importSymbols("A3COM0027-RMON-EXTENSIONS", "eventExtensions")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eventIndex, eventDescription, DisplayString = mibBuilder.importSymbols("RMON-MIB", "eventIndex", "eventDescription", "DisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, IpAddress, TimeTicks, NotificationType, iso, MibIdentifier, Unsigned32, ModuleIdentity, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "IpAddress", "TimeTicks", "NotificationType", "iso", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
extEventTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 25, 4, 1), )
if mibBuilder.loadTexts: extEventTable.setStatus('mandatory')
extEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 25, 4, 1, 1), ).setIndexNames((0, "RMON-MIB", "eventIndex"))
if mibBuilder.loadTexts: extEventEntry.setStatus('mandatory')
eventAction = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 4, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventAction.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM0024-EVENT-EXTENSION", eventAction=eventAction, extEventEntry=extEventEntry, extEventTable=extEventTable)
