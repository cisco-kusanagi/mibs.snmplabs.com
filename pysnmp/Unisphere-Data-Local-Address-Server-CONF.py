#
# PySNMP MIB module Unisphere-Data-Local-Address-Server-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Local-Address-Server-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, ModuleIdentity, Integer32, Gauge32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Bits, ObjectIdentity, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ModuleIdentity", "Integer32", "Gauge32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Bits", "ObjectIdentity", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usdAddressPoolGroup, usdAddressPoolTrapGroup, usdAddressPoolGroup3, usdAddressPoolGroup2 = mibBuilder.importSymbols("Unisphere-Data-ADDRESS-POOL-MIB", "usdAddressPoolGroup", "usdAddressPoolTrapGroup", "usdAddressPoolGroup3", "usdAddressPoolGroup2")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdLocalAddressServerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25))
usdLocalAddressServerAgent.setRevisions(('2002-05-06 19:20', '2001-05-02 13:22',))
if mibBuilder.loadTexts: usdLocalAddressServerAgent.setLastUpdated('200205061920Z')
if mibBuilder.loadTexts: usdLocalAddressServerAgent.setOrganization('Unisphere Networks, Inc.')
usdLocalAddressServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV1 = usdLocalAddressServerAgentV1.setProductRelease('Version 1 of the Local Address Server component of the Unisphere\n        Routing Switch SNMP agent.  This version of the Local Address Server\n        component was supported in the Unisphere RX 1.3 thru RX 3.1 system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV1 = usdLocalAddressServerAgentV1.setStatus('obsolete')
usdLocalAddressServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV2 = usdLocalAddressServerAgentV2.setProductRelease('Version 2 of the Local Address Server component of the Unisphere\n        Routing Switch SNMP agent.  This version of the Local Address Server\n        component was supported in the Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV2 = usdLocalAddressServerAgentV2.setStatus('obsolete')
usdLocalAddressServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 25, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV3 = usdLocalAddressServerAgentV3.setProductRelease('Version 3 of the Local Address Server component of the Unisphere\n        Routing Switch SNMP agent.  This version of the Local Address Server\n        component is supported in the Unisphere RX 3.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLocalAddressServerAgentV3 = usdLocalAddressServerAgentV3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-Local-Address-Server-CONF", usdLocalAddressServerAgentV3=usdLocalAddressServerAgentV3, usdLocalAddressServerAgentV2=usdLocalAddressServerAgentV2, usdLocalAddressServerAgent=usdLocalAddressServerAgent, PYSNMP_MODULE_ID=usdLocalAddressServerAgent, usdLocalAddressServerAgentV1=usdLocalAddressServerAgentV1)
