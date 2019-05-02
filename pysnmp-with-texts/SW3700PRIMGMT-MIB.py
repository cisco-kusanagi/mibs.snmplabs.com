#
# PySNMP MIB module SW3700PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3700PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:44:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Counter64, NotificationType, iso, TimeTicks, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Counter64", "NotificationType", "iso", "TimeTicks", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Dgs3700Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102)).setLabel("dlink-Dgs3700Series")
dgs3700 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1))
dgs3712 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1))
dgs3712g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 2))
dlink_Dgs3700SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 102)).setLabel("dlink-Dgs3700SeriesProd")
dgs3712Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 102, 1))
dgs3712pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 102, 2))
mibBuilder.exportSymbols("SW3700PRIMGMT-MIB", dlink_Dgs3700SeriesProd=dlink_Dgs3700SeriesProd, dgs3712Prod=dgs3712Prod, dgs3712g=dgs3712g, dgs3712pProd=dgs3712pProd, dgs3712=dgs3712, dgs3700=dgs3700, dlink_Dgs3700Series=dlink_Dgs3700Series)
