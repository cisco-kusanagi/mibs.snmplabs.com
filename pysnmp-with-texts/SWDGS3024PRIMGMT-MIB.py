#
# PySNMP MIB module SWDGS3024PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWDGS3024PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, ModuleIdentity, Integer32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ModuleIdentity", "Integer32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dgs_3024SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68)).setLabel("dgs-3024SeriesProd")
dgs_3024 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68, 1)).setLabel("dgs-3024")
dgs_3024SeriesProd_Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68)).setLabel("dgs-3024SeriesProd-Mgmt")
dgs_3024Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68, 1)).setLabel("dgs-3024Mgmt")
mibBuilder.exportSymbols("SWDGS3024PRIMGMT-MIB", dgs_3024=dgs_3024, dgs_3024SeriesProd=dgs_3024SeriesProd, dgs_3024Mgmt=dgs_3024Mgmt, dgs_3024SeriesProd_Mgmt=dgs_3024SeriesProd_Mgmt)
