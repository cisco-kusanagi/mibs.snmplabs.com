#
# PySNMP MIB module SWPRIMGMT-DES30XXP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWPRIMGMT-DES30XXP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:40:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Counter32, MibIdentifier, Gauge32, ModuleIdentity, Unsigned32, ObjectIdentity, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter32", "MibIdentifier", "Gauge32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_des30xxproductProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63)).setLabel("dlink-des30xxproductProd")
dlink_des3028Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 6)).setLabel("dlink-des3028Prod")
dlink_des3028PProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 7)).setLabel("dlink-des3028PProd")
dlink_des3052Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 8)).setLabel("dlink-des3052Prod")
dlink_des3052PProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 63, 9)).setLabel("dlink-des3052PProd")
des30xxSeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63))
des3028 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 6))
des3028p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 7))
des3052 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 8))
des3052p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 9))
des3028g = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 63, 11))
mibBuilder.exportSymbols("SWPRIMGMT-DES30XXP-MIB", dlink_des3028PProd=dlink_des3028PProd, des3028p=des3028p, dlink_des30xxproductProd=dlink_des30xxproductProd, des3052=des3052, dlink_des3052Prod=dlink_des3052Prod, des3052p=des3052p, dlink_des3052PProd=dlink_des3052PProd, des3028=des3028, des3028g=des3028g, des30xxSeriesProd=des30xxSeriesProd, dlink_des3028Prod=dlink_des3028Prod)
