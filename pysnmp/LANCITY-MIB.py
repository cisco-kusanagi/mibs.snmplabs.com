#
# PySNMP MIB module LANCITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANCITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:54:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, IpAddress, MibIdentifier, TimeTicks, enterprises, ModuleIdentity, ObjectIdentity, Unsigned32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "IpAddress", "MibIdentifier", "TimeTicks", "enterprises", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lancity = ModuleIdentity((1, 3, 6, 1, 4, 1, 482))
if mibBuilder.loadTexts: lancity.setLastUpdated('9709061024Z')
if mibBuilder.loadTexts: lancity.setOrganization('Bay Networks Broadband Technologies Division')
mibBuilder.exportSymbols("LANCITY-MIB", lancity=lancity, PYSNMP_MODULE_ID=lancity)
