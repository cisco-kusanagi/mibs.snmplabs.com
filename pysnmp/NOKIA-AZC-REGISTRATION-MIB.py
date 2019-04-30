#
# PySNMP MIB module NOKIA-AZC-REGISTRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-AZC-REGISTRATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, enterprises, Bits, Counter32, Unsigned32, IpAddress, ObjectIdentity, iso, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "enterprises", "Bits", "Counter32", "Unsigned32", "IpAddress", "ObjectIdentity", "iso", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nokia = MibIdentifier((1, 3, 6, 1, 4, 1, 94))
nokiaProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1))
azcProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32))
azcProductIds = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 1))
unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 1, 1))
p020 = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 1, 2))
mibBuilder.exportSymbols("NOKIA-AZC-REGISTRATION-MIB", p020=p020, nokia=nokia, azcProductIds=azcProductIds, nokiaProducts=nokiaProducts, unknown=unknown, azcProducts=azcProducts)
