#
# PySNMP MIB module SWDES3528-52PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWDES3528-52PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:41:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, MibIdentifier, Gauge32, Unsigned32, Bits, IpAddress, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "MibIdentifier", "Gauge32", "Unsigned32", "Bits", "IpAddress", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Des3500Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105)).setLabel("dlink-Des3500Series")
des3528 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 1))
des3528p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 2))
des3552 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 3))
des3552p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 4))
des3528dc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 5))
dlink_Des3500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105)).setLabel("dlink-Des3500SeriesProd")
des3528Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 1))
des3528pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 2))
des3552Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 3))
des3552pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 4))
des3528dcProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 5))
mibBuilder.exportSymbols("SWDES3528-52PRIMGMT-MIB", des3552p=des3552p, dlink_Des3500SeriesProd=dlink_Des3500SeriesProd, des3552pProd=des3552pProd, des3528p=des3528p, des3528dc=des3528dc, des3528pProd=des3528pProd, des3528Prod=des3528Prod, des3552Prod=des3552Prod, des3528dcProd=des3528dcProd, des3552=des3552, des3528=des3528, dlink_Des3500Series=dlink_Des3500Series)
