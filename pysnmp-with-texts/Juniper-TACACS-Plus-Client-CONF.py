#
# PySNMP MIB module Juniper-TACACS-Plus-Client-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-TACACS-Plus-Client-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, ModuleIdentity, ObjectIdentity, Integer32, Counter64, Gauge32, IpAddress, Counter32, Bits, Unsigned32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Integer32", "Counter64", "Gauge32", "IpAddress", "Counter32", "Bits", "Unsigned32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniTacacsPlusClientAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 57))
juniTacacsPlusClientAgent.setRevisions(('2004-03-02 17:31', '2002-09-06 16:54', '2002-04-08 14:37',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniTacacsPlusClientAgent.setRevisionsDescriptions(('Defined juniTacacsPlusClientHostConfigGroup2', 'Replaced Unisphere names with Juniper names.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniTacacsPlusClientAgent.setLastUpdated('200403021731Z')
if mibBuilder.loadTexts: juniTacacsPlusClientAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniTacacsPlusClientAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniTacacsPlusClientAgent.setDescription('The agent capabilities definitions for the Terminal Access Controller Access Control System Plus (TACACS+) client component of the SNMP agent in the Juniper E-series family of products.')
juniTacacsPlusClientAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 57, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientAgentV1 = juniTacacsPlusClientAgentV1.setProductRelease('Version 1 of the TACACS+ Client component of the JUNOSe SNMP agent.\n        This version of the TACACS+ Client component is supported in JUNOSe 4.1\n        through JUNOSe 5.2.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientAgentV1 = juniTacacsPlusClientAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniTacacsPlusClientAgentV1.setDescription('The MIB supported by the SNMP agent for the TACACS+ Client application in JUNOSe.')
juniTacacsPlusClientAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 57, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientAgentV2 = juniTacacsPlusClientAgentV2.setProductRelease('Version 2 of the Tacacs Plus Client component of the JUNOSe SNMP agent.\n        This version of the Tacacs Plus Client component is supported in JUNOSe\n        5.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTacacsPlusClientAgentV2 = juniTacacsPlusClientAgentV2.setStatus('current')
if mibBuilder.loadTexts: juniTacacsPlusClientAgentV2.setDescription('The MIB supported by the JUNOSe SNMP agent for the Tacacs Plus Client application.')
mibBuilder.exportSymbols("Juniper-TACACS-Plus-Client-CONF", juniTacacsPlusClientAgent=juniTacacsPlusClientAgent, juniTacacsPlusClientAgentV1=juniTacacsPlusClientAgentV1, juniTacacsPlusClientAgentV2=juniTacacsPlusClientAgentV2, PYSNMP_MODULE_ID=juniTacacsPlusClientAgent)
