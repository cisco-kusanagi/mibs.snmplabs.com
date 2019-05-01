#
# PySNMP MIB module SWPRIMGMT-DGS3000-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWPRIMGMT-DGS3000-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, Integer32, Unsigned32, ModuleIdentity, ObjectIdentity, Counter32, Counter64, Gauge32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Integer32", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Counter32", "Counter64", "Gauge32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_dgs3000SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133)).setLabel("dlink-dgs3000SeriesProd")
dgs_3000_10tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 1)).setLabel("dgs-3000-10tc")
dgs_3000_26tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 2)).setLabel("dgs-3000-26tc")
dgs_3000_24tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 4)).setLabel("dgs-3000-24tc")
dgs_3000_10_tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 1, 1)).setLabel("dgs-3000-10-tc")
dgs_3000_26_tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 2, 1)).setLabel("dgs-3000-26-tc")
dgs_3000_24_tcax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 133, 4, 1)).setLabel("dgs-3000-24-tcax")
dgs3000SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133))
dgs3000_10tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 1)).setLabel("dgs3000-10tc")
dgs3000_26tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 2)).setLabel("dgs3000-26tc")
dgs3000_24tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 4)).setLabel("dgs3000-24tc")
dgs3000_10_tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 1, 1)).setLabel("dgs3000-10-tc")
dgs3000_26_tc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 2, 1)).setLabel("dgs3000-26-tc")
dgs3000_24_tcax = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 133, 4, 1)).setLabel("dgs3000-24-tcax")
mibBuilder.exportSymbols("SWPRIMGMT-DGS3000-MIB", dgs_3000_24_tcax=dgs_3000_24_tcax, dgs_3000_24tc=dgs_3000_24tc, dgs3000_26tc=dgs3000_26tc, dlink_dgs3000SeriesProd=dlink_dgs3000SeriesProd, dgs_3000_26tc=dgs_3000_26tc, dgs_3000_26_tc=dgs_3000_26_tc, dgs3000_24tc=dgs3000_24tc, dgs3000_26_tc=dgs3000_26_tc, dgs3000_10_tc=dgs3000_10_tc, dgs3000_24_tcax=dgs3000_24_tcax, dgs3000_10tc=dgs3000_10tc, dgs_3000_10_tc=dgs_3000_10_tc, dgs3000SeriesProd=dgs3000SeriesProd, dgs_3000_10tc=dgs_3000_10tc)
