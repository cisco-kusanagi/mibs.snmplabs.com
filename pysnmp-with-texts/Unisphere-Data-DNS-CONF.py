#
# PySNMP MIB module Unisphere-Data-DNS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DNS-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, iso, Unsigned32, MibIdentifier, Integer32, Counter64, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "iso", "Unsigned32", "MibIdentifier", "Integer32", "Counter64", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdDnsLocalDomainNameListGroup, usdDnsEnableGroup, usdDnsServerListGroup = mibBuilder.importSymbols("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListGroup", "usdDnsEnableGroup", "usdDnsServerListGroup")
usdDnsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9))
usdDnsAgent.setRevisions(('2001-03-27 23:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdDnsAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdDnsAgent.setLastUpdated('200103272300Z')
if mibBuilder.loadTexts: usdDnsAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdDnsAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdDnsAgent.setDescription('The agent capabilities definitions for the DNS component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdDnsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsAgentV1 = usdDnsAgentV1.setProductRelease('Version 1 of the DNS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DNS component is supported in the Unisphere\n        RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsAgentV1 = usdDnsAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdDnsAgentV1.setDescription('The MIB supported by the SNMP agent for the DNS application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-DNS-CONF", PYSNMP_MODULE_ID=usdDnsAgent, usdDnsAgent=usdDnsAgent, usdDnsAgentV1=usdDnsAgentV1)
