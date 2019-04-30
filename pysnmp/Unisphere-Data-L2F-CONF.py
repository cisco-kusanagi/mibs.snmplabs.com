#
# PySNMP MIB module Unisphere-Data-L2F-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-L2F-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, ModuleIdentity, ObjectIdentity, NotificationType, Bits, Integer32, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Bits", "Integer32", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdL2fConfigGroup, usdL2fMapGroup, usdL2fStatGroup, usdL2fStatusGroup = mibBuilder.importSymbols("Unisphere-Data-L2F-MIB", "usdL2fConfigGroup", "usdL2fMapGroup", "usdL2fStatGroup", "usdL2fStatusGroup")
usdL2fAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 49))
usdL2fAgent.setRevisions(('2001-04-13 13:37',))
if mibBuilder.loadTexts: usdL2fAgent.setLastUpdated('200104131337Z')
if mibBuilder.loadTexts: usdL2fAgent.setOrganization('Unisphere Networks, Inc.')
usdL2fAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 49, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2fAgentV1 = usdL2fAgentV1.setProductRelease('Version 1 of the L2F component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2F component is supported in the Unisphere\n        RX 3.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2fAgentV1 = usdL2fAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-L2F-CONF", usdL2fAgent=usdL2fAgent, usdL2fAgentV1=usdL2fAgentV1, PYSNMP_MODULE_ID=usdL2fAgent)
