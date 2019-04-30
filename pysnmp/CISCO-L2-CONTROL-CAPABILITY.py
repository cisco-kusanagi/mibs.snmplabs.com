#
# PySNMP MIB module CISCO-L2-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L2-CONTROL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:46:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ObjectIdentity, MibIdentifier, ModuleIdentity, iso, Unsigned32, IpAddress, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Counter32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "iso", "Unsigned32", "IpAddress", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Counter32", "Gauge32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoL2ControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 397))
ciscoL2ControlCapability.setRevisions(('2013-10-16 00:00', '2007-06-30 00:00', '2007-02-28 00:00', '2004-11-01 00:00', '2004-03-29 00:00', '2003-10-31 00:00',))
if mibBuilder.loadTexts: ciscoL2ControlCapability.setLastUpdated('201310160000Z')
if mibBuilder.loadTexts: ciscoL2ControlCapability.setOrganization('Cisco Systems, Inc.')
clcCapabilityV12R0217aSXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV12R0217aSXCat6K = clcCapabilityV12R0217aSXCat6K.setProductRelease('Cisco IOS 12.2(17a)SX on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV12R0217aSXCat6K = clcCapabilityV12R0217aSXCat6K.setStatus('current')
clcCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityCatOSV08R0301 = clcCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityCatOSV08R0301 = clcCapabilityCatOSV08R0301.setStatus('current')
clcCapabilityCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityCatOSV08R0601 = clcCapabilityCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityCatOSV08R0601 = clcCapabilityCatOSV08R0601.setStatus('current')
clcCapabilityV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV12R0233SXHPCat6K = clcCapabilityV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                       series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV12R0233SXHPCat6K = clcCapabilityV12R0233SXHPCat6K.setStatus('current')
clcCapabilityV6R0002U0102PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV6R0002U0102PN3K = clcCapabilityV6R0002U0102PN3K.setProductRelease('Cisco NX-OS 6.0(2)U1(2) on Nexus 3000\n                       series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV6R0002U0102PN3K = clcCapabilityV6R0002U0102PN3K.setStatus('current')
mibBuilder.exportSymbols("CISCO-L2-CONTROL-CAPABILITY", PYSNMP_MODULE_ID=ciscoL2ControlCapability, clcCapabilityCatOSV08R0301=clcCapabilityCatOSV08R0301, clcCapabilityCatOSV08R0601=clcCapabilityCatOSV08R0601, clcCapabilityV12R0233SXHPCat6K=clcCapabilityV12R0233SXHPCat6K, ciscoL2ControlCapability=ciscoL2ControlCapability, clcCapabilityV12R0217aSXCat6K=clcCapabilityV12R0217aSXCat6K, clcCapabilityV6R0002U0102PN3K=clcCapabilityV6R0002U0102PN3K)
