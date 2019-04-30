#
# PySNMP MIB module Unisphere-Data-IGMP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-IGMP-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Counter32, MibIdentifier, ObjectIdentity, Unsigned32, IpAddress, NotificationType, Integer32, Gauge32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Counter32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "Integer32", "Gauge32", "TimeTicks", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIgmpProxyInterfaceGroup, usdIgmpProxyCacheGroup = mibBuilder.importSymbols("Unisphere-Data-IGMP-MIB", "usdIgmpProxyInterfaceGroup", "usdIgmpProxyCacheGroup")
usdIgmpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19))
usdIgmpAgent.setRevisions(('2001-03-28 17:20',))
if mibBuilder.loadTexts: usdIgmpAgent.setLastUpdated('200103281720Z')
if mibBuilder.loadTexts: usdIgmpAgent.setOrganization('Unisphere Networks, Inc.')
usdIgmpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 19, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIgmpAgentV1 = usdIgmpAgentV1.setProductRelease('Version 1 of the IGMP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the IGMP component is supported in the Unisphere\n        RX 3.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdIgmpAgentV1 = usdIgmpAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-IGMP-CONF", PYSNMP_MODULE_ID=usdIgmpAgent, usdIgmpAgent=usdIgmpAgent, usdIgmpAgentV1=usdIgmpAgentV1)
