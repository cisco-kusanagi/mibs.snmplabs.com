#
# PySNMP MIB module SWDGS3024PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWDGS3024PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:30:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, TimeTicks, Counter64, ObjectIdentity, Gauge32, NotificationType, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "TimeTicks", "Counter64", "ObjectIdentity", "Gauge32", "NotificationType", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dgs_3024SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68)).setLabel("dgs-3024SeriesProd")
dgs_3024 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 68, 1)).setLabel("dgs-3024")
dgs_3024SeriesProd_Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68)).setLabel("dgs-3024SeriesProd-Mgmt")
dgs_3024Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 68, 1)).setLabel("dgs-3024Mgmt")
mibBuilder.exportSymbols("SWDGS3024PRIMGMT-MIB", dgs_3024SeriesProd=dgs_3024SeriesProd, dgs_3024=dgs_3024, dgs_3024SeriesProd_Mgmt=dgs_3024SeriesProd_Mgmt, dgs_3024Mgmt=dgs_3024Mgmt)
