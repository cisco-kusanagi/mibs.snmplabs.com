#
# PySNMP MIB module CISCO-UDLDP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UDLDP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:58:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
IpAddress, NotificationType, ObjectIdentity, Integer32, ModuleIdentity, iso, Bits, TimeTicks, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "ObjectIdentity", "Integer32", "ModuleIdentity", "iso", "Bits", "TimeTicks", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoUdldpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 344))
ciscoUdldpCapability.setRevisions(('2012-09-10 00:00', '2011-03-30 00:00', '2010-03-16 09:00', '2004-04-07 00:00',))
if mibBuilder.loadTexts: ciscoUdldpCapability.setLastUpdated('201209100000Z')
if mibBuilder.loadTexts: ciscoUdldpCapability.setOrganization('Cisco Systems, Inc.')
ciscoUdldpCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV12R0214SXCat6K = ciscoUdldpCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14SX) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV12R0214SXCat6K = ciscoUdldpCapV12R0214SXCat6K.setStatus('current')
ciscoUdldpCapCatOSV07R0604 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapCatOSV07R0604 = ciscoUdldpCapCatOSV07R0604.setProductRelease('Cisco CatOS 7.6(4).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapCatOSV07R0604 = ciscoUdldpCapCatOSV07R0604.setStatus('current')
ciscoUdldpCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapCatOSV08R0101 = ciscoUdldpCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapCatOSV08R0101 = ciscoUdldpCapCatOSV08R0101.setStatus('current')
ciscoUdldpCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV12R0233SXI4PCat6K = ciscoUdldpCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices running IOS images.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV12R0233SXI4PCat6K = ciscoUdldpCapV12R0233SXI4PCat6K.setStatus('current')
ciscoUdldpCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV15R0002SGPCat4K = ciscoUdldpCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Catalyst 4000 family\n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV15R0002SGPCat4K = ciscoUdldpCapV15R0002SGPCat4K.setStatus('current')
ciscoUdldpCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 344, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV15R0001SY1PCat6K = ciscoUdldpCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUdldpCapV15R0001SY1PCat6K = ciscoUdldpCapV15R0001SY1PCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-UDLDP-CAPABILITY", PYSNMP_MODULE_ID=ciscoUdldpCapability, ciscoUdldpCapability=ciscoUdldpCapability, ciscoUdldpCapV12R0214SXCat6K=ciscoUdldpCapV12R0214SXCat6K, ciscoUdldpCapCatOSV08R0101=ciscoUdldpCapCatOSV08R0101, ciscoUdldpCapV12R0233SXI4PCat6K=ciscoUdldpCapV12R0233SXI4PCat6K, ciscoUdldpCapCatOSV07R0604=ciscoUdldpCapCatOSV07R0604, ciscoUdldpCapV15R0002SGPCat4K=ciscoUdldpCapV15R0002SGPCat4K, ciscoUdldpCapV15R0001SY1PCat6K=ciscoUdldpCapV15R0001SY1PCat6K)
