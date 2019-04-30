#
# PySNMP MIB module CTRON-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:14:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, ModuleIdentity, Gauge32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, iso, Unsigned32, TimeTicks, Counter32, Counter64, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "ModuleIdentity", "Gauge32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "iso", "Unsigned32", "TimeTicks", "Counter32", "Counter64", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
ctronProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 10))
ssr3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 10, 1))
ssr32000 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 10, 2))
mibBuilder.exportSymbols("CTRON-PRODUCTS-MIB", ssr3000=ssr3000, ssr32000=ssr32000, ctronProducts=ctronProducts, cabletron=cabletron)
