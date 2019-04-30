#
# PySNMP MIB module CISCO-MIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MIP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ObjectIdentity, IpAddress, NotificationType, Integer32, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Unsigned32, MibIdentifier, iso, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "NotificationType", "Integer32", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Unsigned32", "MibIdentifier", "iso", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMIPCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 203))
ciscoMIPCapability.setRevisions(('2003-12-24 00:00', '2002-10-08 00:00', '2000-11-17 00:00',))
if mibBuilder.loadTexts: ciscoMIPCapability.setLastUpdated('200312240000Z')
if mibBuilder.loadTexts: ciscoMIPCapability.setOrganization('Cisco Systems, Inc.')
ciscoMIPCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R02 = ciscoMIPCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R02 = ciscoMIPCapabilityV12R02.setStatus('current')
ciscoMIPCapabilityV12R0204T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0204T = ciscoMIPCapabilityV12R0204T.setProductRelease('Cisco IOS 12.2(4)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0204T = ciscoMIPCapabilityV12R0204T.setStatus('current')
ciscoMIPCapabilityV12R0304T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0304T = ciscoMIPCapabilityV12R0304T.setProductRelease('Cisco IOS 12.3(4)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0304T = ciscoMIPCapabilityV12R0304T.setStatus('current')
mibBuilder.exportSymbols("CISCO-MIP-CAPABILITY", PYSNMP_MODULE_ID=ciscoMIPCapability, ciscoMIPCapabilityV12R0204T=ciscoMIPCapabilityV12R0204T, ciscoMIPCapability=ciscoMIPCapability, ciscoMIPCapabilityV12R02=ciscoMIPCapabilityV12R02, ciscoMIPCapabilityV12R0304T=ciscoMIPCapabilityV12R0304T)
