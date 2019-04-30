#
# PySNMP MIB module SW3810PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3810PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:24:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, Counter32, ModuleIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, MibIdentifier, NotificationType, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Counter32", "ModuleIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "MibIdentifier", "NotificationType", "Unsigned32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Des3810Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114)).setLabel("dlink-Des3810Series")
des3810 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1))
des3810_28 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1)).setLabel("des3810-28")
des3810_28DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 2)).setLabel("des3810-28DC")
des3810_52 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3)).setLabel("des3810-52")
mibBuilder.exportSymbols("SW3810PRIMGMT-MIB", dlink_Des3810Series=dlink_Des3810Series, des3810_28=des3810_28, des3810_28DC=des3810_28DC, des3810=des3810, des3810_52=des3810_52)
