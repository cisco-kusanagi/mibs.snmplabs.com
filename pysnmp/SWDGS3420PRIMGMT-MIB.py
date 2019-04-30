#
# PySNMP MIB module SWDGS3420PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWDGS3420PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:28:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, Counter32, Counter64, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Bits, Gauge32, IpAddress, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Counter32", "Counter64", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Bits", "Gauge32", "IpAddress", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SWDGS3420PRIMGMT-MIB", dlink_Dgs3420Prod_Dgs3420_26SC=dlink_Dgs3420Prod_Dgs3420_26SC, dlink_Dgs3420Prod_Dgs3420_28SC=dlink_Dgs3420Prod_Dgs3420_28SC, dlink_Dgs3420Proj_Dgs3420_28TC=dlink_Dgs3420Proj_Dgs3420_28TC, dlink_Dgs3420Proj_Dgs3420_28PC=dlink_Dgs3420Proj_Dgs3420_28PC, dlink_Dgs3420Proj_Dgs3420_52P=dlink_Dgs3420Proj_Dgs3420_52P, dlink_Dgs3420Prod_Dgs3420_52T=dlink_Dgs3420Prod_Dgs3420_52T, dlink_Dgs3420Prod=dlink_Dgs3420Prod, dlink_Dgs3420Prod_Dgs3420_28TC=dlink_Dgs3420Prod_Dgs3420_28TC, dlink_Dgs3420Prod_Dgs3420_52P=dlink_Dgs3420Prod_Dgs3420_52P, dlink_Dgs3420Proj_Dgs3420_26SC=dlink_Dgs3420Proj_Dgs3420_26SC, dlink_Dgs3420Prod_Dgs3420_28PC=dlink_Dgs3420Prod_Dgs3420_28PC, dlink_Dgs3420Proj_Dgs3420_52T=dlink_Dgs3420Proj_Dgs3420_52T, dlink_Dgs3420Proj=dlink_Dgs3420Proj, dlink_Dgs3420Proj_Dgs3420_28SC=dlink_Dgs3420Proj_Dgs3420_28SC)
