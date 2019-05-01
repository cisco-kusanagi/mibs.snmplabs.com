#
# PySNMP MIB module DGS1100PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS1100PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, IpAddress, Counter64, Integer32, TimeTicks, Unsigned32, Bits, Counter32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "IpAddress", "Counter64", "Integer32", "TimeTicks", "Unsigned32", "Bits", "Counter32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DGS1100PRIMGMT-MIB", dgs1100_16ME=dgs1100_16ME, dgs1100_18ME=dgs1100_18ME, dgs1100_24P=dgs1100_24P, dgs1100_16=dgs1100_16, dgs1100SeriesProd=dgs1100SeriesProd, dgs1100_26ME=dgs1100_26ME, dgs1100_18=dgs1100_18, dgs1100_24PME=dgs1100_24PME, dgs1100_26=dgs1100_26, dgs1100_24=dgs1100_24, dgs1100_24ME=dgs1100_24ME)
