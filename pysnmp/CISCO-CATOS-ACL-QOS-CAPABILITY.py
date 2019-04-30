#
# PySNMP MIB module CISCO-CATOS-ACL-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CATOS-ACL-QOS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, Counter32, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, NotificationType, MibIdentifier, IpAddress, iso, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "NotificationType", "MibIdentifier", "IpAddress", "iso", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCatOSAclQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 325))
ciscoCatOSAclQosCapability.setRevisions(('2008-03-17 00:00', '2006-06-29 00:00', '2005-09-06 00:00', '2004-06-24 00:00', '2004-01-27 00:00', '2003-12-19 00:00', '2003-08-25 10:00',))
if mibBuilder.loadTexts: ciscoCatOSAclQosCapability.setLastUpdated('200803170000Z')
if mibBuilder.loadTexts: ciscoCatOSAclQosCapability.setOrganization('Cisco Systems, Inc.')
caqCapabilityV08R0101Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc = caqCapabilityV08R0101Cat6KPfc.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc = caqCapabilityV08R0101Cat6KPfc.setStatus('current')
caqCapabilityV08R0101Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc2 = caqCapabilityV08R0101Cat6KPfc2.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc2 = caqCapabilityV08R0101Cat6KPfc2.setStatus('current')
caqCapabilityV08R0101Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc3 = caqCapabilityV08R0101Cat6KPfc3.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat6KPfc3 = caqCapabilityV08R0101Cat6KPfc3.setStatus('current')
caqCapabilityV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat4K = caqCapabilityV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0101Cat4K = caqCapabilityV08R0101Cat4K.setStatus('current')
caqCapabilityV08R0301Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc = caqCapabilityV08R0301Cat6KPfc.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc = caqCapabilityV08R0301Cat6KPfc.setStatus('current')
caqCapabilityV08R0301Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc2 = caqCapabilityV08R0301Cat6KPfc2.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc2 = caqCapabilityV08R0301Cat6KPfc2.setStatus('current')
caqCapabilityV08R0301Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc3 = caqCapabilityV08R0301Cat6KPfc3.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0301Cat6KPfc3 = caqCapabilityV08R0301Cat6KPfc3.setStatus('current')
caqCapabilityV08R0401Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc = caqCapabilityV08R0401Cat6KPfc.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc = caqCapabilityV08R0401Cat6KPfc.setStatus('current')
caqCapabilityV08R0401Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc2 = caqCapabilityV08R0401Cat6KPfc2.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc2 = caqCapabilityV08R0401Cat6KPfc2.setStatus('current')
caqCapabilityV08R0401Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3 = caqCapabilityV08R0401Cat6KPfc3.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3 = caqCapabilityV08R0401Cat6KPfc3.setStatus('current')
caqCapabilityV08R0401Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3b = caqCapabilityV08R0401Cat6KPfc3b.setProductRelease('Cisco CatOS 8.4(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0401Cat6KPfc3b = caqCapabilityV08R0401Cat6KPfc3b.setStatus('current')
caqCapabilityV08R0501Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc = caqCapabilityV08R0501Cat6KPfc.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc = caqCapabilityV08R0501Cat6KPfc.setStatus('current')
caqCapabilityV08R0501Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc2 = caqCapabilityV08R0501Cat6KPfc2.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc2 = caqCapabilityV08R0501Cat6KPfc2.setStatus('current')
caqCapabilityV08R0501Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3 = caqCapabilityV08R0501Cat6KPfc3.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3 = caqCapabilityV08R0501Cat6KPfc3.setStatus('current')
caqCapabilityV08R0501Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 15))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3b = caqCapabilityV08R0501Cat6KPfc3b.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0501Cat6KPfc3b = caqCapabilityV08R0501Cat6KPfc3b.setStatus('current')
caqCapabilityV08R0601Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 16))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc = caqCapabilityV08R0601Cat6KPfc.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc = caqCapabilityV08R0601Cat6KPfc.setStatus('current')
caqCapabilityV08R0601Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 17))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc2 = caqCapabilityV08R0601Cat6KPfc2.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc2 = caqCapabilityV08R0601Cat6KPfc2.setStatus('current')
caqCapabilityV08R0601Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 18))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3 = caqCapabilityV08R0601Cat6KPfc3.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3 = caqCapabilityV08R0601Cat6KPfc3.setStatus('current')
caqCapabilityV08R0601Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 19))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3b = caqCapabilityV08R0601Cat6KPfc3b.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0601Cat6KPfc3b = caqCapabilityV08R0601Cat6KPfc3b.setStatus('current')
caqCapabilityV08R0701Cat6KPfc = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 20))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc = caqCapabilityV08R0701Cat6KPfc.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc = caqCapabilityV08R0701Cat6KPfc.setStatus('current')
caqCapabilityV08R0701Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 21))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc2 = caqCapabilityV08R0701Cat6KPfc2.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC2\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc2 = caqCapabilityV08R0701Cat6KPfc2.setStatus('current')
caqCapabilityV08R0701Cat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 22))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3 = caqCapabilityV08R0701Cat6KPfc3.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3\n                         card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3 = caqCapabilityV08R0701Cat6KPfc3.setStatus('current')
caqCapabilityV08R0701Cat6KPfc3b = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 325, 23))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3b = caqCapabilityV08R0701Cat6KPfc3b.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with PFC3B\n                         or PFC3BXL card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caqCapabilityV08R0701Cat6KPfc3b = caqCapabilityV08R0701Cat6KPfc3b.setStatus('current')
mibBuilder.exportSymbols("CISCO-CATOS-ACL-QOS-CAPABILITY", caqCapabilityV08R0501Cat6KPfc3=caqCapabilityV08R0501Cat6KPfc3, caqCapabilityV08R0401Cat6KPfc3=caqCapabilityV08R0401Cat6KPfc3, caqCapabilityV08R0601Cat6KPfc2=caqCapabilityV08R0601Cat6KPfc2, caqCapabilityV08R0301Cat6KPfc3=caqCapabilityV08R0301Cat6KPfc3, caqCapabilityV08R0301Cat6KPfc=caqCapabilityV08R0301Cat6KPfc, PYSNMP_MODULE_ID=ciscoCatOSAclQosCapability, caqCapabilityV08R0501Cat6KPfc=caqCapabilityV08R0501Cat6KPfc, caqCapabilityV08R0601Cat6KPfc3b=caqCapabilityV08R0601Cat6KPfc3b, caqCapabilityV08R0101Cat6KPfc=caqCapabilityV08R0101Cat6KPfc, caqCapabilityV08R0101Cat6KPfc2=caqCapabilityV08R0101Cat6KPfc2, caqCapabilityV08R0501Cat6KPfc3b=caqCapabilityV08R0501Cat6KPfc3b, caqCapabilityV08R0101Cat4K=caqCapabilityV08R0101Cat4K, caqCapabilityV08R0401Cat6KPfc2=caqCapabilityV08R0401Cat6KPfc2, caqCapabilityV08R0501Cat6KPfc2=caqCapabilityV08R0501Cat6KPfc2, caqCapabilityV08R0701Cat6KPfc2=caqCapabilityV08R0701Cat6KPfc2, caqCapabilityV08R0701Cat6KPfc=caqCapabilityV08R0701Cat6KPfc, caqCapabilityV08R0401Cat6KPfc=caqCapabilityV08R0401Cat6KPfc, caqCapabilityV08R0601Cat6KPfc3=caqCapabilityV08R0601Cat6KPfc3, caqCapabilityV08R0401Cat6KPfc3b=caqCapabilityV08R0401Cat6KPfc3b, caqCapabilityV08R0701Cat6KPfc3=caqCapabilityV08R0701Cat6KPfc3, caqCapabilityV08R0301Cat6KPfc2=caqCapabilityV08R0301Cat6KPfc2, caqCapabilityV08R0701Cat6KPfc3b=caqCapabilityV08R0701Cat6KPfc3b, ciscoCatOSAclQosCapability=ciscoCatOSAclQosCapability, caqCapabilityV08R0601Cat6KPfc=caqCapabilityV08R0601Cat6KPfc, caqCapabilityV08R0101Cat6KPfc3=caqCapabilityV08R0101Cat6KPfc3)
