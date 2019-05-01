#
# PySNMP MIB module SWPRIMGMT-DES1228ME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWPRIMGMT-DES1228ME-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:39:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, ModuleIdentity, ObjectIdentity, Counter64, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Integer32, Gauge32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Counter64", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Integer32", "Gauge32", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_des1228MEproductProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116)).setLabel("dlink-des1228MEproductProd")
dlink_des1228MEProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116, 1)).setLabel("dlink-des1228MEProd")
dlink_des1228MEv2Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116, 2)).setLabel("dlink-des1228MEv2Prod")
des1228MESeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116))
des1228ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116, 1))
des1228MEv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116, 2))
mibBuilder.exportSymbols("SWPRIMGMT-DES1228ME-MIB", dlink_des1228MEproductProd=dlink_des1228MEproductProd, des1228ME=des1228ME, dlink_des1228MEv2Prod=dlink_des1228MEv2Prod, des1228MESeriesProd=des1228MESeriesProd, des1228MEv2=des1228MEv2, dlink_des1228MEProd=dlink_des1228MEProd)
