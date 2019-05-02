#
# PySNMP MIB module DGS3024PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS3024PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, IpAddress, Counter32, Counter64, Gauge32, ModuleIdentity, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "IpAddress", "Counter32", "Counter64", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dgs_3024SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68)).setLabel("dgs-3024SeriesProd")
dgs_3024 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68, 1)).setLabel("dgs-3024")
dgs_3024SeriesProd_Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68)).setLabel("dgs-3024SeriesProd-Mgmt")
dgs_3024Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68, 1)).setLabel("dgs-3024Mgmt")
mibBuilder.exportSymbols("DGS3024PRIMGMT-MIB", dgs_3024Mgmt=dgs_3024Mgmt, dgs_3024=dgs_3024, dgs_3024SeriesProd=dgs_3024SeriesProd, dgs_3024SeriesProd_Mgmt=dgs_3024SeriesProd_Mgmt)
