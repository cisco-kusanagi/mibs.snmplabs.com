#
# PySNMP MIB module Juniper-IKE-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IKE-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, Counter64, Bits, iso, Counter32, TimeTicks, ModuleIdentity, ObjectIdentity, IpAddress, Unsigned32, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Bits", "iso", "Counter32", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Unsigned32", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniIkeAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 66))
juniIkeAgent.setRevisions(('2004-01-23 15:21', '2003-10-23 20:17',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniIkeAgent.setRevisionsDescriptions(('Replaced the juniIkeSaTable with the juniIkeSa2Table.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniIkeAgent.setLastUpdated('200401231521Z')
if mibBuilder.loadTexts: juniIkeAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniIkeAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniIkeAgent.setDescription('The agent capabilities definitions for the Internet Key Exchange (IKE) component of the SNMP agent in the Juniper E-series family of products.')
juniIkeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 66, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeAgentV1 = juniIkeAgentV1.setProductRelease('Version 1 of the IKE component of the JUNOSe SNMP agent.  This version\n        of the IKE component was supported in JUNOSe 5.3 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeAgentV1 = juniIkeAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniIkeAgentV1.setDescription('The MIB supported by the JUNOSe SNMP agent for the IKE application in JUNOSe. These capabilities became obsolete when the juniIkeSa2Table replaced the juniIkeSaTable.')
juniIkeAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 66, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeAgentV2 = juniIkeAgentV2.setProductRelease('Version 2 of the IKE component of the JUNOSe SNMP agent.  This version\n        of the IKE component is supported in JUNOSe 6.0 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeAgentV2 = juniIkeAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniIkeAgentV2.setDescription('The MIB supported by the JUNOSe SNMP agent for the IKE application.')
mibBuilder.exportSymbols("Juniper-IKE-CONF", juniIkeAgentV2=juniIkeAgentV2, PYSNMP_MODULE_ID=juniIkeAgent, juniIkeAgentV1=juniIkeAgentV1, juniIkeAgent=juniIkeAgent)
