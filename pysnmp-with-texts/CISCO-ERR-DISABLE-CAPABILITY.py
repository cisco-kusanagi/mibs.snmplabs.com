#
# PySNMP MIB module CISCO-ERR-DISABLE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ERR-DISABLE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Unsigned32, iso, ModuleIdentity, TimeTicks, Bits, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "TimeTicks", "Bits", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoErrDisableCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 589))
ciscoErrDisableCapability.setRevisions(('2013-09-25 00:00', '2010-10-29 00:00', '2010-05-05 00:00', '2010-03-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoErrDisableCapability.setRevisionsDescriptions(('Added agent capabilities statement cErrDisableCapV15R0102SYPCat6K. Added VARIATION clause for cErrDisableFeatureConfigurable to capability statement cErrDisableCapV12R0250SYPCat6K.', 'Added agent capabilities statement cErrDisableCapV12R0250SYPCat6K.', 'Added agent capabilities statement cErrDisableCapV12R0254SGPCat4K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoErrDisableCapability.setLastUpdated('201309250000Z')
if mibBuilder.loadTexts: ciscoErrDisableCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoErrDisableCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoErrDisableCapability.setDescription('The capabilities description of CISCO-ERR-DISABLE-MIB.')
cErrDisableCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0233SXI4PCat6K = cErrDisableCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0233SXI4PCat6K = cErrDisableCapV12R0233SXI4PCat6K.setStatus('current')
if mibBuilder.loadTexts: cErrDisableCapV12R0233SXI4PCat6K.setDescription('CISCO-ERR-DISABLE-MIB capabilities.')
cErrDisableCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0254SGPCat4K = cErrDisableCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0254SGPCat4K = cErrDisableCapV12R0254SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: cErrDisableCapV12R0254SGPCat4K.setDescription('CISCO-ERR-DISABLE-MIB capabilities.')
cErrDisableCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0250SYPCat6K = cErrDisableCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0250SYPCat6K = cErrDisableCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cErrDisableCapV12R0250SYPCat6K.setDescription('CISCO-ERR-DISABLE-MIB capabilities.')
cErrDisableCapV15R0102SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV15R0102SYPCat6K = cErrDisableCapV15R0102SYPCat6K.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV15R0102SYPCat6K = cErrDisableCapV15R0102SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: cErrDisableCapV15R0102SYPCat6K.setDescription('CISCO-ERR-DISABLE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ERR-DISABLE-CAPABILITY", cErrDisableCapV12R0250SYPCat6K=cErrDisableCapV12R0250SYPCat6K, cErrDisableCapV12R0254SGPCat4K=cErrDisableCapV12R0254SGPCat4K, ciscoErrDisableCapability=ciscoErrDisableCapability, PYSNMP_MODULE_ID=ciscoErrDisableCapability, cErrDisableCapV12R0233SXI4PCat6K=cErrDisableCapV12R0233SXI4PCat6K, cErrDisableCapV15R0102SYPCat6K=cErrDisableCapV15R0102SYPCat6K)
