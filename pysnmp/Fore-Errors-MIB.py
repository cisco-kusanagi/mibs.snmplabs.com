#
# PySNMP MIB module Fore-Errors-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Errors-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
snmpErrors, = mibBuilder.importSymbols("Fore-Common-MIB", "snmpErrors")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, IpAddress, Bits, MibIdentifier, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "MibIdentifier", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
errorLogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 2, 3))
if mibBuilder.loadTexts: errorLogMib.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: errorLogMib.setOrganization('FORE')
lastLogMessage = MibScalar((1, 3, 6, 1, 4, 1, 326, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastLogMessage.setStatus('current')
lastLogMessageOID = MibScalar((1, 3, 6, 1, 4, 1, 326, 1, 2, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastLogMessageOID.setStatus('current')
mibBuilder.exportSymbols("Fore-Errors-MIB", lastLogMessageOID=lastLogMessageOID, PYSNMP_MODULE_ID=errorLogMib, lastLogMessage=lastLogMessage, errorLogMib=errorLogMib)
