#
# PySNMP MIB module Juniper-Dos-Protection-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Dos-Protection-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, Counter32, ObjectIdentity, IpAddress, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, TimeTicks, NotificationType, Gauge32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "ObjectIdentity", "IpAddress", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "iso", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDosProtectionAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 76))
juniDosProtectionAgent.setRevisions(('2006-07-01 00:00', '2006-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDosProtectionAgent.setRevisionsDescriptions(('Added dos-protection-group support.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniDosProtectionAgent.setLastUpdated('200511111830Z')
if mibBuilder.loadTexts: juniDosProtectionAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDosProtectionAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniDosProtectionAgent.setDescription('The agent capabilities definitions for the Dos Protection component of the SNMP agent in the Juniper E-series family of products.')
juniDosProtectionAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 76, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionAgentV1 = juniDosProtectionAgentV1.setProductRelease('Version 1 of the Dos Protection component of the JUNOSe SNMP agent.\n        This version of the Dos Protection component is supported in JUNOSe 7.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionAgentV1 = juniDosProtectionAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniDosProtectionAgentV1.setDescription('The MIB supported by the JUNOSe SNMP agent for the Dos Protection application.')
juniDosProtectionAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 76, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionAgentV2 = juniDosProtectionAgentV2.setProductRelease('Version 2 of the Dos Protection component of the JUNOSe SNMP agent.\n        This version of the Dos Protection component is supported in JUNOSe x.y\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionAgentV2 = juniDosProtectionAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniDosProtectionAgentV2.setDescription('The MIB supported by the JUNOSe SNMP agent for the Dos Protection application.')
mibBuilder.exportSymbols("Juniper-Dos-Protection-CONF", juniDosProtectionAgent=juniDosProtectionAgent, PYSNMP_MODULE_ID=juniDosProtectionAgent, juniDosProtectionAgentV2=juniDosProtectionAgentV2, juniDosProtectionAgentV1=juniDosProtectionAgentV1)
