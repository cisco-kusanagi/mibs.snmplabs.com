#
# PySNMP MIB module Juniper-Bridging-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Bridging-Manager-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter64, Bits, Integer32, Counter32, IpAddress, iso, Unsigned32, Gauge32, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Integer32", "Counter32", "IpAddress", "iso", "Unsigned32", "Gauge32", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniBridgingMgrAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 61))
juniBridgingMgrAgent.setRevisions(('2003-09-26 20:47', '2002-10-02 15:26',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniBridgingMgrAgent.setRevisionsDescriptions(('Fixed the Juniper-Bridging-Manager-MIB name.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniBridgingMgrAgent.setLastUpdated('200309262047Z')
if mibBuilder.loadTexts: juniBridgingMgrAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniBridgingMgrAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniBridgingMgrAgent.setDescription('The agent capabilities definitions for the Bridging Manager component of the SNMP agent in the Juniper E-series family of products.')
juniBridgingMgrAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 61, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgingMgrAgentV1 = juniBridgingMgrAgentV1.setProductRelease('Version 1 of the Bridging Manager component of the JUNOSe SNMP agent.\n        This version of the Bridging Manager component is supported in JUNOSe\n        5.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgingMgrAgentV1 = juniBridgingMgrAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniBridgingMgrAgentV1.setDescription('The MIB supported by the SNMP agent for the Bridging Manager application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Bridging-Manager-CONF", juniBridgingMgrAgent=juniBridgingMgrAgent, PYSNMP_MODULE_ID=juniBridgingMgrAgent, juniBridgingMgrAgentV1=juniBridgingMgrAgentV1)
