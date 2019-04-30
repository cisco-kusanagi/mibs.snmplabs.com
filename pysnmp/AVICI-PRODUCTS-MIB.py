#
# PySNMP MIB module AVICI-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVICI-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:16:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
aviciMibs, aviciProducts = mibBuilder.importSymbols("AVICI-SMI", "aviciMibs", "aviciProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, ModuleIdentity, Unsigned32, IpAddress, iso, MibIdentifier, Counter32, NotificationType, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "ModuleIdentity", "Unsigned32", "IpAddress", "iso", "MibIdentifier", "Counter32", "NotificationType", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aviciProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2474, 1, 1))
if mibBuilder.loadTexts: aviciProductsMIB.setLastUpdated('000524190000Z')
if mibBuilder.loadTexts: aviciProductsMIB.setOrganization('Avici Systems, Inc.')
aviciTSR = MibIdentifier((1, 3, 6, 1, 4, 1, 2474, 2, 1))
mibBuilder.exportSymbols("AVICI-PRODUCTS-MIB", PYSNMP_MODULE_ID=aviciProductsMIB, aviciProductsMIB=aviciProductsMIB, aviciTSR=aviciTSR)
