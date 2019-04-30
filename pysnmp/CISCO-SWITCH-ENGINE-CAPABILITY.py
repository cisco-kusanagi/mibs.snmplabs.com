#
# PySNMP MIB module CISCO-SWITCH-ENGINE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-ENGINE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Gauge32, iso, Counter64, IpAddress, MibIdentifier, NotificationType, Counter32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "Counter64", "IpAddress", "MibIdentifier", "NotificationType", "Counter32", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSwitchEngineCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 343))
ciscoSwitchEngineCapability.setRevisions(('2013-07-25 00:00', '2012-09-10 00:00', '2011-09-28 00:00', '2010-11-11 00:00', '2010-03-22 00:00', '2008-10-30 00:00', '2007-07-16 00:00', '2005-09-16 00:00', '2005-08-24 00:00', '2004-12-22 00:00', '2004-06-14 00:00', '2004-01-15 00:00', '2003-12-04 00:00', '2003-08-12 00:00',))
if mibBuilder.loadTexts: ciscoSwitchEngineCapability.setLastUpdated('201307250000Z')
if mibBuilder.loadTexts: ciscoSwitchEngineCapability.setOrganization('Cisco Systems, Inc.')
cseCapCatOSV08R0101Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc = cseCapCatOSV08R0101Cat6KPfc.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                    series devices with PFC card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc = cseCapCatOSV08R0101Cat6KPfc.setStatus('current')
cseCapCatOSV08R0101Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc2 = cseCapCatOSV08R0101Cat6KPfc2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc2 = cseCapCatOSV08R0101Cat6KPfc2.setStatus('current')
cseCapCatOSV08R0101Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc3 = cseCapCatOSV08R0101Cat6KPfc3.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0101Cat6KPfc3 = cseCapCatOSV08R0101Cat6KPfc3.setStatus('current')
cseCapV12R0119ECat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0119ECat6KPfc = cseCapV12R0119ECat6KPfc.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                    series devices with PFC card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0119ECat6KPfc = cseCapV12R0119ECat6KPfc.setStatus('current')
cseCapV12R0119ECat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0119ECat6KPfc2 = cseCapV12R0119ECat6KPfc2.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0119ECat6KPfc2 = cseCapV12R0119ECat6KPfc2.setStatus('current')
cseCapV12R0217SXCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0217SXCat6KPfc3 = cseCapV12R0217SXCat6KPfc3.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0217SXCat6KPfc3 = cseCapV12R0217SXCat6KPfc3.setStatus('current')
cseCapCatOSV08R0301Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0301Cat6KPfc2 = cseCapCatOSV08R0301Cat6KPfc2.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0301Cat6KPfc2 = cseCapCatOSV08R0301Cat6KPfc2.setStatus('current')
cseCapCatOSV08R0301Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0301Cat6KPfc3 = cseCapCatOSV08R0301Cat6KPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0301Cat6KPfc3 = cseCapCatOSV08R0301Cat6KPfc3.setStatus('current')
cseCapCatOSV08R0401Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0401Cat6KPfc3 = cseCapCatOSV08R0401Cat6KPfc3.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0401Cat6KPfc3 = cseCapCatOSV08R0401Cat6KPfc3.setStatus('current')
cseCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0218SXEPCat6K = cseCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0218SXEPCat6K = cseCapV12R0218SXEPCat6K.setStatus('current')
cseCapCatOSV08R0501PCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0501PCat6KPfc3 = cseCapCatOSV08R0501PCat6KPfc3.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices with \n                    PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapCatOSV08R0501PCat6KPfc3 = cseCapCatOSV08R0501PCat6KPfc3.setStatus('current')
cseCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXHPCat6K = cseCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXHPCat6K = cseCapV12R0233SXHPCat6K.setStatus('current')
cseCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXIPCat6K = cseCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXIPCat6K = cseCapV12R0233SXIPCat6K.setStatus('current')
cseCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXI4PCat6K = cseCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0233SXI4PCat6K = cseCapV12R0233SXI4PCat6K.setStatus('current')
cseCapV12R0250SYPCat6KPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0250SYPCat6KPfc4 = cseCapV12R0250SYPCat6KPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices for PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV12R0250SYPCat6KPfc4 = cseCapV12R0250SYPCat6KPfc4.setStatus('current')
cseCapV15R0001SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0001SYPCat6kPfc4 = cseCapV15R0001SYPCat6kPfc4.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices for PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0001SYPCat6kPfc4 = cseCapV15R0001SYPCat6kPfc4.setStatus('current')
cseCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0101SYPCat6kPfc3 = cseCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0101SYPCat6kPfc3 = cseCapV15R0101SYPCat6kPfc3.setStatus('current')
cseCapV15R0101SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0101SYPCat6kPfc4 = cseCapV15R0101SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices for PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapV15R0101SYPCat6kPfc4 = cseCapV15R0101SYPCat6kPfc4.setStatus('current')
cseCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 343, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapNxOSV06R0104PN7k = cseCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cseCapNxOSV06R0104PN7k = cseCapNxOSV06R0104PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-ENGINE-CAPABILITY", cseCapV15R0001SYPCat6kPfc4=cseCapV15R0001SYPCat6kPfc4, cseCapV12R0218SXEPCat6K=cseCapV12R0218SXEPCat6K, cseCapV12R0233SXHPCat6K=cseCapV12R0233SXHPCat6K, cseCapCatOSV08R0101Cat6KPfc3=cseCapCatOSV08R0101Cat6KPfc3, cseCapV15R0101SYPCat6kPfc4=cseCapV15R0101SYPCat6kPfc4, cseCapV12R0233SXIPCat6K=cseCapV12R0233SXIPCat6K, cseCapV12R0233SXI4PCat6K=cseCapV12R0233SXI4PCat6K, cseCapCatOSV08R0301Cat6KPfc2=cseCapCatOSV08R0301Cat6KPfc2, cseCapV12R0119ECat6KPfc2=cseCapV12R0119ECat6KPfc2, cseCapV15R0101SYPCat6kPfc3=cseCapV15R0101SYPCat6kPfc3, cseCapCatOSV08R0301Cat6KPfc3=cseCapCatOSV08R0301Cat6KPfc3, cseCapV12R0250SYPCat6KPfc4=cseCapV12R0250SYPCat6KPfc4, cseCapV12R0217SXCat6KPfc3=cseCapV12R0217SXCat6KPfc3, cseCapCatOSV08R0401Cat6KPfc3=cseCapCatOSV08R0401Cat6KPfc3, cseCapV12R0119ECat6KPfc=cseCapV12R0119ECat6KPfc, PYSNMP_MODULE_ID=ciscoSwitchEngineCapability, ciscoSwitchEngineCapability=ciscoSwitchEngineCapability, cseCapCatOSV08R0101Cat6KPfc=cseCapCatOSV08R0101Cat6KPfc, cseCapCatOSV08R0501PCat6KPfc3=cseCapCatOSV08R0501PCat6KPfc3, cseCapNxOSV06R0104PN7k=cseCapNxOSV06R0104PN7k, cseCapCatOSV08R0101Cat6KPfc2=cseCapCatOSV08R0101Cat6KPfc2)
