#
# PySNMP MIB module SW3200PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3200PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:31:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, iso, Unsigned32, Gauge32, IpAddress, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter64, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "iso", "Unsigned32", "Gauge32", "IpAddress", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter64", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_Dgs3200Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101)).setLabel("dlink-Dgs3200Series")
dgs3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 1))
dgs3216 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 2))
dgs3224 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 3))
dlink_Dgs3200SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101)).setLabel("dlink-Dgs3200SeriesProd")
dgs3200_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 1)).setLabel("dgs3200-Prod")
dgs3216_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 2)).setLabel("dgs3216-Prod")
dgs3224_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 3)).setLabel("dgs3224-Prod")
mibBuilder.exportSymbols("SW3200PRIMGMT-MIB", dgs3224=dgs3224, dgs3216_Prod=dgs3216_Prod, dgs3200_Prod=dgs3200_Prod, dgs3216=dgs3216, dgs3200=dgs3200, dgs3224_Prod=dgs3224_Prod, dlink_Dgs3200SeriesProd=dlink_Dgs3200SeriesProd, dlink_Dgs3200Series=dlink_Dgs3200Series)
