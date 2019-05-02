#
# PySNMP MIB module Juniper-RADIUS-Proxy-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-RADIUS-Proxy-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter32, TimeTicks, iso, Integer32, Counter64, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, IpAddress, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "iso", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "IpAddress", "ModuleIdentity", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniRadiusProxyAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 68))
juniRadiusProxyAgent.setRevisions(('2004-01-23 19:16',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniRadiusProxyAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: juniRadiusProxyAgent.setLastUpdated('200401231916Z')
if mibBuilder.loadTexts: juniRadiusProxyAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniRadiusProxyAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniRadiusProxyAgent.setDescription('The agent capabilities definitions for the RADIUS Proxy component of the SNMP agent in the Juniper E-series family of products.')
juniRadiusProxyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 68, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusProxyAgentV1 = juniRadiusProxyAgentV1.setProductRelease('Version 1 of the RADIUS Proxy component of the JUNOSe SNMP agent.  This\n        version of the RADIUS Proxy component is supported in JUNOSe 6.0 and\n        subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusProxyAgentV1 = juniRadiusProxyAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniRadiusProxyAgentV1.setDescription('The MIBs supported by the JUNOSe SNMP agent for the RADIUS Proxy application.')
mibBuilder.exportSymbols("Juniper-RADIUS-Proxy-CONF", juniRadiusProxyAgentV1=juniRadiusProxyAgentV1, PYSNMP_MODULE_ID=juniRadiusProxyAgent, juniRadiusProxyAgent=juniRadiusProxyAgent)
