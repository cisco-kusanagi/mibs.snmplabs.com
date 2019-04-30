#
# PySNMP MIB module WATCHGUARD-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WATCHGUARD-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 21:29:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, enterprises, Gauge32, ObjectIdentity, NotificationType, Counter32, IpAddress, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "enterprises", "Gauge32", "ObjectIdentity", "NotificationType", "Counter32", "IpAddress", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
watchguard = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097))
watchguard.setRevisions(('2008-11-10 00:00',))
if mibBuilder.loadTexts: watchguard.setLastUpdated('200811100000Z')
if mibBuilder.loadTexts: watchguard.setOrganization('WatchGuard Technologies, Inc.')
wgProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 1))
if mibBuilder.loadTexts: wgProducts.setStatus('current')
wgSystemConfigMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 2))
if mibBuilder.loadTexts: wgSystemConfigMIB.setStatus('current')
mibBuilder.exportSymbols("WATCHGUARD-SMI", wgProducts=wgProducts, PYSNMP_MODULE_ID=watchguard, watchguard=watchguard, wgSystemConfigMIB=wgSystemConfigMIB)
