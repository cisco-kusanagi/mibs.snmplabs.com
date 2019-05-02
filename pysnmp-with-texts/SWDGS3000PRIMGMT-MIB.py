#
# PySNMP MIB module SWDGS3000PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWDGS3000PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, TimeTicks, MibIdentifier, Bits, iso, Gauge32, Unsigned32, Counter32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "TimeTicks", "MibIdentifier", "Bits", "iso", "Gauge32", "Unsigned32", "Counter32", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_Dgs3000Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133)).setLabel("dlink-Dgs3000Prod")
dlink_Dgs3000Prod_DGS3000_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 5)).setLabel("dlink-Dgs3000Prod-DGS3000-28SC")
dlink_Dgs3000Prod_DGS3000_28SCax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 5, 1)).setLabel("dlink-Dgs3000Prod-DGS3000-28SCax")
dlink_Dgs3000Proj = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133)).setLabel("dlink-Dgs3000Proj")
dlink_Dgs3000Proj_DGS3000_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 5)).setLabel("dlink-Dgs3000Proj-DGS3000-28SC")
dlink_Dgs3000Proj_DGS3000_28SCax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1)).setLabel("dlink-Dgs3000Proj-DGS3000-28SCax")
mibBuilder.exportSymbols("SWDGS3000PRIMGMT-MIB", dlink_Dgs3000Prod_DGS3000_28SC=dlink_Dgs3000Prod_DGS3000_28SC, dlink_Dgs3000Prod=dlink_Dgs3000Prod, dlink_Dgs3000Proj_DGS3000_28SCax=dlink_Dgs3000Proj_DGS3000_28SCax, dlink_Dgs3000Proj=dlink_Dgs3000Proj, dlink_Dgs3000Prod_DGS3000_28SCax=dlink_Dgs3000Prod_DGS3000_28SCax, dlink_Dgs3000Proj_DGS3000_28SC=dlink_Dgs3000Proj_DGS3000_28SC)
