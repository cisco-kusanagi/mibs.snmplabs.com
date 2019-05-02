#
# PySNMP MIB module CISCO-ENVMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENVMON-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ObjectIdentity, Bits, Unsigned32, iso, ModuleIdentity, Counter64, MibIdentifier, NotificationType, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ObjectIdentity", "Bits", "Unsigned32", "iso", "ModuleIdentity", "Counter64", "MibIdentifier", "NotificationType", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEnvMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 33))
ciscoEnvMonCapability.setRevisions(('2009-12-16 00:00', '2009-01-05 00:00', '2007-05-18 00:00', '2006-12-12 00:00', '2006-07-19 00:00', '2006-04-19 00:00', '2004-12-16 01:00', '2004-03-26 00:00', '1996-11-12 00:00', '1995-01-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEnvMonCapability.setRevisionsDescriptions(('Added agent capabilities for Wireless LAN Controllers.', 'Added agent capabilities for TelePresence platforms.', 'The following capability statements have been added: 1. ciscoEnvMonCapV12R05TP28xx 2. ciscoEnvMonCapV12R05TP3825 3. ciscoEnvMonCapV12R05TP3845 4. ciscoEnvMonCapV12R05TP1841Rev1 ciscoEnvMonCapV12R05TP1841 has been made obsolete by ciscoEnvMonCapV12R05TP1841Rev1. ciscoEnvMonCapV12R05TPMARS has been updated to indicate the platforms this capability statement is applicable to.', 'Added VARIATION for ciscoEnvMonMIBGroupRev, ciscoEnvMonMIBMiscNotifGroup and ciscoEnvMonStatChangeNotifGroup with PCBU platform routers (180x, 181x, 1841 & 2801).', 'Added VARIATION for ciscoEnvMonStatChangeNotifGroup to MARs platform routers (26xx, 28xx, 37xx, 38xx, IAD243x and VG224).', 'Added VARIATION for ciscoEnvMonTemperatureLastShutdown to agent capability statement ciscoEnvMonCapV12R0119ECat6K.', 'Added agent capabilities for 38xx, 37xx, 26xx, 28xx, VG224 and IAD243x platforms.', 'Added agent capability statements ciscoEnvMonCapCatOSV08R0101Cat6k, ciscoEnvMonCapCatOSV08R0101Cat4k, ciscoEnvMonCapV12R0119ECat6K.', 'Added agent capabilities for platform c3600.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEnvMonCapability.setLastUpdated('200912160000Z')
if mibBuilder.loadTexts: ciscoEnvMonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEnvMonCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEnvMonCapability.setDescription('Agent capabilities for CISCO-ENVMON-MIB.')
ciscoEnvMonCapabilityV10R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapabilityV10R03 = ciscoEnvMonCapabilityV10R03.setProductRelease('Cisco IOS 10.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapabilityV10R03 = ciscoEnvMonCapabilityV10R03.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoEnvMonCapabilityV10R03.setDescription('Cisco Environmental Monitor MIB capabilities')
ciscoEnvMonCapabilityV11R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapabilityV11R02 = ciscoEnvMonCapabilityV11R02.setProductRelease('Cisco IOS 11.2 on mid-range platforms C3600.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapabilityV11R02 = ciscoEnvMonCapabilityV11R02.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapabilityV11R02.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapCatOSV08R0101Cat6k = ciscoEnvMonCapCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapCatOSV08R0101Cat6k = ciscoEnvMonCapCatOSV08R0101Cat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapCatOSV08R0101Cat6k.setDescription('CISCO-ENVMON-MIB capabilities.')
ciscoEnvMonCapCatOSV08R0101Cat4k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapCatOSV08R0101Cat4k = ciscoEnvMonCapCatOSV08R0101Cat4k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000/4500\n                          series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapCatOSV08R0101Cat4k = ciscoEnvMonCapCatOSV08R0101Cat4k.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapCatOSV08R0101Cat4k.setDescription('CISCO-ENVMON-MIB capabilities.')
ciscoEnvMonCapV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R0119ECat6K = ciscoEnvMonCapV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                       and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R0119ECat6K = ciscoEnvMonCapV12R0119ECat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R0119ECat6K.setDescription('CISCO-ENVMON-MIB capabilities.')
ciscoEnvMonCapV12R04TP37xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP37xx = ciscoEnvMonCapV12R04TP37xx.setProductRelease('Cisco IOS 12.4T on c37xx devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP37xx = ciscoEnvMonCapV12R04TP37xx.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R04TP37xx.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R04TP28xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP28xx = ciscoEnvMonCapV12R04TP28xx.setProductRelease('Cisco IOS 12.4T on c28xx devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP28xx = ciscoEnvMonCapV12R04TP28xx.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R04TP28xx.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R04TP26xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP26xx = ciscoEnvMonCapV12R04TP26xx.setProductRelease('Cisco IOS 12.4T on c26xx devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP26xx = ciscoEnvMonCapV12R04TP26xx.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R04TP26xx.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R04TPIAD243x = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TPIAD243x = ciscoEnvMonCapV12R04TPIAD243x.setProductRelease('Cisco IOS 12.4T on IAD243x devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TPIAD243x = ciscoEnvMonCapV12R04TPIAD243x.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R04TPIAD243x.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R04TPVG224 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TPVG224 = ciscoEnvMonCapV12R04TPVG224.setProductRelease('Cisco IOS 12.4T on VG224 devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TPVG224 = ciscoEnvMonCapV12R04TPVG224.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R04TPVG224.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R04TP3825 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP3825 = ciscoEnvMonCapV12R04TP3825.setProductRelease('Cisco IOS 12.4T on c3825 devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP3825 = ciscoEnvMonCapV12R04TP3825.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R04TP3825.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R04TP3845 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP3845 = ciscoEnvMonCapV12R04TP3845.setProductRelease('Cisco IOS 12.4T on c3845 devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP3845 = ciscoEnvMonCapV12R04TP3845.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R04TP3845.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R04TP2691 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP2691 = ciscoEnvMonCapV12R04TP2691.setProductRelease('Cisco IOS 12.4T on c2691 devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R04TP2691 = ciscoEnvMonCapV12R04TP2691.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R04TP2691.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R05TPMARS = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TPMARS = ciscoEnvMonCapV12R05TPMARS.setProductRelease('Cisco IOS 12.5T on MARS devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TPMARS = ciscoEnvMonCapV12R05TPMARS.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R05TPMARS.setDescription('Cisco Environmental Monitor MIB capabilities for 26xx, 28xx, 37xx, 38xx, IAD243x and VG224 platforms.')
ciscoEnvMonCapV12R05TP180x = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP180x = ciscoEnvMonCapV12R05TP180x.setProductRelease('Cisco IOS 12.5T on 180x PCBU devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP180x = ciscoEnvMonCapV12R05TP180x.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R05TP180x.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R05TP181x = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP181x = ciscoEnvMonCapV12R05TP181x.setProductRelease('Cisco IOS 12.5T on 181x PCBU devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP181x = ciscoEnvMonCapV12R05TP181x.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R05TP181x.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R05TP1841 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP1841 = ciscoEnvMonCapV12R05TP1841.setProductRelease('Cisco IOS 12.5T on 1841 & 2801 PCBU devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP1841 = ciscoEnvMonCapV12R05TP1841.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R05TP1841.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R05TP28xx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP28xx = ciscoEnvMonCapV12R05TP28xx.setProductRelease('Cisco IOS 12.5T on c28xx devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP28xx = ciscoEnvMonCapV12R05TP28xx.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R05TP28xx.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R05TP3825 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP3825 = ciscoEnvMonCapV12R05TP3825.setProductRelease('Cisco IOS 12.5T on c3825 devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP3825 = ciscoEnvMonCapV12R05TP3825.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R05TP3825.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R05TP3845 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP3845 = ciscoEnvMonCapV12R05TP3845.setProductRelease('Cisco IOS 12.5T on c3845 devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP3845 = ciscoEnvMonCapV12R05TP3845.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R05TP3845.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapV12R05TP1841Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP1841Rev1 = ciscoEnvMonCapV12R05TP1841Rev1.setProductRelease('Cisco IOS 12.5T on 1841 and 2801 PCBU devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapV12R05TP1841Rev1 = ciscoEnvMonCapV12R05TP1841Rev1.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapV12R05TP1841Rev1.setDescription('Cisco Environmental Monitor MIB capabilities.')
ciscoEnvMonCapabilityCTSV140 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapabilityCTSV140 = ciscoEnvMonCapabilityCTSV140.setProductRelease('Cisco TelePresence System (CTS) 1.4.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapabilityCTSV140 = ciscoEnvMonCapabilityCTSV140.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapabilityCTSV140.setDescription('Agent capabilities for CISCO-ENVMON-MIB.')
ciscoEnvMonCapabilityWLCV70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 33, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapabilityWLCV70 = ciscoEnvMonCapabilityWLCV70.setProductRelease('Cisco Wireless LAN Controller version 7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnvMonCapabilityWLCV70 = ciscoEnvMonCapabilityWLCV70.setStatus('current')
if mibBuilder.loadTexts: ciscoEnvMonCapabilityWLCV70.setDescription('Agent capabilities for CISCO-ENVMON-MIB.')
mibBuilder.exportSymbols("CISCO-ENVMON-CAPABILITY", ciscoEnvMonCapV12R05TP181x=ciscoEnvMonCapV12R05TP181x, ciscoEnvMonCapV12R05TPMARS=ciscoEnvMonCapV12R05TPMARS, ciscoEnvMonCapV12R04TP26xx=ciscoEnvMonCapV12R04TP26xx, ciscoEnvMonCapV12R04TP37xx=ciscoEnvMonCapV12R04TP37xx, ciscoEnvMonCapV12R0119ECat6K=ciscoEnvMonCapV12R0119ECat6K, ciscoEnvMonCapabilityV10R03=ciscoEnvMonCapabilityV10R03, ciscoEnvMonCapV12R04TP3845=ciscoEnvMonCapV12R04TP3845, ciscoEnvMonCapV12R05TP1841Rev1=ciscoEnvMonCapV12R05TP1841Rev1, ciscoEnvMonCapV12R04TP28xx=ciscoEnvMonCapV12R04TP28xx, ciscoEnvMonCapV12R04TPIAD243x=ciscoEnvMonCapV12R04TPIAD243x, ciscoEnvMonCapV12R05TP28xx=ciscoEnvMonCapV12R05TP28xx, ciscoEnvMonCapV12R04TP2691=ciscoEnvMonCapV12R04TP2691, ciscoEnvMonCapV12R04TPVG224=ciscoEnvMonCapV12R04TPVG224, ciscoEnvMonCapV12R05TP3825=ciscoEnvMonCapV12R05TP3825, ciscoEnvMonCapV12R04TP3825=ciscoEnvMonCapV12R04TP3825, ciscoEnvMonCapV12R05TP3845=ciscoEnvMonCapV12R05TP3845, ciscoEnvMonCapV12R05TP1841=ciscoEnvMonCapV12R05TP1841, ciscoEnvMonCapCatOSV08R0101Cat4k=ciscoEnvMonCapCatOSV08R0101Cat4k, ciscoEnvMonCapabilityWLCV70=ciscoEnvMonCapabilityWLCV70, ciscoEnvMonCapabilityV11R02=ciscoEnvMonCapabilityV11R02, ciscoEnvMonCapCatOSV08R0101Cat6k=ciscoEnvMonCapCatOSV08R0101Cat6k, ciscoEnvMonCapabilityCTSV140=ciscoEnvMonCapabilityCTSV140, ciscoEnvMonCapV12R05TP180x=ciscoEnvMonCapV12R05TP180x, PYSNMP_MODULE_ID=ciscoEnvMonCapability, ciscoEnvMonCapability=ciscoEnvMonCapability)
