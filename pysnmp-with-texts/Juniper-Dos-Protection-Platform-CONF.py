#
# PySNMP MIB module Juniper-Dos-Protection-Platform-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Dos-Protection-Platform-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
iso, Bits, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Unsigned32, MibIdentifier, ModuleIdentity, TimeTicks, IpAddress, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "IpAddress", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDosProtectionPlatformAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 77))
juniDosProtectionPlatformAgent.setRevisions(('2006-07-01 00:00', '2006-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDosProtectionPlatformAgent.setRevisionsDescriptions(('Added support for MAC address in the flow table as well as in the flow traps.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniDosProtectionPlatformAgent.setLastUpdated('200511111831Z')
if mibBuilder.loadTexts: juniDosProtectionPlatformAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDosProtectionPlatformAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniDosProtectionPlatformAgent.setDescription('The agent capabilities definitions for the Dos Protection Platform component of the SNMP agent in the Juniper E-series family of products.')
juniDosProtectionPlatformAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 77, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionPlatformAgentV1 = juniDosProtectionPlatformAgentV1.setProductRelease('Version 1 of the Dos Protection Platform component of the JUNOSe SNMP agent.\n        This version of the Dos Protection Platform component is supported in JUNOSe 7.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionPlatformAgentV1 = juniDosProtectionPlatformAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniDosProtectionPlatformAgentV1.setDescription('The MIB supported by the JUNOSe SNMP agent for the Dos Protection Platform application.')
juniDosProtectionPlatformAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 77, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionPlatformAgentV2 = juniDosProtectionPlatformAgentV2.setProductRelease('Version 1 of the Dos Protection Platform component of the JUNOSe SNMP agent.\n        This version of the Dos Protection Platform component is supported in JUNOSe -.-\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionPlatformAgentV2 = juniDosProtectionPlatformAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniDosProtectionPlatformAgentV2.setDescription('The MIB supported by the JUNOSe SNMP agent for the Dos Protection Platform application.')
mibBuilder.exportSymbols("Juniper-Dos-Protection-Platform-CONF", juniDosProtectionPlatformAgentV1=juniDosProtectionPlatformAgentV1, juniDosProtectionPlatformAgentV2=juniDosProtectionPlatformAgentV2, juniDosProtectionPlatformAgent=juniDosProtectionPlatformAgent, PYSNMP_MODULE_ID=juniDosProtectionPlatformAgent)
