#
# PySNMP MIB module WATCHGUARD-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WATCHGUARD-INFO-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, ModuleIdentity, enterprises, Bits, MibIdentifier, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Integer32, iso, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ModuleIdentity", "enterprises", "Bits", "MibIdentifier", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Integer32", "iso", "ObjectIdentity", "NotificationType")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-SMI", "watchguard")
wgInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 6))
wgInfoModule.setRevisions(('2007-01-25 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wgInfoModule.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: wgInfoModule.setLastUpdated('200701251200Z')
if mibBuilder.loadTexts: wgInfoModule.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: wgInfoModule.setContactInfo(' WatchGuard Technologies, Inc. 505 Fifth Avenue South Suite 500 Seattle, WA 98104 United States +1.206.613.6600 ')
if mibBuilder.loadTexts: wgInfoModule.setDescription('The MIB module describes general information of WatchGuard system. Mainly, the information obtained from this MIB is used by wgInfoSystemMIB, wgClientMIB, wgSystemStatisticsMIB, wgIpsecTunnelMIB.')
wgInfoSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 6, 1))
if mibBuilder.loadTexts: wgInfoSystem.setStatus('current')
if mibBuilder.loadTexts: wgInfoSystem.setDescription('This is the base system information for all wg Client branches.')
wgInfoSystemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgInfoSystemCurrentTime.setStatus('current')
if mibBuilder.loadTexts: wgInfoSystemCurrentTime.setDescription("The host's notion of the local date and time of day.")
wgInfoGavService = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgInfoGavService.setStatus('current')
if mibBuilder.loadTexts: wgInfoGavService.setDescription('Version and update time of Gateway Antivirus Service')
wgInfoIpsService = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgInfoIpsService.setStatus('current')
if mibBuilder.loadTexts: wgInfoIpsService.setDescription('Version and update time of Intrusion Prevention Service')
mibBuilder.exportSymbols("WATCHGUARD-INFO-SYSTEM-MIB", wgInfoGavService=wgInfoGavService, wgInfoIpsService=wgInfoIpsService, wgInfoSystemCurrentTime=wgInfoSystemCurrentTime, wgInfoSystem=wgInfoSystem, wgInfoModule=wgInfoModule, PYSNMP_MODULE_ID=wgInfoModule)
