#
# PySNMP MIB module Juniper-Bridge-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-Bridge-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:01:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, Counter64, IpAddress, TimeTicks, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, MibIdentifier, Gauge32, iso, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "IpAddress", "TimeTicks", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "iso", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniBridgeAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 60))
juniBridgeAgent.setRevisions(('2003-09-30 13:03', '2002-10-02 15:29',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniBridgeAgent.setRevisionsDescriptions(('BRIDGE-MIB: Switched to the SMIv2 version of the standard BRIDGE-MIB.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniBridgeAgent.setLastUpdated('200309301303Z')
if mibBuilder.loadTexts: juniBridgeAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniBridgeAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniBridgeAgent.setDescription('The agent capabilities definitions for the Bridge component of the SNMP agent in the Juniper E-series family of products.')
juniBridgeAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 60, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgeAgentV1 = juniBridgeAgentV1.setProductRelease('Version 1 of the Bridge component of the JUNOSe SNMP agent.  This\n        version of the Bridge component is supported in the Juniper JUNOSe 5.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniBridgeAgentV1 = juniBridgeAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniBridgeAgentV1.setDescription('The MIBs supported by the SNMP agent for the Bridge application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-Bridge-CONF", juniBridgeAgent=juniBridgeAgent, juniBridgeAgentV1=juniBridgeAgentV1, PYSNMP_MODULE_ID=juniBridgeAgent)
