#
# PySNMP MIB module SW3528PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3528PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:25:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, NotificationType, Gauge32, ModuleIdentity, ObjectIdentity, IpAddress, iso, Counter32, MibIdentifier, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "NotificationType", "Gauge32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "iso", "Counter32", "MibIdentifier", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink_Des3528Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105)).setLabel("dlink-Des3528Series")
des3528 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 1))
des3528p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 2))
des3552 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 3))
des3552p = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 4))
des3528dc = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 105, 5))
dlink_Des3528SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105)).setLabel("dlink-Des3528SeriesProd")
des3528Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 1))
des3528pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 2))
des3552Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 3))
des3552pProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 4))
des3528dcProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 105, 5))
mibBuilder.exportSymbols("SW3528PRIMGMT-MIB", des3528pProd=des3528pProd, des3528p=des3528p, des3528dc=des3528dc, des3528Prod=des3528Prod, des3552p=des3552p, des3552=des3552, des3552Prod=des3552Prod, des3528dcProd=des3528dcProd, dlink_Des3528Series=dlink_Des3528Series, des3528=des3528, des3552pProd=des3552pProd, dlink_Des3528SeriesProd=dlink_Des3528SeriesProd)
