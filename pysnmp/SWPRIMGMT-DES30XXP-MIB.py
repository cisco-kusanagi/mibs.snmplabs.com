#
# PySNMP MIB module SWPRIMGMT-DES30XXP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWPRIMGMT-DES30XXP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:24:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Bits, NotificationType, iso, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Unsigned32, ModuleIdentity, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Bits", "NotificationType", "iso", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SWPRIMGMT-DES30XXP-MIB", dlink_des3028Prod=dlink_des3028Prod, des3052p=des3052p, des3028g=des3028g, des30xxSeriesProd=des30xxSeriesProd, des3028p=des3028p, dlink_des30xxproductProd=dlink_des30xxproductProd, dlink_des3052PProd=dlink_des3052PProd, dlink_des3028PProd=dlink_des3028PProd, des3052=des3052, des3028=des3028, dlink_des3052Prod=dlink_des3052Prod)
