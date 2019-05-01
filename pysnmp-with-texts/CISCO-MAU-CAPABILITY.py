#
# PySNMP MIB module CISCO-MAU-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MAU-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:06:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, Bits, Gauge32, NotificationType, ObjectIdentity, iso, TimeTicks, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Gauge32", "NotificationType", "ObjectIdentity", "iso", "TimeTicks", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMauCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 411))
ciscoMauCapability.setRevisions(('2014-07-30 00:00', '2011-09-28 00:00', '2008-10-28 00:00', '2007-07-13 00:00', '2004-10-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMauCapability.setRevisionsDescriptions(('Added capability statement ciscoMauCapV05R0003U0401PN3K.', 'Added capability statement ciscoMauCapV12R0233SXJPCat6K and ciscoMauCapV15R0001SYPCat6K.', 'Added capability statement ciscoMauCapV12R0233SXIPCat6K.', 'Added capability statement ciscoMauCapV12R0233SXHPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMauCapability.setLastUpdated('201407300000Z')
if mibBuilder.loadTexts: ciscoMauCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMauCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMauCapability.setDescription('The capabilities description of MAU-MIB.')
ciscoMauCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapCatOSV08R0401 = ciscoMauCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapCatOSV08R0401 = ciscoMauCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoMauCapCatOSV08R0401.setDescription('MAU-MIB capabilities.')
ciscoMauCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXHPCat6K = ciscoMauCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXHPCat6K = ciscoMauCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoMauCapV12R0233SXHPCat6K.setDescription('MAU-MIB capabilities.')
ciscoMauCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXIPCat6K = ciscoMauCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXIPCat6K = ciscoMauCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoMauCapV12R0233SXIPCat6K.setDescription('MAU-MIB capabilities.')
ciscoMauCapV12R0233SXJPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXJPCat6K = ciscoMauCapV12R0233SXJPCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV12R0233SXJPCat6K = ciscoMauCapV12R0233SXJPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoMauCapV12R0233SXJPCat6K.setDescription('MAU-MIB capabilities.')
ciscoMauCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV15R0001SYPCat6K = ciscoMauCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV15R0001SYPCat6K = ciscoMauCapV15R0001SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoMauCapV15R0001SYPCat6K.setDescription('MAU-MIB capabilities.')
ciscoMauCapV05R0003U0401PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 411, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV05R0003U0401PN3K = ciscoMauCapV05R0003U0401PN3K.setProductRelease('Cisco NX-OS 5.0(3)U4(1) on Nexus 3000 series\n                     devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMauCapV05R0003U0401PN3K = ciscoMauCapV05R0003U0401PN3K.setStatus('current')
if mibBuilder.loadTexts: ciscoMauCapV05R0003U0401PN3K.setDescription('MAU-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MAU-CAPABILITY", ciscoMauCapV12R0233SXIPCat6K=ciscoMauCapV12R0233SXIPCat6K, ciscoMauCapability=ciscoMauCapability, ciscoMauCapCatOSV08R0401=ciscoMauCapCatOSV08R0401, ciscoMauCapV05R0003U0401PN3K=ciscoMauCapV05R0003U0401PN3K, ciscoMauCapV15R0001SYPCat6K=ciscoMauCapV15R0001SYPCat6K, PYSNMP_MODULE_ID=ciscoMauCapability, ciscoMauCapV12R0233SXJPCat6K=ciscoMauCapV12R0233SXJPCat6K, ciscoMauCapV12R0233SXHPCat6K=ciscoMauCapV12R0233SXHPCat6K)
