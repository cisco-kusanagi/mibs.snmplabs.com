#
# PySNMP MIB module SWPRIMGMT-DES1228ME-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWPRIMGMT-DES1228ME-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:24:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, iso, NotificationType, TimeTicks, Counter64, Gauge32, Unsigned32, IpAddress, Bits, ModuleIdentity, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "NotificationType", "TimeTicks", "Counter64", "Gauge32", "Unsigned32", "IpAddress", "Bits", "ModuleIdentity", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_des1228MEproductProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116)).setLabel("dlink-des1228MEproductProd")
dlink_des1228MEProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116, 1)).setLabel("dlink-des1228MEProd")
dlink_des1228MEv2Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 116, 2)).setLabel("dlink-des1228MEv2Prod")
des1228MESeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116))
des1228ME = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116, 1))
des1228MEv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 116, 2))
mibBuilder.exportSymbols("SWPRIMGMT-DES1228ME-MIB", des1228MEv2=des1228MEv2, dlink_des1228MEProd=dlink_des1228MEProd, des1228MESeriesProd=des1228MESeriesProd, dlink_des1228MEproductProd=dlink_des1228MEproductProd, dlink_des1228MEv2Prod=dlink_des1228MEv2Prod, des1228ME=des1228ME)
