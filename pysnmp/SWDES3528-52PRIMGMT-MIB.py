#
# PySNMP MIB module SWDES3528-52PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWDES3528-52PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:25:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, IpAddress, Integer32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, NotificationType, Unsigned32, TimeTicks, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "IpAddress", "Integer32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "NotificationType", "Unsigned32", "TimeTicks", "iso", "MibIdentifier")
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
mibBuilder.exportSymbols("SWDES3528-52PRIMGMT-MIB", dlink_Des3500SeriesProd=dlink_Des3500SeriesProd, des3528=des3528, des3528dcProd=des3528dcProd, des3552=des3552, des3528Prod=des3528Prod, des3552p=des3552p, dlink_Des3500Series=dlink_Des3500Series, des3528pProd=des3528pProd, des3528dc=des3528dc, des3528p=des3528p, des3552pProd=des3552pProd, des3552Prod=des3552Prod)
