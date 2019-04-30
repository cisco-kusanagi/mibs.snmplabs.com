#
# PySNMP MIB module SW6500PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW6500PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, IpAddress, iso, Gauge32, Unsigned32, MibIdentifier, ObjectIdentity, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "IpAddress", "iso", "Gauge32", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Des6500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 78)).setLabel("dlink-Des6500SeriesProd")
dlink_Des6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 78, 1)).setLabel("dlink-Des6500")
des6500SeriesProd = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 78))
des6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 78, 1))
mibBuilder.exportSymbols("SW6500PRIMGMT-MIB", des6500=des6500, dlink_Des6500SeriesProd=dlink_Des6500SeriesProd, des6500SeriesProd=des6500SeriesProd, dlink_Des6500=dlink_Des6500)
