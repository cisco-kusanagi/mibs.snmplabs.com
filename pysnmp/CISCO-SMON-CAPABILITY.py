#
# PySNMP MIB module CISCO-SMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SMON-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, Counter64, NotificationType, ModuleIdentity, Unsigned32, Gauge32, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Bits, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "NotificationType", "ModuleIdentity", "Unsigned32", "Gauge32", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Bits", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 381))
ciscoSmonCapability.setRevisions(('2004-01-22 00:00',))
if mibBuilder.loadTexts: ciscoSmonCapability.setLastUpdated('200401220000Z')
if mibBuilder.loadTexts: ciscoSmonCapability.setOrganization('Cisco Systems, Inc.')
csCapV12R0214SXCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0214SXCat6KPfc3 = csCapV12R0214SXCat6KPfc3.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 3 (PFC 3).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0214SXCat6KPfc3 = csCapV12R0214SXCat6KPfc3.setStatus('current')
csCapV12R0113ECat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0113ECat6KPfc2 = csCapV12R0113ECat6KPfc2.setProductRelease('Cisco IOS 12.1(13)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 2 (PFC 2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0113ECat6KPfc2 = csCapV12R0113ECat6KPfc2.setStatus('current')
csCapCatOSV07R0102Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapCatOSV07R0102Cat6KPfc2 = csCapCatOSV07R0102Cat6KPfc2.setProductRelease('Cisco CatOS 7.1(2) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 2 (PFC 2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapCatOSV07R0102Cat6KPfc2 = csCapCatOSV07R0102Cat6KPfc2.setStatus('current')
mibBuilder.exportSymbols("CISCO-SMON-CAPABILITY", PYSNMP_MODULE_ID=ciscoSmonCapability, csCapV12R0113ECat6KPfc2=csCapV12R0113ECat6KPfc2, csCapV12R0214SXCat6KPfc3=csCapV12R0214SXCat6KPfc3, ciscoSmonCapability=ciscoSmonCapability, csCapCatOSV07R0102Cat6KPfc2=csCapCatOSV07R0102Cat6KPfc2)
