#
# PySNMP MIB module CISCO-ERR-DISABLE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ERR-DISABLE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, TimeTicks, Bits, iso, Counter32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Integer32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "TimeTicks", "Bits", "iso", "Counter32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Integer32", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoErrDisableCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 589))
ciscoErrDisableCapability.setRevisions(('2013-09-25 00:00', '2010-10-29 00:00', '2010-05-05 00:00', '2010-03-11 00:00',))
if mibBuilder.loadTexts: ciscoErrDisableCapability.setLastUpdated('201309250000Z')
if mibBuilder.loadTexts: ciscoErrDisableCapability.setOrganization('Cisco Systems, Inc.')
cErrDisableCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0233SXI4PCat6K = cErrDisableCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0233SXI4PCat6K = cErrDisableCapV12R0233SXI4PCat6K.setStatus('current')
cErrDisableCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0254SGPCat4K = cErrDisableCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on CAT4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0254SGPCat4K = cErrDisableCapV12R0254SGPCat4K.setStatus('current')
cErrDisableCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0250SYPCat6K = cErrDisableCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV12R0250SYPCat6K = cErrDisableCapV12R0250SYPCat6K.setStatus('current')
cErrDisableCapV15R0102SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 589, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV15R0102SYPCat6K = cErrDisableCapV15R0102SYPCat6K.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cErrDisableCapV15R0102SYPCat6K = cErrDisableCapV15R0102SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-ERR-DISABLE-CAPABILITY", cErrDisableCapV12R0254SGPCat4K=cErrDisableCapV12R0254SGPCat4K, PYSNMP_MODULE_ID=ciscoErrDisableCapability, cErrDisableCapV12R0233SXI4PCat6K=cErrDisableCapV12R0233SXI4PCat6K, cErrDisableCapV15R0102SYPCat6K=cErrDisableCapV15R0102SYPCat6K, ciscoErrDisableCapability=ciscoErrDisableCapability, cErrDisableCapV12R0250SYPCat6K=cErrDisableCapV12R0250SYPCat6K)
