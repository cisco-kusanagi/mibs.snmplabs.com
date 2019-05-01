#
# PySNMP MIB module NOKIA-AZC-REGISTRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-AZC-REGISTRATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, enterprises, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Unsigned32, ModuleIdentity, ObjectIdentity, IpAddress, TimeTicks, Bits, Integer32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "TimeTicks", "Bits", "Integer32", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nokia = MibIdentifier((1, 3, 6, 1, 4, 1, 94))
nokiaProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1))
azcProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32))
azcProductIds = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 1))
unknown = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 1, 1))
p020 = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 1, 2))
mibBuilder.exportSymbols("NOKIA-AZC-REGISTRATION-MIB", azcProductIds=azcProductIds, p020=p020, azcProducts=azcProducts, unknown=unknown, nokiaProducts=nokiaProducts, nokia=nokia)
