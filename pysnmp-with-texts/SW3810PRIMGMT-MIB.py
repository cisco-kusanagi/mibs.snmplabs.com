#
# PySNMP MIB module SW3810PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW3810PRIMGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:39:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
dlink_products, dlink_mgmt = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-products", "dlink-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Gauge32, ObjectIdentity, Integer32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter64, ModuleIdentity, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "Integer32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter64", "ModuleIdentity", "MibIdentifier", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Des3810Series = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114)).setLabel("dlink-Des3810Series")
des3810 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1))
des3810_28 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1)).setLabel("des3810-28")
des3810_28DC = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 2)).setLabel("des3810-28DC")
des3810_52 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3)).setLabel("des3810-52")
mibBuilder.exportSymbols("SW3810PRIMGMT-MIB", des3810_28DC=des3810_28DC, des3810_52=des3810_52, des3810_28=des3810_28, des3810=des3810, dlink_Des3810Series=dlink_Des3810Series)
