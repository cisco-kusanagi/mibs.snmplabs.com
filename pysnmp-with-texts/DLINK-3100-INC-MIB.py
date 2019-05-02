#
# PySNMP MIB module DLINK-3100-INC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-INC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:47:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, Bits, ObjectIdentity, IpAddress, ModuleIdentity, Unsigned32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, enterprises, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Bits", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Unsigned32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "enterprises", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 171))
dlink_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10)).setLabel("dlink-products")
dlink_Dgs3100SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94)).setLabel("dlink-Dgs3100SeriesProd")
dgs3124_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 1)).setLabel("dgs3124-Prod")
dgs3124p_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 2)).setLabel("dgs3124p-Prod")
dgs3148_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 3)).setLabel("dgs3148-Prod")
dgs3148p_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 4)).setLabel("dgs3148p-Prod")
dgs3124tg_Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 5)).setLabel("dgs3124tg-Prod")
dgs3100_SWL2MGMT_MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89)).setLabel("dgs3100-SWL2MGMT-MIB")
rnd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89))
mibBuilder.exportSymbols("DLINK-3100-INC-MIB", dgs3124p_Prod=dgs3124p_Prod, dlink_products=dlink_products, dgs3148p_Prod=dgs3148p_Prod, dlink_Dgs3100SeriesProd=dlink_Dgs3100SeriesProd, dgs3124_Prod=dgs3124_Prod, dgs3148_Prod=dgs3148_Prod, dgs3100_SWL2MGMT_MIB=dgs3100_SWL2MGMT_MIB, rnd=rnd, dgs3124tg_Prod=dgs3124tg_Prod, dlink=dlink)
