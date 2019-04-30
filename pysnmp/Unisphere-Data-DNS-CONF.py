#
# PySNMP MIB module Unisphere-Data-DNS-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DNS-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, iso, Gauge32, MibIdentifier, Bits, IpAddress, Counter32, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "iso", "Gauge32", "MibIdentifier", "Bits", "IpAddress", "Counter32", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdDnsEnableGroup, usdDnsLocalDomainNameListGroup, usdDnsServerListGroup = mibBuilder.importSymbols("Unisphere-Data-DNS-MIB", "usdDnsEnableGroup", "usdDnsLocalDomainNameListGroup", "usdDnsServerListGroup")
usdDnsAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9))
usdDnsAgent.setRevisions(('2001-03-27 23:00',))
if mibBuilder.loadTexts: usdDnsAgent.setLastUpdated('200103272300Z')
if mibBuilder.loadTexts: usdDnsAgent.setOrganization('Unisphere Networks, Inc.')
usdDnsAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 9, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsAgentV1 = usdDnsAgentV1.setProductRelease('Version 1 of the DNS component of the Unisphere Routing Switch SNMP\n        agent.  This version of the DNS component is supported in the Unisphere\n        RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDnsAgentV1 = usdDnsAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-DNS-CONF", PYSNMP_MODULE_ID=usdDnsAgent, usdDnsAgentV1=usdDnsAgentV1, usdDnsAgent=usdDnsAgent)
