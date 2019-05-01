#
# PySNMP MIB module WATCHGUARD-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WATCHGUARD-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:35:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, NotificationType, Unsigned32, TimeTicks, MibIdentifier, Counter32, IpAddress, iso, Counter64, Bits, Integer32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "NotificationType", "Unsigned32", "TimeTicks", "MibIdentifier", "Counter32", "IpAddress", "iso", "Counter64", "Bits", "Integer32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
watchguard = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097))
watchguard.setRevisions(('2008-11-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: watchguard.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: watchguard.setLastUpdated('200811100000Z')
if mibBuilder.loadTexts: watchguard.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: watchguard.setContactInfo(' WatchGuard Technologies, Inc. 505 Fifth Avenue South Suite 500 Seattle, WA 98104 United States +1.206.613.6600 ')
if mibBuilder.loadTexts: watchguard.setDescription('The Structure of Management Information for the WatchGuard enterprise.')
wgProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 1))
if mibBuilder.loadTexts: wgProducts.setStatus('current')
if mibBuilder.loadTexts: wgProducts.setDescription('wgProducts is the root OBJECT IDENTIFIER of WatchGuard Product OIDs.')
wgSystemConfigMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 2))
if mibBuilder.loadTexts: wgSystemConfigMIB.setStatus('current')
if mibBuilder.loadTexts: wgSystemConfigMIB.setDescription('wgSystemConfig is the root OBJECT IDENTIFIER of WatchGuard Firebox system configurations.')
mibBuilder.exportSymbols("WATCHGUARD-SMI", wgProducts=wgProducts, watchguard=watchguard, PYSNMP_MODULE_ID=watchguard, wgSystemConfigMIB=wgSystemConfigMIB)
