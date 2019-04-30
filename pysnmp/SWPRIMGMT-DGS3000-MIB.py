#
# PySNMP MIB module SWPRIMGMT-DGS3000-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWPRIMGMT-DGS3000-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:30:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, NotificationType, Gauge32, ModuleIdentity, TimeTicks, Counter32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks", "Counter32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Integer32", "ObjectIdentity")
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
mibBuilder.exportSymbols("SWPRIMGMT-DGS3000-MIB", dgs3000_10_tc=dgs3000_10_tc, dgs_3000_24tc=dgs_3000_24tc, dlink_dgs3000SeriesProd=dlink_dgs3000SeriesProd, dgs3000_24_tcax=dgs3000_24_tcax, dgs_3000_10tc=dgs_3000_10tc, dgs3000_26_tc=dgs3000_26_tc, dgs3000SeriesProd=dgs3000SeriesProd, dgs_3000_10_tc=dgs_3000_10_tc, dgs_3000_26tc=dgs_3000_26tc, dgs3000_24tc=dgs3000_24tc, dgs3000_10tc=dgs3000_10tc, dgs_3000_24_tcax=dgs_3000_24_tcax, dgs_3000_26_tc=dgs_3000_26_tc, dgs3000_26tc=dgs3000_26tc)
