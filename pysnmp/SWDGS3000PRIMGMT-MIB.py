#
# PySNMP MIB module SWDGS3000PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWDGS3000PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:30:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, TimeTicks, Counter32, NotificationType, Unsigned32, Gauge32, Bits, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "Bits", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Dgs3000Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133)).setLabel("dlink-Dgs3000Prod")
dlink_Dgs3000Prod_DGS3000_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 5)).setLabel("dlink-Dgs3000Prod-DGS3000-28SC")
dlink_Dgs3000Prod_DGS3000_28SCax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 5, 1)).setLabel("dlink-Dgs3000Prod-DGS3000-28SCax")
dlink_Dgs3000Proj = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133)).setLabel("dlink-Dgs3000Proj")
dlink_Dgs3000Proj_DGS3000_28SC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 5)).setLabel("dlink-Dgs3000Proj-DGS3000-28SC")
dlink_Dgs3000Proj_DGS3000_28SCax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1)).setLabel("dlink-Dgs3000Proj-DGS3000-28SCax")
mibBuilder.exportSymbols("SWDGS3000PRIMGMT-MIB", dlink_Dgs3000Prod_DGS3000_28SCax=dlink_Dgs3000Prod_DGS3000_28SCax, dlink_Dgs3000Proj=dlink_Dgs3000Proj, dlink_Dgs3000Prod=dlink_Dgs3000Prod, dlink_Dgs3000Proj_DGS3000_28SC=dlink_Dgs3000Proj_DGS3000_28SC, dlink_Dgs3000Prod_DGS3000_28SC=dlink_Dgs3000Prod_DGS3000_28SC, dlink_Dgs3000Proj_DGS3000_28SCax=dlink_Dgs3000Proj_DGS3000_28SCax)
