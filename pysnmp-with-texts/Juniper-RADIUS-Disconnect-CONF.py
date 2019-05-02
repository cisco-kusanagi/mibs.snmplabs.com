#
# PySNMP MIB module Juniper-RADIUS-Disconnect-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-RADIUS-Disconnect-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:04:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, NotificationType, ObjectIdentity, MibIdentifier, ModuleIdentity, Counter64, Unsigned32, Bits, TimeTicks, Gauge32, IpAddress, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Counter64", "Unsigned32", "Bits", "TimeTicks", "Gauge32", "IpAddress", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniRadiusDisconnectAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 63))
juniRadiusDisconnectAgent.setRevisions(('2003-01-13 21:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniRadiusDisconnectAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: juniRadiusDisconnectAgent.setLastUpdated('200301132145Z')
if mibBuilder.loadTexts: juniRadiusDisconnectAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniRadiusDisconnectAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniRadiusDisconnectAgent.setDescription('The agent capabilities definitions for the RADIUS Disconnect component of the SNMP agent in the Juniper E-series family of products.')
juniRadiusDisconnectAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 63, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusDisconnectAgentV1 = juniRadiusDisconnectAgentV1.setProductRelease('Version 1 of the RADIUS Disconnect component of the JUNOSe SNMP agent.\n        This version of the RADIUS Disconnect component is supported in JUNOSe\n        5.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniRadiusDisconnectAgentV1 = juniRadiusDisconnectAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniRadiusDisconnectAgentV1.setDescription('The MIB supported by the SNMP agent for the RADIUS Disconnect application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-RADIUS-Disconnect-CONF", PYSNMP_MODULE_ID=juniRadiusDisconnectAgent, juniRadiusDisconnectAgentV1=juniRadiusDisconnectAgentV1, juniRadiusDisconnectAgent=juniRadiusDisconnectAgent)
