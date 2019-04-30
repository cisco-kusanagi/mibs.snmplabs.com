#
# PySNMP MIB module Nortel-Magellan-Passport-KurtNetMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-KurtNetMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:18:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, Gauge32, ModuleIdentity, Counter64, IpAddress, Integer32, MibIdentifier, Unsigned32, Bits, NotificationType, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter64", "IpAddress", "Integer32", "MibIdentifier", "Unsigned32", "Bits", "NotificationType", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
kurtNetMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 100))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-KurtNetMIB", kurtNetMIB=kurtNetMIB)
