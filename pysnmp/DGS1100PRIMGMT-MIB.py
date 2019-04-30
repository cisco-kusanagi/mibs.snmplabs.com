#
# PySNMP MIB module DGS1100PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS1100PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:30:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, ObjectIdentity, Counter64, Unsigned32, Gauge32, MibIdentifier, Integer32, ModuleIdentity, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "ObjectIdentity", "Counter64", "Unsigned32", "Gauge32", "MibIdentifier", "Integer32", "ModuleIdentity", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dgs1100SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134))
dgs1100_16 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 3)).setLabel("dgs1100-16")
dgs1100_16ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 4)).setLabel("dgs1100-16ME")
dgs1100_18 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 5)).setLabel("dgs1100-18")
dgs1100_18ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 6)).setLabel("dgs1100-18ME")
dgs1100_24 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 7)).setLabel("dgs1100-24")
dgs1100_24ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 8)).setLabel("dgs1100-24ME")
dgs1100_24P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 9)).setLabel("dgs1100-24P")
dgs1100_24PME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 10)).setLabel("dgs1100-24PME")
dgs1100_26 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 11)).setLabel("dgs1100-26")
dgs1100_26ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 134, 12)).setLabel("dgs1100-26ME")
mibBuilder.exportSymbols("DGS1100PRIMGMT-MIB", dgs1100_18=dgs1100_18, dgs1100_24ME=dgs1100_24ME, dgs1100_24=dgs1100_24, dgs1100_24P=dgs1100_24P, dgs1100SeriesProd=dgs1100SeriesProd, dgs1100_26=dgs1100_26, dgs1100_26ME=dgs1100_26ME, dgs1100_16=dgs1100_16, dgs1100_18ME=dgs1100_18ME, dgs1100_24PME=dgs1100_24PME, dgs1100_16ME=dgs1100_16ME)
