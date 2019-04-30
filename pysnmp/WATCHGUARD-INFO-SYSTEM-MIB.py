#
# PySNMP MIB module WATCHGUARD-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WATCHGUARD-INFO-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:29:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, NotificationType, Counter64, Integer32, IpAddress, MibIdentifier, Gauge32, Unsigned32, Counter32, ObjectIdentity, enterprises, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "NotificationType", "Counter64", "Integer32", "IpAddress", "MibIdentifier", "Gauge32", "Unsigned32", "Counter32", "ObjectIdentity", "enterprises", "iso", "TimeTicks")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-SMI", "watchguard")
wgInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 6))
wgInfoModule.setRevisions(('2007-01-25 12:00',))
if mibBuilder.loadTexts: wgInfoModule.setLastUpdated('200701251200Z')
if mibBuilder.loadTexts: wgInfoModule.setOrganization('WatchGuard Technologies, Inc.')
wgInfoSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 6, 1))
if mibBuilder.loadTexts: wgInfoSystem.setStatus('current')
wgInfoSystemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgInfoSystemCurrentTime.setStatus('current')
wgInfoGavService = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgInfoGavService.setStatus('current')
wgInfoIpsService = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgInfoIpsService.setStatus('current')
mibBuilder.exportSymbols("WATCHGUARD-INFO-SYSTEM-MIB", wgInfoSystemCurrentTime=wgInfoSystemCurrentTime, wgInfoModule=wgInfoModule, wgInfoGavService=wgInfoGavService, wgInfoSystem=wgInfoSystem, wgInfoIpsService=wgInfoIpsService, PYSNMP_MODULE_ID=wgInfoModule)
