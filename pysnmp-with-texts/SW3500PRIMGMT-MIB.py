#
# PySNMP MIB module SW3500PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3500PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:41:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, ObjectIdentity, NotificationType, Bits, Gauge32, IpAddress, ModuleIdentity, MibIdentifier, iso, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "ObjectIdentity", "NotificationType", "Bits", "Gauge32", "IpAddress", "ModuleIdentity", "MibIdentifier", "iso", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_des3500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 64)).setLabel("dlink-des3500SeriesProd")
dlink_des3526Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 64, 1)).setLabel("dlink-des3526Prod")
dlink_des3550Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 64, 2)).setLabel("dlink-des3550Prod")
des3500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 64))
des3526 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 64, 1))
des3550 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 64, 2))
mibBuilder.exportSymbols("SW3500PRIMGMT-MIB", dlink_des3526Prod=dlink_des3526Prod, des3550=des3550, des3500SeriesProd=des3500SeriesProd, dlink_des3550Prod=dlink_des3550Prod, des3526=des3526, dlink_des3500SeriesProd=dlink_des3500SeriesProd)
