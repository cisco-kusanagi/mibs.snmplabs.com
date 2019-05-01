#
# PySNMP MIB module CISCO-CLASS-BASED-QOS-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CLASS-BASED-QOS-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:53:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, Unsigned32, Counter32, IpAddress, Gauge32, MibIdentifier, TimeTicks, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Counter32", "IpAddress", "Gauge32", "MibIdentifier", "TimeTicks", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCBQosMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 525))
ciscoCBQosMibCapability.setRevisions(('2007-07-17 00:00', '2006-11-08 00:00', '2005-06-22 00:00', '2004-09-01 00:00', '2003-01-24 00:00', '2001-06-13 00:00', '2000-12-01 00:00', '2000-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCBQosMibCapability.setRevisionsDescriptions(('Added capability statements: ciscoCBQosMibCapV12R0218SXFPCat6KPfc2, ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 and ciscoCBQosMibCapV12R0233SXHPCat6K.', 'Added agent capabilities for Cisco IOS XR 3.4 on CRS-1 platform', 'Added agent capabilities for Cisco IOS XR 3.2.0 on CRS-1 platform', 'Added agent capabilities for 12.0(29)S. Added agent capabilities for 12.2(RLS7)S.', 'Added agent capabilities for Catalyst 8540MSR platform.', 'Added agent capabilities for Mainline. Modified capabilities for T train.', 'Added agent capabilities for T train.', 'The capabilities description of Cisco Class Based QoS MIB.',))
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setLastUpdated('200707170000Z')
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-qos@cisco.com')
if mibBuilder.loadTexts: ciscoCBQosMibCapability.setDescription('Agent capabilities for CISCO-CLASS-BASED-QOS-MIB.')
ciscoCBQosMibCapabilityV121R02E7500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R02E7500 = ciscoCBQosMibCapabilityV121R02E7500.setProductRelease('Cisco IOS 12.1(2)E on 7500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R02E7500 = ciscoCBQosMibCapabilityV121R02E7500.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV121R02E7500.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV120R12S7500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV120R12S7500 = ciscoCBQosMibCapabilityV120R12S7500.setProductRelease('Cisco IOS 12.0(12)S on 7500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV120R12S7500 = ciscoCBQosMibCapabilityV120R12S7500.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV120R12S7500.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV121R05T7200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R05T7200 = ciscoCBQosMibCapabilityV121R05T7200.setProductRelease('Cisco IOS 12.1(5)T for 7200/lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R05T7200 = ciscoCBQosMibCapabilityV121R05T7200.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV121R05T7200.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV122R01T7200 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV122R01T7200 = ciscoCBQosMibCapabilityV122R01T7200.setProductRelease('Cisco IOS 12.2(2)T on 7200 and lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV122R01T7200 = ciscoCBQosMibCapabilityV122R01T7200.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV122R01T7200.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV123R01T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV123R01T = ciscoCBQosMibCapabilityV123R01T.setProductRelease('Cisco IOS 12.3(1)T on 7500, 7200 and \n                 lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV123R01T = ciscoCBQosMibCapabilityV123R01T.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV123R01T.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV121R14EB = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R14EB = ciscoCBQosMibCapabilityV121R14EB.setProductRelease('Cisco IOS 12.1(14)EB on Catalyst 8540MSR platform.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV121R14EB = ciscoCBQosMibCapabilityV121R14EB.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV121R14EB.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV12R0306T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R0306T = ciscoCBQosMibCapabilityV12R0306T.setProductRelease('Cisco IOS 12.3(6)T on 7200 and \n                 lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R0306T = ciscoCBQosMibCapabilityV12R0306T.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV12R0306T.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R02S = ciscoCBQosMibCapabilityV12R02S.setProductRelease('Cisco IOS 12.2S for 7500/7200/lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R02S = ciscoCBQosMibCapabilityV12R02S.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV12R02S.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R00S = ciscoCBQosMibCapabilityV12R00S.setProductRelease('Cisco IOS 12.0S for 7500/7200/lower-end platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV12R00S = ciscoCBQosMibCapabilityV12R00S.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV12R00S.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV320CRS1 = ciscoCBQosMibCapabilityV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV320CRS1 = ciscoCBQosMibCapabilityV320CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV320CRS1.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapabilityV3R4CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV3R4CRS1 = ciscoCBQosMibCapabilityV3R4CRS1.setProductRelease('Cisco IOS XR 3.4 on CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapabilityV3R4CRS1 = ciscoCBQosMibCapabilityV3R4CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapabilityV3R4CRS1.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                     and Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc2 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapV12R0218SXFPCat6KPfc2.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 13))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setProductRelease('Cisco IOS 12.2(18)SXF on Catalyst 6000/6500\n                     and Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0218SXFPCat6KPfc3 = ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapV12R0218SXFPCat6KPfc3.setDescription('Class-Based QoS MIB capabilities.')
ciscoCBQosMibCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 525, 14))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0233SXHPCat6K = ciscoCBQosMibCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCBQosMibCapV12R0233SXHPCat6K = ciscoCBQosMibCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoCBQosMibCapV12R0233SXHPCat6K.setDescription('Class-Based QoS MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CLASS-BASED-QOS-MIB-CAPABILITY", ciscoCBQosMibCapabilityV123R01T=ciscoCBQosMibCapabilityV123R01T, ciscoCBQosMibCapabilityV320CRS1=ciscoCBQosMibCapabilityV320CRS1, ciscoCBQosMibCapV12R0218SXFPCat6KPfc2=ciscoCBQosMibCapV12R0218SXFPCat6KPfc2, ciscoCBQosMibCapabilityV122R01T7200=ciscoCBQosMibCapabilityV122R01T7200, ciscoCBQosMibCapabilityV12R00S=ciscoCBQosMibCapabilityV12R00S, ciscoCBQosMibCapabilityV121R02E7500=ciscoCBQosMibCapabilityV121R02E7500, ciscoCBQosMibCapabilityV3R4CRS1=ciscoCBQosMibCapabilityV3R4CRS1, ciscoCBQosMibCapV12R0218SXFPCat6KPfc3=ciscoCBQosMibCapV12R0218SXFPCat6KPfc3, ciscoCBQosMibCapability=ciscoCBQosMibCapability, ciscoCBQosMibCapabilityV120R12S7500=ciscoCBQosMibCapabilityV120R12S7500, ciscoCBQosMibCapabilityV121R05T7200=ciscoCBQosMibCapabilityV121R05T7200, ciscoCBQosMibCapabilityV121R14EB=ciscoCBQosMibCapabilityV121R14EB, ciscoCBQosMibCapabilityV12R0306T=ciscoCBQosMibCapabilityV12R0306T, ciscoCBQosMibCapabilityV12R02S=ciscoCBQosMibCapabilityV12R02S, PYSNMP_MODULE_ID=ciscoCBQosMibCapability, ciscoCBQosMibCapV12R0233SXHPCat6K=ciscoCBQosMibCapV12R0233SXHPCat6K)
