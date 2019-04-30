#
# PySNMP MIB module CISCO-HW-MODULE-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HW-MODULE-CONTROL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, Bits, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Gauge32, ModuleIdentity, Counter64, NotificationType, IpAddress, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Gauge32", "ModuleIdentity", "Counter64", "NotificationType", "IpAddress", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHwModuleControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 588))
ciscoHwModuleControlCapability.setRevisions(('2012-09-07 00:00', '2011-09-27 00:00', '2010-03-17 00:00',))
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setOrganization('Cisco Systems, Inc.')
chmcCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setStatus('current')
chmcCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setStatus('current')
chmcCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-HW-MODULE-CONTROL-CAPABILITY", chmcCapV15R0001SYPCat6K=chmcCapV15R0001SYPCat6K, PYSNMP_MODULE_ID=ciscoHwModuleControlCapability, chmcCapV12R0233SXI4PCat6K=chmcCapV12R0233SXI4PCat6K, ciscoHwModuleControlCapability=ciscoHwModuleControlCapability, chmcCapV15R0001SY1PCat6K=chmcCapV15R0001SY1PCat6K)
