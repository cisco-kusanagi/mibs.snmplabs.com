#
# PySNMP MIB module CISCO-SMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SMON-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Bits, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, TimeTicks, Counter32, Gauge32, iso, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Bits", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "TimeTicks", "Counter32", "Gauge32", "iso", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 381))
ciscoSmonCapability.setRevisions(('2004-01-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSmonCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSmonCapability.setLastUpdated('200401220000Z')
if mibBuilder.loadTexts: ciscoSmonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSmonCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSmonCapability.setDescription('Agent capabilities for SMON-MIB.')
csCapV12R0214SXCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0214SXCat6KPfc3 = csCapV12R0214SXCat6KPfc3.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 3 (PFC 3).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0214SXCat6KPfc3 = csCapV12R0214SXCat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: csCapV12R0214SXCat6KPfc3.setDescription('SMON-MIB agent capabilities.')
csCapV12R0113ECat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0113ECat6KPfc2 = csCapV12R0113ECat6KPfc2.setProductRelease('Cisco IOS 12.1(13)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 2 (PFC 2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0113ECat6KPfc2 = csCapV12R0113ECat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: csCapV12R0113ECat6KPfc2.setDescription('SMON-MIB agent capabilities.')
csCapCatOSV07R0102Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapCatOSV07R0102Cat6KPfc2 = csCapCatOSV07R0102Cat6KPfc2.setProductRelease('Cisco CatOS 7.1(2) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 2 (PFC 2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapCatOSV07R0102Cat6KPfc2 = csCapCatOSV07R0102Cat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: csCapCatOSV07R0102Cat6KPfc2.setDescription('SMON-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-SMON-CAPABILITY", csCapV12R0214SXCat6KPfc3=csCapV12R0214SXCat6KPfc3, csCapCatOSV07R0102Cat6KPfc2=csCapCatOSV07R0102Cat6KPfc2, PYSNMP_MODULE_ID=ciscoSmonCapability, csCapV12R0113ECat6KPfc2=csCapV12R0113ECat6KPfc2, ciscoSmonCapability=ciscoSmonCapability)
