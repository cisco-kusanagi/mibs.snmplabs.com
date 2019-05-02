#
# PySNMP MIB module SWDGS3420PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWDGS3420PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:43:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, NotificationType, MibIdentifier, Counter32, ModuleIdentity, ObjectIdentity, Bits, Counter64, Gauge32, TimeTicks, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter64", "Gauge32", "TimeTicks", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_Dgs3420Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119)).setLabel("dlink-Dgs3420Prod")
dlink_Dgs3420Prod_Dgs3420_28TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 1)).setLabel("dlink-Dgs3420Prod-Dgs3420-28TC")
dlink_Dgs3420Prod_Dgs3420_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 2)).setLabel("dlink-Dgs3420Prod-Dgs3420-28SC")
dlink_Dgs3420Prod_Dgs3420_28PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 3)).setLabel("dlink-Dgs3420Prod-Dgs3420-28PC")
dlink_Dgs3420Prod_Dgs3420_52T = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 4)).setLabel("dlink-Dgs3420Prod-Dgs3420-52T")
dlink_Dgs3420Prod_Dgs3420_52P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 5)).setLabel("dlink-Dgs3420Prod-Dgs3420-52P")
dlink_Dgs3420Prod_Dgs3420_26SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 119, 6)).setLabel("dlink-Dgs3420Prod-Dgs3420-26SC")
dlink_Dgs3420Proj = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119)).setLabel("dlink-Dgs3420Proj")
dlink_Dgs3420Proj_Dgs3420_28TC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 1)).setLabel("dlink-Dgs3420Proj-Dgs3420-28TC")
dlink_Dgs3420Proj_Dgs3420_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 2)).setLabel("dlink-Dgs3420Proj-Dgs3420-28SC")
dlink_Dgs3420Proj_Dgs3420_28PC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 3)).setLabel("dlink-Dgs3420Proj-Dgs3420-28PC")
dlink_Dgs3420Proj_Dgs3420_52T = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 4)).setLabel("dlink-Dgs3420Proj-Dgs3420-52T")
dlink_Dgs3420Proj_Dgs3420_52P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 5)).setLabel("dlink-Dgs3420Proj-Dgs3420-52P")
dlink_Dgs3420Proj_Dgs3420_26SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 119, 6)).setLabel("dlink-Dgs3420Proj-Dgs3420-26SC")
mibBuilder.exportSymbols("SWDGS3420PRIMGMT-MIB", dlink_Dgs3420Prod_Dgs3420_52P=dlink_Dgs3420Prod_Dgs3420_52P, dlink_Dgs3420Proj_Dgs3420_52P=dlink_Dgs3420Proj_Dgs3420_52P, dlink_Dgs3420Proj_Dgs3420_26SC=dlink_Dgs3420Proj_Dgs3420_26SC, dlink_Dgs3420Prod_Dgs3420_28PC=dlink_Dgs3420Prod_Dgs3420_28PC, dlink_Dgs3420Prod_Dgs3420_52T=dlink_Dgs3420Prod_Dgs3420_52T, dlink_Dgs3420Prod_Dgs3420_26SC=dlink_Dgs3420Prod_Dgs3420_26SC, dlink_Dgs3420Proj_Dgs3420_28PC=dlink_Dgs3420Proj_Dgs3420_28PC, dlink_Dgs3420Proj_Dgs3420_52T=dlink_Dgs3420Proj_Dgs3420_52T, dlink_Dgs3420Prod=dlink_Dgs3420Prod, dlink_Dgs3420Proj_Dgs3420_28TC=dlink_Dgs3420Proj_Dgs3420_28TC, dlink_Dgs3420Proj=dlink_Dgs3420Proj, dlink_Dgs3420Proj_Dgs3420_28SC=dlink_Dgs3420Proj_Dgs3420_28SC, dlink_Dgs3420Prod_Dgs3420_28SC=dlink_Dgs3420Prod_Dgs3420_28SC, dlink_Dgs3420Prod_Dgs3420_28TC=dlink_Dgs3420Prod_Dgs3420_28TC)
