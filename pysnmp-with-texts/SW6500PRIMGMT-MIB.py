#
# PySNMP MIB module SW6500PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW6500PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:41:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, MibIdentifier, Bits, Unsigned32, IpAddress, Counter64, TimeTicks, Integer32, NotificationType, ObjectIdentity, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "MibIdentifier", "Bits", "Unsigned32", "IpAddress", "Counter64", "TimeTicks", "Integer32", "NotificationType", "ObjectIdentity", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_Des6500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 78)).setLabel("dlink-Des6500SeriesProd")
dlink_Des6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 78, 1)).setLabel("dlink-Des6500")
des6500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 78))
des6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 78, 1))
mibBuilder.exportSymbols("SW6500PRIMGMT-MIB", dlink_Des6500=dlink_Des6500, des6500=des6500, dlink_Des6500SeriesProd=dlink_Des6500SeriesProd, des6500SeriesProd=des6500SeriesProd)
