#
# PySNMP MIB module CISCO-MAC-NOTIFICATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MAC-NOTIFICATION-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, Gauge32, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, ObjectIdentity, Counter32, Integer32, NotificationType, Bits, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "ObjectIdentity", "Counter32", "Integer32", "NotificationType", "Bits", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMacNotificationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 327))
ciscoMacNotificationCapability.setRevisions(('2007-07-09 00:00', '2004-02-05 00:00', '2003-11-12 00:00',))
if mibBuilder.loadTexts: ciscoMacNotificationCapability.setLastUpdated('200707090000Z')
if mibBuilder.loadTexts: ciscoMacNotificationCapability.setOrganization('Cisco Systems, Inc.')
cmnCapabilityCatOSV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat4K = cmnCapabilityCatOSV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n                        devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat4K = cmnCapabilityCatOSV08R0101Cat4K.setStatus('current')
cmnCapabilityCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat6K = cmnCapabilityCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat6K = cmnCapabilityCatOSV08R0101Cat6K.setStatus('current')
cmnCapabilityV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0217SXCat6K = cmnCapabilityV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0217SXCat6K = cmnCapabilityV12R0217SXCat6K.setStatus('current')
cmnCapabilityCatOSV08R0301Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0301Cat6K = cmnCapabilityCatOSV08R0301Cat6K.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0301Cat6K = cmnCapabilityCatOSV08R0301Cat6K.setStatus('current')
cmnCapabilityV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0233SXHPCat6K = cmnCapabilityV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0233SXHPCat6K = cmnCapabilityV12R0233SXHPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAC-NOTIFICATION-CAPABILITY", cmnCapabilityCatOSV08R0101Cat6K=cmnCapabilityCatOSV08R0101Cat6K, cmnCapabilityV12R0217SXCat6K=cmnCapabilityV12R0217SXCat6K, ciscoMacNotificationCapability=ciscoMacNotificationCapability, PYSNMP_MODULE_ID=ciscoMacNotificationCapability, cmnCapabilityCatOSV08R0301Cat6K=cmnCapabilityCatOSV08R0301Cat6K, cmnCapabilityV12R0233SXHPCat6K=cmnCapabilityV12R0233SXHPCat6K, cmnCapabilityCatOSV08R0101Cat4K=cmnCapabilityCatOSV08R0101Cat4K)
