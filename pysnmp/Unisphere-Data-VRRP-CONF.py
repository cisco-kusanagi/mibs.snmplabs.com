#
# PySNMP MIB module Unisphere-Data-VRRP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-VRRP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:26:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, Counter64, ObjectIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, TimeTicks, Counter32, IpAddress, Unsigned32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "ObjectIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "TimeTicks", "Counter32", "IpAddress", "Unsigned32", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
vrrpStatsGroup, vrrpTrapGroup, vrrpNotificationGroup, vrrpOperGroup = mibBuilder.importSymbols("VRRP-MIB", "vrrpStatsGroup", "vrrpTrapGroup", "vrrpNotificationGroup", "vrrpOperGroup")
usdVrrpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 53))
usdVrrpAgent.setRevisions(('2002-01-24 15:20',))
if mibBuilder.loadTexts: usdVrrpAgent.setLastUpdated('200201241520Z')
if mibBuilder.loadTexts: usdVrrpAgent.setOrganization('Unisphere Networks, Inc.')
usdVrrpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 53, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdVrrpAgentV1 = usdVrrpAgentV1.setProductRelease('Version 1 of the VRRP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the VRRP component is supported in the Unisphere\n        RX 3.4 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdVrrpAgentV1 = usdVrrpAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-VRRP-CONF", PYSNMP_MODULE_ID=usdVrrpAgent, usdVrrpAgentV1=usdVrrpAgentV1, usdVrrpAgent=usdVrrpAgent)
