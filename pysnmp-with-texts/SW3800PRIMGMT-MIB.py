#
# PySNMP MIB module SW3800PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3800PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:41:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, Integer32, Unsigned32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, NotificationType, Counter32, ObjectIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "NotificationType", "Counter32", "ObjectIdentity", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_des3800SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69)).setLabel("dlink-des3800SeriesProd")
dlink_des3828Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 1)).setLabel("dlink-des3828Prod")
dlink_des3828DCProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 2)).setLabel("dlink-des3828DCProd")
dlink_des3828PProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 3)).setLabel("dlink-des3828PProd")
dlink_des3852Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 4)).setLabel("dlink-des3852Prod")
dlink_des3852PProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 69, 5)).setLabel("dlink-des3852PProd")
des3800SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69))
des3828 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 1))
des3828DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 2))
des3828P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 3))
des3852 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 4))
des3852P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 69, 5))
mibBuilder.exportSymbols("SW3800PRIMGMT-MIB", des3800SeriesProd=des3800SeriesProd, dlink_des3852Prod=dlink_des3852Prod, dlink_des3828PProd=dlink_des3828PProd, dlink_des3800SeriesProd=dlink_des3800SeriesProd, des3828DC=des3828DC, dlink_des3852PProd=dlink_des3852PProd, des3828P=des3828P, des3828=des3828, dlink_des3828Prod=dlink_des3828Prod, dlink_des3828DCProd=dlink_des3828DCProd, des3852=des3852, des3852P=des3852P)
