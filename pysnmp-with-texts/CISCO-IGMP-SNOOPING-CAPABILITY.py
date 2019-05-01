#
# PySNMP MIB module CISCO-IGMP-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IGMP-SNOOPING-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:01:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, Bits, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, TimeTicks, ObjectIdentity, Counter32, ModuleIdentity, MibIdentifier, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "TimeTicks", "ObjectIdentity", "Counter32", "ModuleIdentity", "MibIdentifier", "Gauge32", "Counter64")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoIgmpSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 320))
ciscoIgmpSnoopingCapability.setRevisions(('2012-09-12 00:00', '2010-11-16 00:00', '2008-10-31 00:00', '2004-03-10 00:00', '2003-08-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIgmpSnoopingCapability.setRevisionsDescriptions(('Added the following capability statements: - cisCapV15R0101SYPCat6kPfc3 - cisCapV15R0101SYPCat6kPfc4 Updated the following capability statements: - cisCapV12R0233SXIPCat6K - cisCapV12R0250SYPCat6K.', 'Added capability statement cisCapV12R0250SYPCat6K.', 'Added capability statement cisCapV12R0233SXIPCat6K.', 'Added the following capability statements: - cisCapCatOSV08R0301Cat6kPfc2 - cisCapCatOSV08R0301Cat6kPfc3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIgmpSnoopingCapability.setLastUpdated('201209120000Z')
if mibBuilder.loadTexts: ciscoIgmpSnoopingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIgmpSnoopingCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-ipmulticast@cisco.com')
if mibBuilder.loadTexts: ciscoIgmpSnoopingCapability.setDescription('The capabilities description of CISCO-IGMP-SNOOPING-MIB.')
cisCapCatOSV08R0101Cat6kPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc = cisCapCatOSV08R0101Cat6kPfc.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc = cisCapCatOSV08R0101Cat6kPfc.setStatus('current')
if mibBuilder.loadTexts: cisCapCatOSV08R0101Cat6kPfc.setDescription('CISCO-IGMP-SNOOPING-MIB capabilities.')
cisCapCatOSV08R0101Cat6kPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc2 = cisCapCatOSV08R0101Cat6kPfc2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc2 = cisCapCatOSV08R0101Cat6kPfc2.setStatus('current')
if mibBuilder.loadTexts: cisCapCatOSV08R0101Cat6kPfc2.setDescription('CISCO-IGMP-SNOOPING-MIB capabilities.')
cisCapCatOSV08R0101Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc3 = cisCapCatOSV08R0101Cat6kPfc3.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0101Cat6kPfc3 = cisCapCatOSV08R0101Cat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: cisCapCatOSV08R0101Cat6kPfc3.setDescription('CISCO-IGMP-SNOOPING-MIB capabilities.')
cisCapCatOSV08R0301Cat6kPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc2 = cisCapCatOSV08R0301Cat6kPfc2.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc2 = cisCapCatOSV08R0301Cat6kPfc2.setStatus('current')
if mibBuilder.loadTexts: cisCapCatOSV08R0301Cat6kPfc2.setDescription('CISCO-IGMP-SNOOPING-MIB capabilities.')
cisCapCatOSV08R0301Cat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc3 = cisCapCatOSV08R0301Cat6kPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 and\n                         Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapCatOSV08R0301Cat6kPfc3 = cisCapCatOSV08R0301Cat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: cisCapCatOSV08R0301Cat6kPfc3.setDescription('CISCO-IGMP-SNOOPING-MIB capabilities.')
cisCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0233SXIPCat6K = cisCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0233SXIPCat6K = cisCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cisCapV12R0233SXIPCat6K.setDescription('CISCO-IGMP-SNOOPING-MIB capabilities.')
cisCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0250SYPCat6K = cisCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV12R0250SYPCat6K = cisCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cisCapV12R0250SYPCat6K.setDescription('CISCO-IGMP-SNOOPING-MIB capabilities.')
cisCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc3 = cisCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc3 = cisCapV15R0101SYPCat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: cisCapV15R0101SYPCat6kPfc3.setDescription('CISCO-IGMP-SNOOPING-MIB capabilities.')
cisCapV15R0101SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 320, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc4 = cisCapV15R0101SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisCapV15R0101SYPCat6kPfc4 = cisCapV15R0101SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: cisCapV15R0101SYPCat6kPfc4.setDescription('CISCO-IGMP-SNOOPING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IGMP-SNOOPING-CAPABILITY", cisCapV12R0233SXIPCat6K=cisCapV12R0233SXIPCat6K, PYSNMP_MODULE_ID=ciscoIgmpSnoopingCapability, cisCapV15R0101SYPCat6kPfc3=cisCapV15R0101SYPCat6kPfc3, ciscoIgmpSnoopingCapability=ciscoIgmpSnoopingCapability, cisCapV12R0250SYPCat6K=cisCapV12R0250SYPCat6K, cisCapCatOSV08R0101Cat6kPfc=cisCapCatOSV08R0101Cat6kPfc, cisCapCatOSV08R0301Cat6kPfc3=cisCapCatOSV08R0301Cat6kPfc3, cisCapCatOSV08R0101Cat6kPfc2=cisCapCatOSV08R0101Cat6kPfc2, cisCapV15R0101SYPCat6kPfc4=cisCapV15R0101SYPCat6kPfc4, cisCapCatOSV08R0301Cat6kPfc2=cisCapCatOSV08R0301Cat6kPfc2, cisCapCatOSV08R0101Cat6kPfc3=cisCapCatOSV08R0101Cat6kPfc3)
