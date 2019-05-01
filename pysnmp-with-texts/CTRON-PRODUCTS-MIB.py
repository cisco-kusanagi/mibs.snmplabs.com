#
# PySNMP MIB module CTRON-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:30:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, TimeTicks, iso, enterprises, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Counter64, ObjectIdentity, NotificationType, Bits, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "TimeTicks", "iso", "enterprises", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Counter64", "ObjectIdentity", "NotificationType", "Bits", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
ctronProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 10))
ssr3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 10, 1))
ssr32000 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 10, 2))
mibBuilder.exportSymbols("CTRON-PRODUCTS-MIB", ssr32000=ssr32000, ssr3000=ssr3000, ctronProducts=ctronProducts, cabletron=cabletron)
