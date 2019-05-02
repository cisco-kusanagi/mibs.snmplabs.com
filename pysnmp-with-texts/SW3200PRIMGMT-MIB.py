#
# PySNMP MIB module SW3200PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3200PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:46:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, IpAddress, TimeTicks, MibIdentifier, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "IpAddress", "TimeTicks", "MibIdentifier", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Dgs3200Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101)).setLabel("dlink-Dgs3200Series")
dgs3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 1))
dgs3216 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 2))
dgs3224 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 101, 3))
dlink_Dgs3200SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101)).setLabel("dlink-Dgs3200SeriesProd")
dgs3200_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 1)).setLabel("dgs3200-Prod")
dgs3216_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 2)).setLabel("dgs3216-Prod")
dgs3224_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 101, 3)).setLabel("dgs3224-Prod")
mibBuilder.exportSymbols("SW3200PRIMGMT-MIB", dlink_Dgs3200SeriesProd=dlink_Dgs3200SeriesProd, dlink_Dgs3200Series=dlink_Dgs3200Series, dgs3224=dgs3224, dgs3224_Prod=dgs3224_Prod, dgs3216_Prod=dgs3216_Prod, dgs3200=dgs3200, dgs3216=dgs3216, dgs3200_Prod=dgs3200_Prod)
