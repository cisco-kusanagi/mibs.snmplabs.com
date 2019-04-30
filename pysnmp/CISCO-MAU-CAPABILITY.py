#
# PySNMP MIB module CISCO-MAU-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MAU-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, Counter32, ObjectIdentity, Unsigned32, TimeTicks, Bits, iso, Gauge32, NotificationType, Integer32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ObjectIdentity", "Unsigned32", "TimeTicks", "Bits", "iso", "Gauge32", "NotificationType", "Integer32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMauCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 411))
ciscoMauCapability.setRevisions(('2014-07-30 00:00', '2011-09-28 00:00', '2008-10-28 00:00', '2007-07-13 00:00', '2004-10-22 00:00',))
if mibBuilder.loadTexts: ciscoMauCapability.setLastUpdated('201407300000Z')
if mibBuilder.loadTexts: ciscoMauCapability.setOrganization('Cisco Systems, Inc.')
ciscoMauCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapCatOSV08R0401 = ciscoMauCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapCatOSV08R0401 = ciscoMauCapCatOSV08R0401.setStatus('current')
ciscoMauCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXHPCat6K = ciscoMauCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXHPCat6K = ciscoMauCapV12R0233SXHPCat6K.setStatus('current')
ciscoMauCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXIPCat6K = ciscoMauCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXIPCat6K = ciscoMauCapV12R0233SXIPCat6K.setStatus('current')
ciscoMauCapV12R0233SXJPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXJPCat6K = ciscoMauCapV12R0233SXJPCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXJPCat6K = ciscoMauCapV12R0233SXJPCat6K.setStatus('current')
ciscoMauCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV15R0001SYPCat6K = ciscoMauCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV15R0001SYPCat6K = ciscoMauCapV15R0001SYPCat6K.setStatus('current')
ciscoMauCapV05R0003U0401PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV05R0003U0401PN3K = ciscoMauCapV05R0003U0401PN3K.setProductRelease('Cisco NX-OS 5.0(3)U4(1) on Nexus 3000 series\n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV05R0003U0401PN3K = ciscoMauCapV05R0003U0401PN3K.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAU-CAPABILITY", ciscoMauCapV12R0233SXHPCat6K=ciscoMauCapV12R0233SXHPCat6K, ciscoMauCapability=ciscoMauCapability, ciscoMauCapV12R0233SXIPCat6K=ciscoMauCapV12R0233SXIPCat6K, ciscoMauCapV12R0233SXJPCat6K=ciscoMauCapV12R0233SXJPCat6K, ciscoMauCapV05R0003U0401PN3K=ciscoMauCapV05R0003U0401PN3K, PYSNMP_MODULE_ID=ciscoMauCapability, ciscoMauCapCatOSV08R0401=ciscoMauCapCatOSV08R0401, ciscoMauCapV15R0001SYPCat6K=ciscoMauCapV15R0001SYPCat6K)
